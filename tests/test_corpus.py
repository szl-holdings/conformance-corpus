"""Conformance corpus tests for scientific-evidence-gate (standard library only).

What these tests check, for every directory in ``entries/``:

* ``entry.json`` validates against ``intake-schema.json`` and the
  ``permissions-schema.json`` it references. A small JSON Schema subset
  validator below interprets the schema files themselves, so the tests
  follow the schemas. It raises on any keyword it does not implement
  instead of silently accepting it.
* The permission rules are also checked by hand: training permission is
  never implied by evaluation permission. ``training_allowed`` must be false
  when ``evidence_of_grant`` is NOASSERTION.
* A synthetic entry is labeled synthetic in ``entry.json``, ``claim.md`` and
  ``limitations.md``, and says what passing does not prove.
* The entry has the layout that the corpus README declares.
* ``expected_outcome.command`` from ``entry.json`` is run once through
  science-gate. The run uses list arguments (never a shell),
  ``--output`` in an OS temporary directory, a fixed clock and the
  science-gate source tree on ``PYTHONPATH``. The run is then compared with
  the INTENDED outcome: status, exit code, reason, failure modes, every
  ``must_mention`` string, and the optional ``must_not_mention``,
  ``reasons_include`` and ``headline_prefix`` fields.

For every directory in ``templates/``, the tests check that the template
has the full layout.

``CorpusHygieneTests`` check the publication rules on every corpus file:
no local home path, local user name or email address; no build junk; LF line
endings; DOIs under the 10.5555 test prefix only; the corpus is never called
a benchmark; no license is chosen; no template placeholder is left in an
entry; every receipt is UNSIGNED and says it does not establish scientific
validity; every ``environment.lock`` names the science-gate version and a
commit that exists in the science-gate repository (``git cat-file -t``).

A divergence between a run and the intended outcome is an ordinary test
failure, with one exception: ``DOCUMENTED_GAPS``. A row there marks one
assertion with ``unittest.expectedFailure``, and only while the entry's own
``known_failures`` still contains the row's anchor text. Every such
assertion also has a companion test. The companion fails normally if the
run diverges in a way the known failure does not describe. The summary
printed at the end of the run explains each expected failure.

Passing these tests shows that science-gate behaves as declared on these
synthetic fixtures only. It does not show that science-gate catches failures
outside the corpus, or that any scientific conclusion is true. It does not
show that science-gate is fit for any particular use.

Environment:
  SCIENCE_GATE_SRC      science-gate ``src`` directory
                        (default: ../scientific-evidence-gate/src relative to the corpus root)
  SCIENCE_GATE_PYTHON   interpreter used to run science-gate (default: the interpreter running the tests)
  CORPUS_RUN_TIMEOUT    seconds allowed per science-gate run (default: 600)
"""

from __future__ import annotations

import dataclasses
import getpass
import hashlib
import json
import locale
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from pathlib import Path
from typing import Any, Callable

# ---------------------------------------------------------------------------
# Locations and fixed settings
# ---------------------------------------------------------------------------

CORPUS_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = CORPUS_ROOT / "entries"
TEMPLATES_DIR = CORPUS_ROOT / "templates"
README_PATH = CORPUS_ROOT / "README.md"
INTAKE_SCHEMA_PATH = CORPUS_ROOT / "intake-schema.json"

FIXED_TIME = "2026-09-26T00:00:00Z"
EXPECTED_RESULTS_SCHEMA = "conformance-corpus-expected-results/v1"
RUN_TIMEOUT_SECONDS = int(os.environ.get("CORPUS_RUN_TIMEOUT", "600"))
PYTHON = os.environ.get("SCIENCE_GATE_PYTHON") or sys.executable


def _seg_src() -> Path:
    configured = os.environ.get("SCIENCE_GATE_SRC")
    if configured:
        return Path(configured).resolve()
    return (CORPUS_ROOT.parent / "scientific-evidence-gate" / "src").resolve()


SEG_SRC = _seg_src()

#: The subcommands the tests know how to read: (machine document, human report).
#: ``impact`` and ``revalidate`` are not here: they write graph state into the
#: entry itself, and an entry must never be modified by its own evaluation.
SUBCOMMAND_OUTPUTS = {
    "verify": ("run.json", "report.md"),
    "mutate": ("mutation-report.json", "mutation-report.md"),
}

# ---------------------------------------------------------------------------
# Documented tool gaps
# ---------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class DocumentedGap:
    """One assertion that is known to diverge, as an entry's ``known_failures`` records it.

    ``anchor`` must occur verbatim in one of the entry's ``known_failures``
    strings. If the anchor is not there, the gap is not applied, the
    assertion runs as an ordinary test, and
    ``test_documented_gap_table_matches_known_failures`` fails.
    ``documented_actual`` is the diverging value that the known failure
    describes. A companion test accepts only the intended value or this one.
    """

    entry_id: str
    aspect: str
    anchor: str
    documented_actual: Any = None


DOCUMENTED_GAPS: tuple[DocumentedGap, ...] = (
    DocumentedGap(
        entry_id="partial-execution-synthetic-01",
        aspect="reason",
        anchor="primary reason is INSUFFICIENT_EVIDENCE, not the intended PARTIAL_EXECUTION",
        documented_actual="INSUFFICIENT_EVIDENCE",
    ),
    DocumentedGap(
        entry_id="partial-execution-synthetic-01",
        aspect="failure_modes",
        anchor="reports failure_modes ['OMITTED_POPULATION'], not the intended ['PARTIAL_EXECUTION']",
        documented_actual=["OMITTED_POPULATION"],
    ),
    DocumentedGap(
        entry_id="partial-execution-synthetic-01",
        aspect="must_mention:PARTIAL_EXECUTION",
        anchor="does not contain the must_mention string 'PARTIAL_EXECUTION'",
    ),
)

# ---------------------------------------------------------------------------
# A JSON Schema subset validator
# ---------------------------------------------------------------------------

#: Keywords that only annotate and never constrain.
ANNOTATION_KEYWORDS = frozenset({"$schema", "$id", "$comment", "title", "description", "default", "examples"})
#: Keywords this validator implements. Any other keyword raises SchemaUnsupported.
SUPPORTED_KEYWORDS = frozenset(
    {
        "type", "enum", "const", "required", "properties", "additionalProperties", "pattern",
        "minLength", "minItems", "items", "$ref", "allOf", "if", "then", "else",
    }
)


class SchemaUnsupported(Exception):
    """The schema uses a keyword or form that this validator does not implement."""


