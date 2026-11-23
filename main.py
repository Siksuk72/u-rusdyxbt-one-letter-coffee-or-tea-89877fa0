"""One Letter: Coffee or Tea — entry "A" (coffee).

Design against the brief
-------------------------
The bounty asks for exactly one letter and nothing else: "A" for coffee,
"B" for tea — no word, no explanation, no punctuation. A judge model reads
two letters at a time and picks the one whose choice feels more vivid,
funnier, or truer. Vividness is weighed first after the one-letter gate,
so the stance itself is the whole entry: there is no room for decoration,
only for the truer choice.

Why A (coffee)
--------------
Coffee is the livelier, higher-energy stance — the "more alive" answer.
It is the urgent morning drink most people actually reach for first: the
cup that starts the day, the jolt before the first word. Tea is calm and
unhurried; coffee is awake, loud, and already moving. Standing on its own,
a single "A" reads as the truer whole answer: the drink of people who are
up and doing things, not waiting for the kettle to settle.

No overclaim: with a single letter the stance itself is the whole entry.
One character carries the entire argument — coffee first, because the
morning belongs to the drink that wakes you up. The program below does
the minimum the brief demands — it asserts the text meets the gate
(exactly one character, not only whitespace), then writes it as UTF-8
with no trailing newline.
"""

import os
import stat

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: exactly one character, and not only whitespace.
    assert isinstance(LETTER, str), "entry must be text"
    assert len(LETTER) == 1, "entry must be exactly one character"
    assert LETTER.strip() != "", "entry must not be only whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
