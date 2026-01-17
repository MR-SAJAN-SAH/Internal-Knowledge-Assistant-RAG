# app/main.py

import logging
from fastapi import FastAPI

from app.api import register_routes
from app.config import EMBEDDING_MODEL
from embeddings.embedder import Embedder
from embeddings.vector_store import VectorStore
from retrieval.retriever import Retriever
from generation.generator import Generator

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Internal Knowledge Assistant (Retrieval-Based)",
    version="1.0.0",
)

# Shared components
embedder = Embedder(model_name=EMBEDDING_MODEL)
vector_store = VectorStore(embedding_dim=384)
retriever = Retriever(embedder, vector_store)
generator = Generator()


def create_app() -> FastAPI:
    router = register_routes(retriever, generator, vector_store)
    app.include_router(router)
    return app


app = create_app()




