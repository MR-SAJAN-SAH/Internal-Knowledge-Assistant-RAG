# embeddings/vector_store.py

from typing import List, Tuple, Dict
import logging
import faiss
import numpy as np

logger = logging.getLogger(__name__)


class VectorStore:
    """
    FAISS-based in-memory vector store.
    Stores embeddings along with chunk text and metadata.
    """

    def __init__(self, embedding_dim: int):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.store: List[Dict] = []

    def add(
        self,
        embeddings: List[List[float]],
        texts: List[str],
        metadatas: List[Dict],
    ) -> None:
        if not (len(embeddings) == len(texts) == len(metadatas)):
            raise ValueError("Embeddings, texts, and metadata must have same length")

        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)

        for text, meta in zip(texts, metadatas):
            self.store.append(
                {
                    "text": text,
                    "metadata": meta,
                }
            )

        logger.info(f"Added {len(embeddings)} chunks to vector store")

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
    ) -> List[Dict]:
        if self.index.ntotal == 0:
            return []

        query = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx == -1:
                continue

            item = self.store[idx]
            results.append(
                {
                    "score": float(dist),
                    "text": item["text"],
                    "metadata": item["metadata"],
                }
            )

        return results

    def size(self) -> int:
        return self.index.ntotal

