# ingestion/loader.py

from pathlib import Path
from typing import Dict
import logging

import pdfplumber


logger = logging.getLogger(__name__)


def load_document(file_path: Path) -> Dict[str, str]:
    """
    Load a document and extract raw text.

    Supported formats:
    - .pdf
    - .txt

    Returns:
        dict with keys: content, source, file_name
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        text = _load_pdf(file_path)
    elif suffix == ".txt":
        text = _load_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")

    return {
        "content": text,
        "source": suffix.replace(".", ""),
        "file_name": file_path.name,
    }


def _load_pdf(file_path: Path) -> str:
    logger.info(f"Loading PDF: {file_path.name}")
    pages_text = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                pages_text.append(page_text)

    return "\n".join(pages_text)


def _load_txt(file_path: Path) -> str:
    logger.info(f"Loading TXT: {file_path.name}")
    return file_path.read_text(encoding="utf-8", errors="ignore")
