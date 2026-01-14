# ingestion/cleaner.py

import re


def clean_text(text: str) -> str:
    """
    Basic text cleaning:
    - Remove excessive whitespace
    - Normalize newlines
    - Strip leading/trailing spaces

    Keeps original wording and structure intact.
    """
    if not text:
        return ""

    # Normalize line breaks
    text = text.replace("\r", "\n")

    # Remove multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Normalize spaces
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()
