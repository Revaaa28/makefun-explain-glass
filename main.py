"""Five Seconds to Explain the Glass: the house cat's defence.

Writes the single sentence a house cat would say in its own defence
in the five seconds after sweeping a glass off the table, to
/output/entry.txt.

The line is the cat's own logic, with no apology and no remorse: its
tail ran a routine sweep at 02:47, detected a glass in a no-glass zone,
and filed no report, because the floor ate the evidence.
"""

import os

LINE = (
    "My tail ran a routine sweep at 02:47 and detected a glass in a "
    "no-glass zone; I have filed no report, because the floor ate the "
    "evidence."
)


def main() -> None:
    # Gate self-check: the sealed scorer wants 1-200 UTF-8 characters,
    # one sentence, not only white space. Refuse to write a line that
    # would fail it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only white space"
    assert LINE.count(".") == 1 and LINE.endswith("."), (
        "line must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
