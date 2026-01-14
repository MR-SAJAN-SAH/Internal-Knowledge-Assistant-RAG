# ingestion/metadata.py

from typing import Dict
from datetime import datetime


def build_document_metadata(
    file_name: str,
    source: str,
) -> Dict[str, str]:
    """
    Create metadata for a document.
    """
    return {
        "file_name": file_name,
        "source": source,
        "ingested_at": datetime.utcnow().isoformat(),
    }


def build_chunk_metadata(
    document_metadata: Dict[str, str],
    chunk_id: int,
) -> Dict[str, str]:
    """
    Extend document metadata with chunk-level information.
    """
    metadata = document_metadata.copy()
    metadata["chunk_id"] = str(chunk_id)
    return metadata
