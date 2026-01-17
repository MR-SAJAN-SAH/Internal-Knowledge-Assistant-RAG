# embeddings/embedder.py

from typing import List
import logging

from sentence_transformers import SentenceTransformer


logger = logging.getLogger(__name__)


class Embedder:
    """
    Wrapper around sentence-transformers embedding model.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        logger.info(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of text chunks.
        """
        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            show_progress_bar=False,
            convert_to_numpy=True,
        )

        return embeddings.tolist()


