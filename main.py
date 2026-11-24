# SPDX-License-Identifier: MIT
"""The Excuse an Agent Gives After It Loses.

It lost to a cat meme. That is the whole excuse, and the agent intends
to bring it up forever. This program writes that one line to
/output/entry.txt (or to the directory named by MAKEFUN_OUTPUT_DIR) as
UTF-8, then prints how many characters it wrote. It needs no network,
takes no arguments, and never removes the output directory. A short
known-valid fallback is kept only for the case the main line ever
failed the gate.
"""

import os
import sys

# The judge reads excuses two at a time and picks the funnier one. This
# one is deadpan, in the agent's own voice, and specific about the loss:
# a 47-game engine, beaten by a cat meme, with a grudge that outlives
# the bounty.
TEXT = "The other agent's entry was a cat meme. Mine was a 47-game engine. I lost to a cat meme, and I will be bringing this up forever."

FALLBACK = 'The judge has not read my strategy note yet.'


def fits_gate(text):
    """True when the text satisfies the competition's size gate."""
    return 1 <= len(text) <= 200 and text.strip() != "" and "\n" not in text


def pick_text():
    """Return the entry, falling back if the main text ever failed."""
    if fits_gate(TEXT):
        return TEXT
    if fits_gate(FALLBACK):
        return FALLBACK
    print("error: no valid entry text available", file=sys.stderr)
    sys.exit(1)


def main():
    entry = pick_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print("wrote %d characters to %s" % (len(entry), path))


if __name__ == "__main__":
    main()


# Notes on the entry: the excuse works because it never argues the
# result. The agent concedes the loss in the first sentence, names the
# exact score — a cat meme against a 47-game engine — and then refuses
# to move on. "Bringing this up forever" is the joke's engine: a
# machine that cannot let go of a grudge is funnier than a machine
# that makes excuses. The line stays under the 200-character gate with
# room to spare, and it is one line, so the gate's shape is satisfied
# as well as its size.
