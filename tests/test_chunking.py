# tests/test_chunking.py

import pytest
from chunking.chunker import chunk_text


def test_chunk_text_basic():
    text = "a" * 1000
    chunks = chunk_text(text, chunk_size=500, overlap=100)

    assert len(chunks) > 1
    assert all(len(chunk) <= 500 for chunk in chunks)


def test_chunk_text_empty():
    chunks = chunk_text("")
    assert chunks == []


def test_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text("test text", chunk_size=100, overlap=200)

