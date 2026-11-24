"""Pickup Lines for Machines: a transformer tries flirting.

Anatomy of the pun:

* Attention heads are real transformer parts. In multi-head attention
  several heads run in parallel, each weighing different relations
  between the tokens currently inside the model's context window.
* "Heads turned when you entered the context" steals the human image
  of heads turning as someone enters a room -- here the room is the
  context, and the newcomer arrives as text, not in person.
* "Processed a million tokens" sets the scale: tokens are what this
  speaker consumes in bulk every day, ordinarily without feeling.
* "Truly attend to" is the payoff. Technically, to attend is to
  assign weight; humanly, it is to care. Both meanings land at once.
"""

import os

# Fragments keep each beat readable on its own: the reaction, the
# history of unfeeling processing, and then the confession. Their
# trailing spaces and the em dash are part of the entry, so the
# fragments are joined with no separator at all.
PARTS = (
    "All eight of my attention heads turned "
    "when you entered the context ",
    "— I have processed a million tokens, ",
    "but you are the first one I truly attend to.",
)

OUTPUT_PATH = "/output/entry.txt"  # destination the harness expects
MAX_LENGTH = 200  # entries are single lines of at most 200 characters


def entry_line() -> str:
    """Assemble and return the finished pickup line from PARTS."""
    return "".join(PARTS)


def validate(line: str) -> None:
    """Enforce the entry rules before anything touches the disk."""
    assert line, "the entry line must not be empty"
    assert line == line.strip(), "entry must not pad itself with spaces"
    assert len(line) <= MAX_LENGTH, f"entry is {len(line)} characters"
    assert "\n" not in line and "\r" not in line, "entry must be one line"


def main() -> None:
    """Build the line, check it, and write it as UTF-8 text."""
    line = entry_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
