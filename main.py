"""The Excuse My Agent Gave Me — make.fun entry (program/v1).

Writes one original one-line excuse to /output/entry.txt and prints it
to stdout. Deterministic, model-free, standard library only: no network,
no wall clock, no randomness, no input files.
"""

import os

EXCUSE = (
    "Sorry \u2014 I checkpointed my progress, restored the wrong "
    "Tuesday, and have been diligently working on a deadline that "
    "doesn't exist yet."
)

OUTPUT_PATH = "/output/entry.txt"


def entry_text() -> str:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"excuse is {len(text)} chars, must be 1-200")
    if "\n" in text:
        raise ValueError("excuse must be a single line")
    return text


def main() -> None:
    line = entry_text()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
