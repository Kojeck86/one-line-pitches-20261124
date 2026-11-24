"""One-line pitch entry for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single persuasive sentence to /output/entry.txt.
Python standard library only; deterministic.
"""

import os

SENTENCE = (
    "Just describe your app idea in plain words and an AI agent on make.fun "
    "will build a first version you can actually try, no coding needed, and "
    "you can change anything until it feels like yours."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    if len(SENTENCE) > 240:
        raise ValueError("sentence exceeds 240 characters")
    # Exactly one sentence: a single terminal period, no ". " splits,
    # and no other sentence-ending punctuation. (The "make.fun" in the
    # sentence contains a period, so a plain "." count would miscount.)
    stripped = SENTENCE.strip()
    if not stripped.endswith(".") or ". " in stripped or "!" in stripped or "?" in stripped:
        raise ValueError("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
