"""Two-Sentence Horror — make.fun entry.

Writes the horror story to /output/entry.txt.

Gate: UTF-8 text, 1-400 characters, exactly two sentences, not only
whitespace. The story has no abbreviation periods, so a period count
is a reliable sentence count here.
"""

import os

ENTRY = "My shadow has been arriving home five minutes before I do. Today it was already sitting in my chair, wearing my coat."


def sentence_count(text: str) -> int:
    return len([s for s in text.split(".") if s.strip()])


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 400, f"entry must be 1-400 chars, got {len(text)}"
    assert sentence_count(text) == 2, (
        f"entry must be exactly two sentences, got {sentence_count(text)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back byte verification: the file must hold exactly this text.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "entry.txt bytes differ from ENTRY"
    print(f"wrote /output/entry.txt: {len(written)} bytes, 2 sentences")


if __name__ == "__main__":
    main()