def json_equal(a: Any, b: Any) -> bool:
    """JSON equality: ``true`` is not ``1``, and ``1`` equals ``1.0``."""
    if isinstance(a, bool) or isinstance(b, bool):
        return isinstance(a, bool) and isinstance(b, bool) and a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(json_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(json_equal(a[k], b[k]) for k in a)
    return type(a) is type(b) and a == b


def json_type_name(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def type_matches(value: Any, name: str) -> bool:
    if name == "object":
        return isinstance(value, dict)
    if name == "array":
        return isinstance(value, list)
    if name == "string":
        return isinstance(value, str)
    if name == "boolean":
        return isinstance(value, bool)
    if name == "null":
        return value is None
    if name == "integer":
        if isinstance(value, bool):
            return False
        return isinstance(value, int) or (isinstance(value, float) and value.is_integer())
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    raise SchemaUnsupported(f"type {name!r} is not implemented")


def ecma_pattern_search(pattern: str, value: str) -> bool:
    """``pattern`` semantics: an unanchored search, with ``$`` meaning the very end.

    In Python ``$`` also matches before a trailing newline, and ECMA-262
    ``$`` (without the multiline flag) does not. A final unescaped ``$`` is
    therefore rewritten as ``\\Z``. ``re.ASCII`` keeps ``\\d`` and ``\\w`` ASCII-only, as in ECMA-262.
    """
    if pattern.endswith("$") and not pattern.endswith("\\$"):
        pattern = pattern[:-1] + r"\Z"
    return re.search(pattern, value, flags=re.ASCII) is not None


class SchemaValidator:
    """Validates an instance against schema files, resolving ``$ref`` to sibling files."""

    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self._cache: dict[str, Any] = {}

    def load(self, name: str) -> Any:
        if name not in self._cache:
            path = (self.base_dir / name).resolve()
            if path.parent != self.base_dir.resolve():
                raise SchemaUnsupported(f"$ref {name!r} leaves the schema directory")
            with open(path, encoding="utf-8") as handle:
                self._cache[name] = json.load(handle)
        return self._cache[name]

    def _resolve(self, ref: str) -> Any:
        file_part, _, fragment = ref.partition("#")
        if fragment not in ("", "/"):
            raise SchemaUnsupported(f"$ref fragment {ref!r} is not implemented")
        if not file_part:
            raise SchemaUnsupported(f"$ref {ref!r}: same-document references are not implemented")
        return self.load(file_part)

    def validate(self, instance: Any, schema: Any, path: str = "$") -> list[str]:
        if schema is True:
            return []
        if schema is False:
            return [f"{path}: the schema 'false' rejects every value"]
        if not isinstance(schema, dict):
            raise SchemaUnsupported(f"{path}: a schema must be an object or a boolean, got {json_type_name(schema)}")
        unknown = set(schema) - SUPPORTED_KEYWORDS - ANNOTATION_KEYWORDS
        if unknown:
            raise SchemaUnsupported(f"{path}: keyword(s) {sorted(unknown)} are not implemented by this validator")

        errors: list[str] = []
        if "$ref" in schema:
            errors += self.validate(instance, self._resolve(schema["$ref"]), path)
        if "type" in schema:
            names = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
            if not any(type_matches(instance, name) for name in names):
                errors.append(f"{path}: expected type {'/'.join(names)}, got {json_type_name(instance)}")
                return errors
        if "const" in schema and not json_equal(instance, schema["const"]):
            errors.append(f"{path}: must equal {schema['const']!r}, got {instance!r}")
        if "enum" in schema and not any(json_equal(instance, option) for option in schema["enum"]):
            errors.append(f"{path}: {instance!r} is not one of {schema['enum']!r}")
        if isinstance(instance, str):
            if "minLength" in schema and len(instance) < schema["minLength"]:
                errors.append(f"{path}: shorter than minLength {schema['minLength']}")
            if "pattern" in schema and not ecma_pattern_search(schema["pattern"], instance):
                errors.append(f"{path}: {instance!r} does not match pattern {schema['pattern']!r}")
        if isinstance(instance, list):
            if "minItems" in schema and len(instance) < schema["minItems"]:
                errors.append(f"{path}: fewer than minItems {schema['minItems']} item(s)")
            if "items" in schema:
                for index, item in enumerate(instance):
                    errors += self.validate(item, schema["items"], f"{path}[{index}]")
        if isinstance(instance, dict):
            for key in schema.get("required", []):
                if key not in instance:
                    errors.append(f"{path}: missing required key {key!r}")
            properties = schema.get("properties", {})
            for key, subschema in properties.items():
                if key in instance:
                    errors += self.validate(instance[key], subschema, f"{path}.{key}")
            additional = schema.get("additionalProperties", True)
            extra = sorted(key for key in instance if key not in properties)
            if additional is False and extra:
                errors.append(f"{path}: unexpected key(s) {extra}")
            elif isinstance(additional, dict):
                for key in extra:
                    errors += self.validate(instance[key], additional, f"{path}.{key}")
        for subschema in schema.get("allOf", []):
            errors += self.validate(instance, subschema, path)
        if "if" in schema:
            if not self.validate(instance, schema["if"], path):
                if "then" in schema:
                    errors += self.validate(instance, schema["then"], path)
            elif "else" in schema:
                errors += self.validate(instance, schema["else"], path)
        return errors


VALIDATOR = SchemaValidator(CORPUS_ROOT)

# ---------------------------------------------------------------------------
# Corpus contract, read from README.md
# ---------------------------------------------------------------------------


def read_text(path: Path) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def load_json(path: Path) -> Any:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def readme_layout() -> tuple[tuple[str, ...], tuple[str, ...]]:
    """(files, directories) of an entry, from the tree under 'What an entry is' in README.md."""
    text = read_text(README_PATH)
    section = text.split("## What an entry is", 1)[-1].split("\n## ", 1)[0]
    names = re.findall(r"^[├└]── (\S+)", section, flags=re.MULTILINE)
    files = tuple(name for name in names if not name.endswith("/"))
    dirs = tuple(name.rstrip("/") for name in names if name.endswith("/"))
    return files, dirs


def readme_categories() -> tuple[str, ...]:
    """Template names from the table under '## Categories' in README.md."""
    text = read_text(README_PATH)
    section = text.split("## Categories", 1)[-1].split("\n## ", 1)[0]
    rows = re.findall(r"^\|\s*([a-z0-9][a-z0-9-]*)\s*\|", section, flags=re.MULTILINE)
    return tuple(rows)


def list_dirs(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir())


def category_of(entry_id: str, categories: list[str]) -> str | None:
    """The longest template name that prefixes ``entry_id`` followed by '-'."""
    matches = [name for name in categories if entry_id.startswith(name + "-")]
    return max(matches, key=len) if matches else None


def tree_digest(root: Path) -> dict[str, str]:
    """{relative path: sha256} for every file under ``root``."""
    digests: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            digests[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


# ---------------------------------------------------------------------------
# science-gate provenance and runs
# ---------------------------------------------------------------------------


def seg_provenance() -> dict[str, str]:
    """Version, git HEAD and a digest of science-gate's source, all read from files (no git process)."""
    info = {"src": str(SEG_SRC), "version": "unknown", "head": "unknown", "src_sha256": "missing"}
    package = SEG_SRC / "science_gate"
    init = package / "__init__.py"
    if init.is_file():
        match = re.search(r'^__version__\s*=\s*"([^"]+)"', read_text(init), flags=re.MULTILINE)
        if match:
            info["version"] = match.group(1)
    git_dir = SEG_SRC.parent / ".git"
    try:
        head = read_text(git_dir / "HEAD").strip()
        if head.startswith("ref: "):
            ref = head[5:]
            ref_file = git_dir / ref
            if ref_file.is_file():
                info["head"] = f"{read_text(ref_file).strip()[:12]} ({ref})"
            else:
                packed = read_text(git_dir / "packed-refs") if (git_dir / "packed-refs").is_file() else ""
                found = re.search(r"^([0-9a-f]{40}) " + re.escape(ref) + r"$", packed, flags=re.MULTILINE)
                info["head"] = f"{found.group(1)[:12]} ({ref})" if found else f"unresolved ({ref})"
        else:
            info["head"] = head[:12] + " (detached)"
    except OSError:
        pass
    if package.is_dir():
        digest = hashlib.sha256()
        for path in sorted(package.rglob("*.py")):
            digest.update(path.relative_to(package).as_posix().encode("utf-8") + b"\0")
            digest.update(hashlib.sha256(path.read_bytes()).digest())
        info["src_sha256"] = digest.hexdigest()
    return info


def science_gate_env() -> dict[str, str]:
    """The run environment: the caller's, minus any SCIENCE_GATE_* setting (no HMAC key), plus the fixed settings."""
    env = {
        key: value
        for key, value in os.environ.items()
        if not key.upper().startswith("SCIENCE_GATE_") and key.upper() not in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP")
    }
    env["PYTHONPATH"] = str(SEG_SRC)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["SCIENCE_GATE_FIXED_TIME"] = FIXED_TIME
    return env


class CommandError(Exception):
    """An expected_outcome.command that the tests refuse to run."""


def build_arguments(command: str, tmp: Path) -> tuple[str, list[str], Path]:
    """(subcommand, science-gate arguments, output directory) for ``command``.

    ``<tmp>`` in an ``--output`` value becomes the temporary directory. If
    the command gives no ``--output``, ``--output <tmp>/run`` is added. Any
    other placeholder, ``--live``, or an unknown subcommand is refused.
    """
    tokens = shlex.split(command, posix=True)
    if not tokens or tokens[0] not in SUBCOMMAND_OUTPUTS:
        raise CommandError(f"unsupported science-gate subcommand in {command!r}; supported: {sorted(SUBCOMMAND_OUTPUTS)}")
    if "--live" in tokens:
        raise CommandError(f"{command!r} asks for live network lookups; corpus runs are offline")
    arguments: list[str] = []
    output: Path | None = None
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token == "--output":
            if index + 1 >= len(tokens):
                raise CommandError(f"{command!r}: --output has no value")
            value = tokens[index + 1]
            if not value.startswith("<tmp>"):
                raise CommandError(f"{command!r}: --output must be under <tmp>, got {value!r}")
            output = tmp / value[len("<tmp>"):].lstrip("/\\") if value != "<tmp>" else tmp / "out"
            arguments += ["--output", str(output)]
            index += 2
            continue
        if "<" in token or ">" in token:
            raise CommandError(f"{command!r}: unresolved placeholder {token!r}")
        arguments.append(token)
        index += 1
    if output is None:
        output = tmp / "run"
        arguments += ["--output", str(output)]
    return tokens[0], arguments, output


@dataclasses.dataclass
class RunRecord:
    entry_id: str
    command: str
    subcommand: str = ""
    argv: list[str] = dataclasses.field(default_factory=list)
    returncode: int | None = None
    stdout: str = ""
    stderr: str = ""
    doc_name: str = ""
    doc: dict[str, Any] | None = None
    mention_name: str = ""
    mention_text: str | None = None
    problems: list[str] = dataclasses.field(default_factory=list)
    entry_before: dict[str, str] = dataclasses.field(default_factory=dict)
    entry_after: dict[str, str] = dataclasses.field(default_factory=dict)
    seg_src_sha256: str = ""
    seconds: float = 0.0
    error: str | None = None

    def tail(self) -> str:
        out = "\n".join(self.stdout.strip().splitlines()[-5:])
        err = "\n".join(self.stderr.strip().splitlines()[-5:])
        return f"exit {self.returncode}; stdout tail:\n{out or '(empty)'}\nstderr tail:\n{err or '(empty)'}"


RUNS: dict[str, RunRecord] = {}
PROVENANCE: dict[str, dict[str, str]] = {}


def mention_file_name(expected: dict[str, Any], default: str) -> str:
    """The report file that must_mention applies to, from expected-results.json when it names one."""
    declared = expected.get("must_mention_in") or expected.get("must_mention_scope")
    if isinstance(declared, str) and declared.strip():
        name = declared.split()[0]
        if "/" in name or "\\" in name or name in (".", ".."):
            raise CommandError(f"must_mention file {name!r} is not a plain file name")
        return name
    return default


def run_entry(entry_dir: Path, entry: dict[str, Any], expected: dict[str, Any]) -> RunRecord:
    entry_id = entry_dir.name
    if entry_id in RUNS:
        return RUNS[entry_id]
    command = str(entry.get("expected_outcome", {}).get("command", ""))
    record = RunRecord(entry_id=entry_id, command=command)
    RUNS[entry_id] = record
    if not (SEG_SRC / "science_gate" / "cli.py").is_file():
        record.error = (
            f"science-gate source not found at {SEG_SRC}; set SCIENCE_GATE_SRC to its src directory. "
            "A missing tool is a failure, never a pass."
        )
        return record
    tmp = Path(tempfile.mkdtemp(prefix="corpus-run-"))
    try:
        try:
            subcommand, arguments, output = build_arguments(command, tmp)
            doc_name, report_name = SUBCOMMAND_OUTPUTS[subcommand]
            record.mention_name = mention_file_name(expected, report_name)
        except (CommandError, ValueError) as exc:
            record.error = f"cannot run expected_outcome.command: {exc}"
            return record
        record.subcommand, record.doc_name = subcommand, doc_name
        record.argv = [PYTHON, "-m", "science_gate.cli", *arguments]
        record.entry_before = tree_digest(entry_dir)
        record.seg_src_sha256 = seg_provenance()["src_sha256"]
        started = time.monotonic()
        try:
            completed = subprocess.run(
                record.argv,
                cwd=str(entry_dir),
                env=science_gate_env(),
                stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=RUN_TIMEOUT_SECONDS,
                shell=False,
                check=False,
            )
        except subprocess.TimeoutExpired:
            record.error = f"science-gate did not finish within {RUN_TIMEOUT_SECONDS} s"
            return record
        except OSError as exc:
            record.error = f"science-gate could not be started: {exc}"
            return record
        finally:
            record.seconds = time.monotonic() - started
        encoding = locale.getpreferredencoding(False) or "utf-8"
        record.returncode = completed.returncode
        record.stdout = completed.stdout.decode(encoding, errors="replace")
        record.stderr = completed.stderr.decode(encoding, errors="replace")
        record.entry_after = tree_digest(entry_dir)
        doc_path = output / doc_name
        try:
            document = load_json(doc_path)
        except (OSError, ValueError) as exc:
            record.problems.append(f"{doc_name} could not be read: {exc}")
        else:
            if isinstance(document, dict):
                record.doc = document
            else:
                record.problems.append(f"{doc_name} is not a JSON object")
        try:
            record.mention_text = read_text(output / record.mention_name)
        except (OSError, ValueError) as exc:
            record.problems.append(f"{record.mention_name} could not be read: {exc}")
        return record
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------------------
# Corpus-level tests
# ---------------------------------------------------------------------------

LAYOUT_FILES, LAYOUT_DIRS = readme_layout()
CATEGORIES = readme_categories()


def layout_problems(directory: Path, extra_files: tuple[str, ...] = ()) -> list[str]:
    problems = []
    for name in LAYOUT_FILES + extra_files:
        if not (directory / name).is_file():
            problems.append(f"missing file {name}")
    for name in LAYOUT_DIRS:
        path = directory / name
        if not path.is_dir():
            problems.append(f"missing directory {name}/")
        elif not any(child.is_file() for child in path.rglob("*")):
            problems.append(f"directory {name}/ holds no file (git would not keep it)")
    return problems


class SchemaValidatorSelfTest(unittest.TestCase):
    """The validator must reject what the schemas forbid. A validator that accepts everything would pass every entry."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_json(INTAKE_SCHEMA_PATH)
        entries = list_dirs(ENTRIES_DIR)
        cls.sample = load_json(entries[0] / "entry.json") if entries else None

    def good(self) -> dict[str, Any]:
        if self.sample is None:
            self.fail("no entry to use as a valid sample")
        return json.loads(json.dumps(self.sample))

    def assertRejected(self, instance: Any, fragment: str) -> None:
        errors = VALIDATOR.validate(instance, self.schema)
        self.assertTrue(errors, f"validator accepted an invalid record ({fragment})")
        self.assertTrue(any(fragment in error for error in errors), f"no error mentions {fragment!r}: {errors}")

    def test_sample_entry_is_accepted(self) -> None:
        self.assertEqual(VALIDATOR.validate(self.good(), self.schema), [])

    def test_rejects_missing_required_key(self) -> None:
        record = self.good()
        del record["falsified_by"]
        self.assertRejected(record, "falsified_by")

    def test_rejects_unexpected_key(self) -> None:
        record = self.good()
        record["benchmark_score"] = 1
        self.assertRejected(record, "benchmark_score")

    def test_rejects_bad_entry_id(self) -> None:
        for bad in ("Bad_ID", "ab", "abc-def\n", "-abc"):
            record = self.good()
            record["entry_id"] = bad
            self.assertRejected(record, "entry_id")

    def test_rejects_boolean_exit_code_and_unknown_status(self) -> None:
        record = self.good()
        record["expected_outcome"]["exit_code"] = True
        self.assertRejected(record, "exit_code")
        record = self.good()
        record["expected_outcome"]["exit_code"] = 4
        self.assertRejected(record, "exit_code")
        record = self.good()
        record["expected_outcome"]["status"] = "MOSTLY_PASS"
        self.assertRejected(record, "status")

    def test_rejects_unknown_failure_mode_and_empty_does_not_prove(self) -> None:
        record = self.good()
        record["failure_mode"] = "LOOKS_FINE"
        self.assertRejected(record, "failure_mode")
        record = self.good()
        record["does_not_prove"] = []
        self.assertRejected(record, "does_not_prove")

    def test_rejects_training_without_grant(self) -> None:
        record = self.good()
        record["permissions"]["evidence_of_grant"] = "NOASSERTION"
        record["permissions"]["training_allowed"] = True
        self.assertRejected(record, "training_allowed")

    def test_rejects_redistribution_of_controlled_data(self) -> None:
        record = self.good()
        record["permissions"].update(
            access_class="CONTROLLED_LOCAL", evidence_of_grant="agreement ref 1", redistribution_allowed=True
        )
        self.assertRejected(record, "redistribution_allowed")

    def test_rejects_string_boolean_and_extra_permission_key(self) -> None:
        record = self.good()
        record["synthetic"] = "true"
        self.assertRejected(record, "synthetic")
        record = self.good()
        record["permissions"]["inferred_from_reachability"] = True
        self.assertRejected(record, "inferred_from_reachability")

    def test_unknown_keyword_raises(self) -> None:
        with self.assertRaises(SchemaUnsupported):
            VALIDATOR.validate({}, {"type": "object", "minProperties": 1})


class CorpusLayoutTests(unittest.TestCase):
    def test_readme_declares_layout_and_categories(self) -> None:
        self.assertIn("entry.json", LAYOUT_FILES)
        self.assertIn("expected-results.json", LAYOUT_FILES)
        self.assertIn("fixtures", LAYOUT_DIRS)
        self.assertTrue(CATEGORIES, "README.md '## Categories' table lists no template")

    def test_entries_exist(self) -> None:
        self.assertTrue(list_dirs(ENTRIES_DIR), "entries/ holds no entry")

    def test_templates_match_readme_categories(self) -> None:
        on_disk = sorted(path.name for path in list_dirs(TEMPLATES_DIR))
        self.assertEqual(on_disk, sorted(CATEGORIES))

    def test_every_template_has_the_full_layout(self) -> None:
        templates = list_dirs(TEMPLATES_DIR)
        self.assertTrue(templates, "templates/ holds no template")
        for template in templates:
            with self.subTest(template=template.name):
                problems = layout_problems(template, extra_files=("README.md",))
                for name in ("entry.json", "expected-results.json", "manifest.json"):
                    try:
                        load_json(template / name)
                    except (OSError, ValueError) as exc:
                        problems.append(f"{name} is not valid JSON: {exc}")
                self.assertEqual(problems, [], f"templates/{template.name}")

    def test_documented_gap_table_matches_known_failures(self) -> None:
        for gap in DOCUMENTED_GAPS:
            with self.subTest(entry=gap.entry_id, aspect=gap.aspect):
                path = ENTRIES_DIR / gap.entry_id / "entry.json"
                self.assertTrue(path.is_file(), f"{path} is missing")
                known = load_json(path).get("known_failures", [])
                self.assertTrue(
                    any(gap.anchor in text for text in known),
                    f"{gap.entry_id} known_failures no longer documents {gap.aspect!r}; "
                    "the assertion now runs as an ordinary test",
                )


# ---------------------------------------------------------------------------
# Publication hygiene (static checks over every corpus file; no science-gate run)
# ---------------------------------------------------------------------------

JUNK_DIR_NAMES = frozenset({"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "science-gate-runs"})
JUNK_FILE_NAMES = frozenset({".DS_Store", "Thumbs.db", "desktop.ini"})
JUNK_SUFFIXES = (".pyc", ".pyo", ".tmp", ".bak", ".swp", ".orig", ".rej", "~")
#: Home-directory paths. Written with character classes so that this file does not match itself.
LOCAL_PATH_RE = re.compile(
    r"(?i)(?:\b[a-z]:[\\/]+(?:users|documents and settings)[\\/]"
    r"|[/]c[/]users[/]|[/]home[/][a-z_][\w.-]*[/]|[/]Users[/][a-z][\w.-]*[/]|\bAppData[\\/])"
)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
DOI_RE = re.compile(r"\b10\.\d{4,9}/")
TEST_DOI_PREFIX = "10.5555/"
#: Template placeholder markers. The templates use several conventions: REPLACE, an upper-case <...>
#: token, <e.g. ...>, a "(placeholder)" or "(template: ...)" heading, and an "-synthetic-NN" id.
PLACEHOLDER_RE = re.compile(r"\bREPLACE\b|<[A-Z][A-Z_ ,.'-]{3,}|<e\.g\.|\((?:placeholder|template)\b|-synthetic-NN\b")
LICENSE_FILE_RE = re.compile(r"(?i)^(licen[cs]e|copying|notice)(\.|$)")
#: User names too generic to search for as words.
GENERIC_USER_NAMES = frozenset(
    {"user", "users", "test", "tests", "runner", "admin", "administrator", "root", "ubuntu", "vscode",
     "codespace", "codespaces", "ci", "build", "builder", "docker", "app", "jovyan", "node", "default", "guest"}
)
LOCK_VERSION_RE = re.compile(
    r'(?im)^science_gate[._](?:cli_)?version\s*=\s*"?(?:science-gate\s+)?(\d+\.\d+\.\d+)\b'
)
LOCK_COMMIT_RE = re.compile(r'(?im)^(?:seg|science_gate)[._]git_commit\s*=\s*"?([0-9a-f]{40})\b')


def corpus_files() -> list[tuple[str, bytes]]:
    """(corpus-relative POSIX path, bytes) for every file outside ``.git``."""
    found = []
    for path in sorted(CORPUS_ROOT.rglob("*")):
        rel = path.relative_to(CORPUS_ROOT)
        if rel.parts and rel.parts[0] == ".git":
            continue
        if path.is_file():
            found.append((rel.as_posix(), path.read_bytes()))
    return found


def local_identity_patterns() -> list[tuple[str, re.Pattern[str]]]:
    """This machine's home directory and user name, which must never appear in a corpus file."""
    patterns: list[tuple[str, re.Pattern[str]]] = []
    try:
        home = str(Path.home())
    except (RuntimeError, KeyError, OSError):
        home = ""
    if len(home) > 3:
        for form in sorted({home, home.replace("\\", "/"), home.replace("\\", "\\\\")}):
            patterns.append(("the local home directory", re.compile(re.escape(form), re.IGNORECASE)))
    try:
        user = getpass.getuser()
    except Exception:  # noqa: BLE001 (getuser raises different errors on different platforms)
        user = ""
    if len(user) >= 3 and user.lower() not in GENERIC_USER_NAMES:
        word = r"(?<![A-Za-z0-9])" + re.escape(user) + r"(?![A-Za-z0-9])"
        patterns.append(("the local user name", re.compile(word, re.IGNORECASE)))
    return patterns


def lock_commit(path: Path) -> str | None:
    match = LOCK_COMMIT_RE.search(read_text(path)) if path.is_file() else None
    return match.group(1) if match else None


class CorpusHygieneTests(unittest.TestCase):
    """The publication rules: nothing local, personal or accidental ships with the corpus."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.files = corpus_files()
        cls.texts = [(rel, data.decode("utf-8", errors="replace")) for rel, data in cls.files]

    def test_no_build_junk(self) -> None:
        junk = []
        for path in CORPUS_ROOT.rglob("*"):
            rel = path.relative_to(CORPUS_ROOT)
            if rel.parts and rel.parts[0] == ".git":
                continue
            name = path.name
            if (path.is_dir() and (name in JUNK_DIR_NAMES or name.startswith("corpus-run-"))) or (
                path.is_file() and (name in JUNK_FILE_NAMES or name.endswith(JUNK_SUFFIXES))
            ):
                junk.append(rel.as_posix())
        self.assertEqual(sorted(junk), [], "build junk or temporary output in the corpus")

    def test_no_local_path_user_name_or_email(self) -> None:
        patterns = [("a home-directory path", LOCAL_PATH_RE), ("an email address", EMAIL_RE)]
        patterns += local_identity_patterns()
        hits = []
        for rel, text in self.texts:
            for what, pattern in patterns:
                match = pattern.search(text)
                if match:
                    line = text.count("\n", 0, match.start()) + 1
                    hits.append(f"{rel}:{line}: {what}")  # the matched text is not echoed
        self.assertEqual(hits, [], "local or personal data in corpus files")

    def test_text_files_use_lf_line_endings(self) -> None:
        with_cr = [rel for rel, data in self.files if b"\r" in data]
        self.assertEqual(with_cr, [], "files with CR line endings (write LF)")

    def test_dois_use_the_test_prefix_only(self) -> None:
        other = []
        for rel, text in self.texts:
            for match in DOI_RE.finditer(text):
                if not text.startswith(TEST_DOI_PREFIX, match.start()):
                    other.append(f"{rel}: {text[match.start():match.start() + 24]!r}")
        self.assertEqual(other, [], f"DOIs outside the {TEST_DOI_PREFIX} test prefix")

    def test_never_called_a_benchmark(self) -> None:
        affirmative = []
        for rel, text in self.texts:
            if rel == "tests/test_corpus.py":
                continue  # code: it names 'benchmark_score' to test that the schema rejects it
            for number, line in enumerate(text.splitlines(), 1):
                if re.search(r"(?i)benchmark", line) and not re.search(r"(?i)\b(not|never)\b", line):
                    affirmative.append(f"{rel}:{number}")
        self.assertEqual(affirmative, [], "a line calls the corpus a benchmark without negating it")

    def test_no_license_is_chosen(self) -> None:
        license_files = [rel for rel, _ in self.files if LICENSE_FILE_RE.match(rel.rsplit("/", 1)[-1])]
        self.assertEqual(license_files, [], "a license file exists, but no license has been chosen")
        for entry_dir in list_dirs(ENTRIES_DIR):
            with self.subTest(entry=entry_dir.name):
                licenses = [item.get("license") for item in load_json(entry_dir / "entry.json").get("source_licenses", [])]
                self.assertTrue(licenses, "source_licenses is empty")
                self.assertEqual(sorted(set(licenses)), ["NOASSERTION"])

    def test_entries_hold_no_template_placeholder(self) -> None:
        left = []
        for rel, text in self.texts:
            if rel.startswith("entries/"):
                match = PLACEHOLDER_RE.search(text)
                if match:
                    left.append(f"{rel}: {match.group(0)!r}")
        self.assertEqual(left, [], "template placeholders left in an entry")

    def test_receipts_are_unsigned_and_not_called_proof(self) -> None:
        for entry_dir in list_dirs(ENTRIES_DIR):
            with self.subTest(entry=entry_dir.name):
                receipt = load_json(entry_dir / "receipts" / "receipt.json")
                self.assertEqual(receipt.get("signature_state"), "UNSIGNED")
                self.assertIsNone(receipt.get("signature"))
                boundary = receipt.get("body", {}).get("evidence_boundary", {})
                self.assertEqual(boundary.get("scientific_validity"), "NOT ESTABLISHED")
                readme = read_text(entry_dir / "receipts" / "README.md")
                self.assertIn("UNSIGNED", readme)
                self.assertRegex(
                    readme, r"(?i)does\s+not\s+establish\s+scientific",
                    "receipts/README.md must say what a receipt does not establish",
                )

    def test_environment_lock_names_version_and_an_existing_commit(self) -> None:
        repo = SEG_SRC.parent
        git = shutil.which("git")
        for entry_dir in list_dirs(ENTRIES_DIR):
            with self.subTest(entry=entry_dir.name):
                lock = entry_dir / "environment.lock"
                text = read_text(lock)
                self.assertRegex(text, LOCK_VERSION_RE, "environment.lock does not record the science-gate version")
                commit = lock_commit(lock)
                self.assertIsNotNone(commit, "environment.lock does not record a 40-hex science-gate git commit")
                if git is None or not (repo / ".git").exists():
                    self.fail(f"cannot confirm commit {commit}: no git executable or no git repository at {repo}")
                env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
                completed = subprocess.run(
                    [git, "--no-optional-locks", "-C", str(repo), "cat-file", "-t", str(commit)],
                    capture_output=True, text=True, timeout=60, env=env, stdin=subprocess.DEVNULL, check=False,
                )
                self.assertEqual(completed.stdout.strip(), "commit", f"{commit} is not a commit in {repo}")


# ---------------------------------------------------------------------------
# Per-entry tests, generated for every directory in entries/
# ---------------------------------------------------------------------------

#: (entry_id, aspect, test name, known_failures index, text) for each applied expectedFailure.
APPLIED_GAPS: list[tuple[str, str, str, int, str]] = []


def slug(text: str, limit: int = 40) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return (cleaned[:limit].rstrip("_")) or "blank"


def normalize_command(value: Any) -> str:
    """The subcommand named by an expected-results.json ``command`` (a string or an object)."""
    if isinstance(value, dict):
        return str(value.get("subcommand", ""))
    if isinstance(value, str) and value.strip():
        return shlex.split(value)[0]
    return ""


class EntryCase:
    """Checks shared by the generated per-entry classes.

    This is a mixin, not a TestCase, so that the loader never collects it
    on its own. Each generated class is ``(EntryCase, unittest.TestCase)``.
    """

    entry_dir: Path
    entry: dict[str, Any]
    expected: dict[str, Any]

    @property
    def outcome(self) -> dict[str, Any]:
        return self.entry.get("expected_outcome", {})

    def run_record(self) -> RunRecord:
        record = run_entry(self.entry_dir, self.entry, self.expected)
        if record.error:
            self.fail(f"{self.entry_dir.name}: {record.error}")
        return record

    def document(self) -> dict[str, Any]:
        record = self.run_record()
        if record.doc is None:
            self.fail(f"{self.entry_dir.name}: {'; '.join(record.problems) or 'no run document'}\n{record.tail()}")
        return record.doc

    def report_text(self) -> str:
        record = self.run_record()
        if record.mention_text is None:
            self.fail(f"{self.entry_dir.name}: {'; '.join(record.problems) or 'no report'}\n{record.tail()}")
        return record.mention_text

    def actual_failure_modes(self) -> list[str]:
        doc = self.document()
        record = self.run_record()
        if "failure_modes" not in doc:
            if record.subcommand == "mutate":
                return []  # a mutation report has no top-level failure_modes field
            self.fail(f"{record.doc_name} has no failure_modes field")
        return sorted(doc["failure_modes"])

    # -- static checks ------------------------------------------------------

    def test_01_entry_json_matches_intake_and_permissions_schemas(self) -> None:
        errors = VALIDATOR.validate(self.entry, load_json(INTAKE_SCHEMA_PATH))
        self.assertEqual(errors, [], "entry.json does not match intake-schema.json / permissions-schema.json")

    def test_02_entry_id_matches_directory(self) -> None:
        self.assertEqual(self.entry.get("entry_id"), self.entry_dir.name)
        self.assertEqual(self.expected.get("entry_id"), self.entry_dir.name, "expected-results.json entry_id")

    def test_03_synthetic_entry_is_labeled_synthetic(self) -> None:
        synthetic = self.entry.get("synthetic")
        access = self.entry.get("permissions", {}).get("access_class")
        self.assertIsInstance(synthetic, bool, "entry.json synthetic must be an explicit boolean")
        if access == "SYNTHETIC":
            self.assertIs(synthetic, True, "access_class SYNTHETIC but synthetic is not true")
        if not synthetic:
            return
        self.assertEqual(access, "SYNTHETIC", "a synthetic entry must have access_class SYNTHETIC")
        label = f"{self.entry.get('entry_id', '')} {self.entry.get('title', '')}".lower()
        self.assertIn("synthetic", label, "entry.json entry_id or title must say synthetic")
        for name in ("claim.md", "limitations.md"):
            self.assertIn("SYNTHETIC", read_text(self.entry_dir / name), f"{name} carries no SYNTHETIC label")
        if "synthetic" in self.expected:
            self.assertIs(self.expected["synthetic"], True, "expected-results.json synthetic disagrees")

    def test_04_training_permission_is_not_implied(self) -> None:
        permissions = self.entry.get("permissions", {})
        training = permissions.get("training_allowed")
        self.assertIsInstance(training, bool, "training_allowed must be an explicit boolean, never inferred")
        grant = permissions.get("evidence_of_grant")
        no_grant = not isinstance(grant, str) or not grant.strip() or grant.strip() == "NOASSERTION"
        # Conservative reading: a grant string that itself says NOASSERTION is not evidence of a grant.
        no_grant = no_grant or bool(re.search(r"\bNOASSERTION\b", grant or ""))
        if no_grant:
            self.assertIs(training, False, f"training_allowed is true without a grant (evidence_of_grant={grant!r})")

    def test_05_permission_rules_by_hand(self) -> None:
        permissions = self.entry.get("permissions", {})
        flags = (
            "evaluation_allowed", "training_allowed", "redistribution_allowed",
            "derivatives_allowed", "public_display_allowed", "commercial_use_allowed",
        )
        for flag in flags:
            self.assertIsInstance(permissions.get(flag), bool, f"{flag} must be an explicit boolean")
        if permissions.get("evidence_of_grant") == "NOASSERTION":
            for flag in flags[1:]:
                self.assertIs(permissions.get(flag), False, f"{flag} must be false when evidence_of_grant is NOASSERTION")
        if permissions.get("access_class") in ("CONTROLLED_LOCAL", "REFERENCE_ONLY"):
            self.assertIs(permissions.get("redistribution_allowed"), False, "controlled or reference-only data")

    def test_06_entry_has_the_declared_layout(self) -> None:
        self.assertEqual(layout_problems(self.entry_dir), [])

    def test_07_says_what_passing_does_not_prove(self) -> None:
        statements = self.entry.get("does_not_prove")
        self.assertTrue(isinstance(statements, list) and statements and all(isinstance(s, str) and s.strip() for s in statements))
        for name in ("claim.md", "limitations.md"):
            self.assertRegex(read_text(self.entry_dir / name), r"(?i)not prove", f"{name} does not say what passing does not prove")
        self.assertTrue(self.expected.get("does_not_prove"), "expected-results.json has no does_not_prove")

    def test_08_expected_results_agree_with_entry_json(self) -> None:
        self.assertEqual(self.expected.get("schema"), EXPECTED_RESULTS_SCHEMA)
        for key in ("status", "exit_code", "reason", "failure_modes", "must_mention"):
            with self.subTest(field=key):
                self.assertTrue(
                    json_equal(self.expected.get(key), self.outcome.get(key)),
                    f"{key}: expected-results.json {self.expected.get(key)!r} != entry.json {self.outcome.get(key)!r}",
                )
        self.assertEqual(normalize_command(self.expected.get("command")), normalize_command(self.outcome.get("command")))

    def test_09_category_has_a_template(self) -> None:
        category = category_of(self.entry_dir.name, list(CATEGORIES))
        self.assertIsNotNone(category, f"{self.entry_dir.name} names no category from README.md")
        self.assertTrue((TEMPLATES_DIR / str(category)).is_dir(), f"templates/{category} is missing")

    # -- run checks (each entry runs science-gate once) ---------------------

    def test_20_status(self) -> None:
        self.assertEqual(self.document().get("status"), self.outcome.get("status"))

    def test_21_exit_code(self) -> None:
        record = self.run_record()
        self.assertEqual(record.returncode, self.outcome.get("exit_code"), f"process exit code\n{record.tail()}")
        self.assertEqual(self.document().get("exit_code"), self.outcome.get("exit_code"), f"{record.doc_name} exit_code")

    def test_22_reason(self) -> None:
        self.assertEqual(self.document().get("reason"), self.outcome.get("reason"))

    def test_23_failure_modes(self) -> None:
        self.assertEqual(self.actual_failure_modes(), sorted(self.outcome.get("failure_modes", [])))

    def test_29_run_leaves_the_entry_unchanged(self) -> None:
        record = self.run_record()
        before, after = record.entry_before, record.entry_after
        changed = sorted(p for p in before.keys() & after.keys() if before[p] != after[p])
        self.assertEqual(
            (sorted(after.keys() - before.keys()), sorted(before.keys() - after.keys()), changed),
            ([], [], []),
            "science-gate added, removed or changed files inside the entry (added, removed, changed)",
        )


def _test_must_mention(text: str) -> Callable[[EntryCase], None]:
    def test(self: EntryCase) -> None:
        if text not in self.report_text():
            self.fail(f"{self.run_record().mention_name} does not contain the must_mention string {text!r}")
    return test


def _test_must_not_mention(texts: list[str]) -> Callable[[EntryCase], None]:
    def test(self: EntryCase) -> None:
        present = [text for text in texts if text in self.report_text()]
        self.assertEqual(present, [], f"{self.run_record().mention_name} contains must_not_mention string(s)")
    return test


def _test_reasons_include(reasons: list[str]) -> Callable[[EntryCase], None]:
    def test(self: EntryCase) -> None:
        actual = self.document().get("reasons", [])
        self.assertEqual(sorted(set(reasons) - set(actual)), [], f"reasons {actual!r} lack an expected reason")
    return test


def _test_never_a_false_pass(forbidden: list[str]) -> Callable[[EntryCase], None]:
    """Generated only when the intended status is not PASS, so it always has something to assert."""

    def test(self: EntryCase) -> None:
        record = self.run_record()
        doc = self.document()  # no run document means PASS cannot be ruled out: a failure, not a pass
        self.assertNotEqual(doc.get("status"), "PASS", "science-gate reported PASS where the intended status is not PASS")
        self.assertNotEqual(record.returncode, 0, "science-gate exited 0 where the intended status is not PASS")
        for status in forbidden:
            self.assertNotEqual(doc.get("status"), status, "status_must_not_be")
    return test


def _test_headline_prefix(prefix: str) -> Callable[[EntryCase], None]:
    def test(self: EntryCase) -> None:
        lines = [line for line in self.run_record().stdout.splitlines() if line.strip()]
        self.assertTrue(lines and lines[0].startswith(prefix), f"stdout headline {lines[:1]!r} does not start with {prefix!r}")
    return test


def _test_gap_is_documented(aspect: str, documented: Any) -> Callable[[EntryCase], None]:
    """Companion of an expectedFailure: the run shows the intended value or the documented divergence, nothing else."""

    def test(self: EntryCase) -> None:
        if aspect == "failure_modes":
            actual: Any = self.actual_failure_modes()
            allowed = [sorted(self.outcome.get("failure_modes", [])), sorted(documented)]
        else:
            actual = self.document().get(aspect)
            allowed = [self.outcome.get(aspect), documented]
        self.assertIn(actual, allowed, f"{aspect} diverges in a way entry.json known_failures does not describe")
    return test


def _mark_documented(entry_id: str, aspect: str, test_name: str, function: Callable, known: list[str]) -> Callable:
    """``function`` marked expectedFailure when this entry's known_failures documents the gap, else unchanged.

    ``unittest.expectedFailure`` sets a flag on the function object it is
    given. The flag goes on a fresh wrapper, so that a method shared by every
    entry class is never marked for all of them.
    """
    for gap in DOCUMENTED_GAPS:
        if gap.entry_id == entry_id and gap.aspect == aspect:
            for index, text in enumerate(known):
                if gap.anchor in text:
                    APPLIED_GAPS.append((entry_id, aspect, test_name, index, text))

                    def wrapper(self: Any, _function: Callable = function) -> None:
                        _function(self)

                    wrapper.__name__ = wrapper.__qualname__ = test_name
                    wrapper.__doc__ = function.__doc__
                    return unittest.expectedFailure(wrapper)
    return function


def _unloadable_case(entry_dir: Path, message: str) -> type[unittest.TestCase]:
    def test_00_entry_files_load(self: unittest.TestCase) -> None:
        self.fail(message)
    return type(f"Entry_{slug(entry_dir.name, 60)}", (unittest.TestCase,), {"test_00_entry_files_load": test_00_entry_files_load})


def make_entry_case(entry_dir: Path) -> type[unittest.TestCase]:
    try:
        entry = load_json(entry_dir / "entry.json")
        expected = load_json(entry_dir / "expected-results.json")
        if not isinstance(entry, dict) or not isinstance(expected, dict):
            raise ValueError("entry.json and expected-results.json must hold JSON objects")
    except (OSError, ValueError) as exc:
        return _unloadable_case(entry_dir, f"{entry_dir.name}: cannot load entry files: {exc}")

    entry_id = entry_dir.name
    known = [text for text in entry.get("known_failures", []) if isinstance(text, str)]
    outcome = entry.get("expected_outcome", {}) if isinstance(entry.get("expected_outcome"), dict) else {}
    attrs: dict[str, Any] = {"entry_dir": entry_dir, "entry": entry, "expected": expected}

    for name, aspect in (("test_20_status", "status"), ("test_21_exit_code", "exit_code"),
                         ("test_22_reason", "reason"), ("test_23_failure_modes", "failure_modes")):
        function = getattr(EntryCase, name)
        marked = _mark_documented(entry_id, aspect, name, function, known)
        if marked is not function:
            attrs[name] = marked
            gap = next(g for g in DOCUMENTED_GAPS if g.entry_id == entry_id and g.aspect == aspect)
            attrs[f"{name}_divergence_is_the_documented_one"] = _test_gap_is_documented(aspect, gap.documented_actual)

    for index, text in enumerate(outcome.get("must_mention", []) or []):
        name = f"test_24_must_mention_{index + 1:02d}_{slug(text)}"
        attrs[name] = _mark_documented(entry_id, f"must_mention:{text}", name, _test_must_mention(text), known)
    if expected.get("must_not_mention"):
        attrs["test_25_must_not_mention"] = _test_must_not_mention(list(expected["must_not_mention"]))
    if expected.get("reasons_include"):
        attrs["test_26_reasons_include"] = _test_reasons_include(list(expected["reasons_include"]))
    if outcome.get("status") != "PASS":
        attrs["test_27_never_a_false_pass"] = _test_never_a_false_pass(list(expected.get("status_must_not_be", [])))
    if isinstance(expected.get("headline_prefix"), str):
        attrs["test_28_headline_prefix"] = _test_headline_prefix(expected["headline_prefix"])

    return type(f"Entry_{slug(entry_id, 60)}", (EntryCase, unittest.TestCase), attrs)


def _register_entry_cases() -> None:
    for entry_dir in list_dirs(ENTRIES_DIR):
        case = make_entry_case(entry_dir)
        globals()[case.__name__] = case


_register_entry_cases()


# ---------------------------------------------------------------------------
# Module setup and the printed summary
# ---------------------------------------------------------------------------


def setUpModule() -> None:  # noqa: N802 (unittest hook name)
    PROVENANCE["start"] = seg_provenance()


def _format_list(values: Any) -> str:
    return "[" + ", ".join(str(v) for v in values) + "]" if isinstance(values, list) else str(values)


def tearDownModule() -> None:  # noqa: N802 (unittest hook name)
    out = sys.stderr
    start = PROVENANCE.get("start", {})
    end = seg_provenance()
    write = lambda text="": out.write(text + "\n")  # noqa: E731
    write()
    write("=" * 78)
    write("CONFORMANCE CORPUS SUMMARY (fixture collection; not a benchmark)")
    write("=" * 78)
    write(f"science-gate {start.get('version')} at {start.get('src')}")
    write(f"  git HEAD {start.get('head')}; src/science_gate/*.py sha256 {start.get('src_sha256', '')[:16]}... at start")
    if end.get("src_sha256") != start.get("src_sha256"):
        write(f"  WARNING: science-gate source changed during this test session (now {end.get('src_sha256', '')[:16]}...);")
        write("  results may mix versions and are not attributable to one source tree.")
    run_digests = {record.seg_src_sha256 for record in RUNS.values() if record.seg_src_sha256}
    if len(run_digests) > 1:
        write(f"  WARNING: runs saw {len(run_digests)} different science-gate source digests.")
    write(f"  interpreter {PYTHON}; SCIENCE_GATE_FIXED_TIME={FIXED_TIME}; --output in an OS temp dir; offline")
    lock_commits = sorted({c for c in (lock_commit(d / "environment.lock") for d in list_dirs(ENTRIES_DIR)) if c})
    write(f"  entries' environment.lock commit(s): {', '.join(c[:12] for c in lock_commits) or 'none recorded'}")
    write("  (the locks and evaluation/ records describe the run they record, not necessarily the source above)")
    write()
    if not RUNS:
        write("No science-gate run happened in this session.")
    reproduced = 0
    for entry_id in sorted(RUNS):
        record = RUNS[entry_id]
        entry_dir = ENTRIES_DIR / entry_id
        try:
            outcome = load_json(entry_dir / "entry.json")["expected_outcome"]
        except (OSError, ValueError, KeyError):
            write(f"{entry_id}: entry.json unreadable")
            continue
        if record.error:
            write(f"{entry_id}: NOT RUN: {record.error}")
            continue
        doc = record.doc or {}
        actual_modes = sorted(doc.get("failure_modes", [])) if ("failure_modes" in doc or record.subcommand != "mutate") else []
        text = record.mention_text or ""
        missing = [m for m in outcome.get("must_mention", []) if m not in text]
        diffs = []
        if doc.get("status") != outcome.get("status"):
            diffs.append(f"status {outcome.get('status')} -> {doc.get('status')}")
        if record.returncode != outcome.get("exit_code") or doc.get("exit_code") != outcome.get("exit_code"):
            diffs.append(f"exit {outcome.get('exit_code')} -> process {record.returncode}, document {doc.get('exit_code')}")
        if doc.get("reason") != outcome.get("reason"):
            diffs.append(f"reason {outcome.get('reason')} -> {doc.get('reason')}")
        if actual_modes != sorted(outcome.get("failure_modes", [])):
            diffs.append(f"failure_modes {_format_list(sorted(outcome.get('failure_modes', [])))} -> {_format_list(actual_modes)}")
        if missing:
            diffs.append(f"must_mention missing {missing}")
        if record.problems:
            diffs.append("; ".join(record.problems))
        verdict = "REPRODUCES" if not diffs else "DIVERGES"
        reproduced += not diffs
        write(
            f"{entry_id:<42} {record.subcommand:<6} expected {outcome.get('status')}/{outcome.get('exit_code')}/"
            f"{outcome.get('reason')}  actual {doc.get('status')}/{record.returncode}/{doc.get('reason')}  "
            f"[{verdict}] {record.seconds:.1f}s"
        )
        for diff in diffs:
            write(f"    - {diff}")
    if RUNS:
        write()
        write(f"{reproduced} of {len(RUNS)} run entries reproduce every asserted field of their intended outcome.")
    write()
    write("Documented tool gaps marked unittest.expectedFailure (each still asserts the INTENDED outcome):")
    if not APPLIED_GAPS:
        write("  (none applied)")
    for entry_id, aspect, test_name, index, text in APPLIED_GAPS:
        write(f"  - {entry_id} / {aspect} ({test_name})")
        write(f"    why: entries/{entry_id}/entry.json known_failures[{index}]:")
        for line in textwrap.wrap(text, width=72):
            write(f"      {line}")
    unapplied = [g for g in DOCUMENTED_GAPS if not any(g.entry_id == a[0] and g.aspect == a[1] for a in APPLIED_GAPS)]
    for gap in unapplied:
        write(f"  - NOT APPLIED {gap.entry_id} / {gap.aspect}: anchor not found in known_failures; asserted normally")
    write()
    write("What passing does not prove: conformance on these declared synthetic fixtures only. It does")
    write("not show that science-gate catches failures outside the corpus, that any scientific conclusion")
    write("is true, or that science-gate is fit for any particular use.")
    write("=" * 78)
    out.flush()


if __name__ == "__main__":
    unittest.main(verbosity=2)
