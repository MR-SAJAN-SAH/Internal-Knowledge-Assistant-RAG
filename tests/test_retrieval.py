# tests/test_retrieval.py

from embeddings.embedder import Embedder
from embeddings.vector_store import VectorStore
from retrieval.retriever import Retriever


def test_retrieval_returns_results():
    texts = [
        "Company policy on remote work",
        "Vacation policy and holidays",
        "Internal security guidelines",
    ]

    embedder = Embedder()
    embeddings = embedder.embed_texts(texts)

    store = VectorStore(embedding_dim=len(embeddings[0]))
    store.add(
        embeddings,
        [{"file_name": "doc.txt", "chunk_id": str(i)} for i in range(len(texts))],
    )

    retriever = Retriever(embedder, store)
    results = retriever.retrieve("vacation policy")

    assert len(results) > 0

