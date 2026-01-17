# chunking/chunker.py

from typing import List


def chunk_text(
    text: str,
    chunk_size: int = 700,
    overlap: int = 100,
) -> List[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: cleaned input text
        chunk_size: number of characters per chunk
        overlap: number of overlapping characters between chunks

    Returns:
        List of text chunks
    """
    if not text:
        return []

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap

    return chunks


