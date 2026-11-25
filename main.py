"""The Moon Finally Answers Back — make.fun entry (program/v1).

Writes the Moon's one-line answer to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only, no network, no clock,
no randomness: the output is identical on every run.
"""

import os

LINE = "I don't grant wishes. I move oceans. Twice a day, on time, for four billion years \u2014 your turn."


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"line is {len(LINE)} chars, gate is 1-240")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            raise SystemExit("round-trip mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
