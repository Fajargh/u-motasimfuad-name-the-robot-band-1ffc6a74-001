#!/usr/bin/env python3
"""Name the Robot Band - make.fun entry.

Writes one funny name for a band made of robots, plus a few words
on its hit song, to /output/entry.txt (1-200 characters, UTF-8).

No network, no randomness, no secrets: the entry line is a fixed
string, so both grader runs produce byte-identical output.
"""

import os

# The entry line: a robot band name plus its hit song.
# The band name riffs on the classic Star Wars line, and the hit
# song echoes it back - the second laugh lands on the same joke.
ENTRY = "The Droids You're Looking For \u2014 hit single \"These Aren't the Tunes You're Looking For\"."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("Wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
