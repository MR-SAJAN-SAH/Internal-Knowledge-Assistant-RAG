# retrieval/retriever.py

from typing import List, Dict
import logging

from embeddings.embedder import Embedder
from embeddings.vector_store import VectorStore

logger = logging.getLogger(__name__)


class Retriever:
    def __init__(
        self,
        embedder: Embedder,
        vector_store: VectorStore,
    ):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Dict]:
        if not query:
            return []

        query_embedding = self.embedder.embed_texts([query])[0]
        return self.vector_store.search(query_embedding, top_k)


