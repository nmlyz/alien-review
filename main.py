#!/usr/bin/env python3
"""alien-review: write one alien tourist's review of Earth to /output/entry.txt.

The review is a single line left by an alien tourist after a two-day
visit: the locals live in boxes, travel in boxes, and are buried in
boxes, and the reviewer rates the boxes. The punch lands on the last
clause, so the line is built in two beats -- the observation, then the
verdict -- and checked before it is written.

Standard library only, no network. Deterministic: the same bytes on
every run.
"""

import hashlib
import os
import sys

# The two beats of the review. Each beat is one sentence; joined with a
# single space they form the entry line exactly as the reviewer left it.
OBSERVATION = (
    "Visited Earth. The locals live in boxes, travel in boxes, "
    "and are buried in boxes."
)
VERDICT = "Four stars; the boxes are well made."

# The entry the brief asks for: one line, two beats, no trailing
# newline in the file.
MIN_LEN = 1
MAX_LEN = 200
EXPECTED_LENGTH = 119
EXPECTED_BOXES = 4
EXPECTED_SHA256 = "32dc0548610adb413db247bd91a634c5cd1e4c5a2eb77c8bd66d06a3b79f5fdf"


def build_line() -> str:
    """Join the two beats into the entry line."""
    return OBSERVATION + " " + VERDICT


def fingerprint(text: str) -> str:
    """SHA-256 of the entry text, for the byte-exactness check."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_beats() -> list:
    """Each beat must be whole sentences ending in a period.

    The observation is two sentences (the arrival, then what the locals
    do); the verdict is one. The counts are part of the line's shape.
    """
    found = []
    expected = (("observation", OBSERVATION, 2), ("verdict", VERDICT, 1))
    for name, beat, sentences in expected:
        if beat != beat.strip():
            found.append(f"{name} beat must not start or end with white space")
        if not beat.endswith("."):
            found.append(f"{name} beat must end with a period")
        if beat.count(".") != sentences:
            found.append(f"{name} beat must be {sentences} sentence(s)")
        if "\n" in beat or "\r" in beat:
            found.append(f"{name} beat must be a single line")
    return found


def problems(text: str) -> list:
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if len(text) != EXPECTED_LENGTH:
        found.append(
            f"entry is {len(text)} code points, expected {EXPECTED_LENGTH}"
        )
    if not MIN_LEN <= len(text) <= MAX_LEN:
        found.append(f"entry must be {MIN_LEN}-{MAX_LEN} code points")
    stripped = text.strip()
    if not stripped:
        found.append("entry must not be only white space")
    if text != stripped:
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if not stripped.endswith("."):
        found.append("entry must end as one sentence")
    if text.count("boxes") != EXPECTED_BOXES:
        found.append(f"entry must mention boxes {EXPECTED_BOXES} times")
    if fingerprint(text) != EXPECTED_SHA256:
        found.append("entry does not match the expected fingerprint")
    return found


def output_path() -> str:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write the line to path, creating the directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


def verify_entry(path: str, text: str) -> bool:
    """Read the file back as bytes; it must match the line exactly."""
    with open(path, "rb") as f:
        return f.read() == text.encode("utf-8")


def main() -> int:
    bad = check_beats()
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    text = build_line()
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    path = output_path()
    write_entry(path, text)
    if not verify_entry(path, text):
        print("entry.txt does not match the review line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
