"""Write the house cat's five-second defence to /output/entry.txt.

The cat knocked a glass off the counter and, given five seconds to
explain itself, offers this single sentence: a deadpan incident report
in which its own tail did the sweeping, the floor did the eating, and
the cat itself did nothing worth reporting. No apology, no remorse —
just a tidy transfer of blame to its tail and the floor, delivered in
one breath and timed to fit inside five seconds.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = (
    "My tail ran a routine sweep at 02:47 and detected a glass in a "
    "no-glass zone; I have filed no report, because the floor ate the "
    "evidence."
)


def check_line(line: str) -> None:
    """Gate self-checks: the line must be a valid one-sentence entry."""
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert line.strip(), "line must not be only whitespace"
    assert line.endswith("."), "line must end with a full stop"
    assert line.count(".") == 1, "line must be exactly one sentence"


def main() -> None:
    check_line(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
