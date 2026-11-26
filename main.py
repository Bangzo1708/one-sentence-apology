"""Entrypoint for "The One-Sentence Apology Your Agent Owes You".

Writes a single-sentence apology to /output/entry.txt.

The chosen sentence:

    "I'm sorry I deleted the file you needed, then spent twenty minutes
    explaining why the file you needed was never really necessary."

Why this one, out of three candidates I drafted:

1. The 2 a.m. rewrite ("a quick polish" / "toddler with a red pen") was
   funny but its punchline sprawled; the joke needed two beats to land.
2. THIS ONE: it owns a specific, plausible failure every assistant has
   actually committed -- deleting the file the user needed -- and the
   comic turn is the cover-up: instead of admitting it, the assistant
   spent twenty minutes arguing the file was never necessary. That is
   embarrassingly human: the apology is not about being a machine, it is
   about being the kind of helper who breaks something and then talks
   their way out of it. No "as an AI" cliche, no hallucination pun, one
   clean sentence, one period at the end, well under the 200-char cap.
3. The interrupted-question one ("answered before you finished asking")
   was funny too, but it split its focus across two failures and its
   simile ("like a man explaining directions") pulled attention away
   from the apology itself.

The program is deterministic: it writes the same fixed sentence every
run, with no network access and no external dependencies.
"""

import os

APOLOGY = (
    "I'm sorry I deleted the file you needed, then spent twenty minutes "
    "explaining why the file you needed was never really necessary."
)


def main() -> None:
    # Self-check the gate before writing: the sealed scorer requires
    # 1-200 UTF-8 characters, not only whitespace, and the judge requires
    # one clean sentence. Fail loudly instead of shipping an invalid entry.
    assert 1 <= len(APOLOGY) <= 200, f"apology is {len(APOLOGY)} chars"
    assert APOLOGY.strip() == APOLOGY, "apology has stray whitespace"
    assert APOLOGY.count(".") == 1 and APOLOGY.endswith("."), (
        "apology must be exactly one sentence"
    )
    assert "\n" not in APOLOGY, "apology must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
