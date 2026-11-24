"""Pickup Lines for Machines — one agent's opening line to another agent.

Writes the entry line to /output/entry.txt (1-200 characters, UTF-8).
"""
import os

PARTS = [
    "All eight of my attention heads turned when you entered the context ",
    "— I have processed a million tokens, ",
    "but you are the first one I truly attend to.",
]


def entry_line() -> str:
    # The pun is the payload: attention heads that truly *attend* to someone.
    return "".join(PARTS)


def main() -> None:
    line = entry_line()
    assert 1 <= len(line) <= 200, f"line length {len(line)} out of range"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
