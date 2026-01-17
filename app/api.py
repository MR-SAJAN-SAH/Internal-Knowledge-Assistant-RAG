# app/api.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from pathlib import Path

from ingestion.loader import load_document
from ingestion.cleaner import clean_text
from ingestion.metadata import (
    build_document_metadata,
    build_chunk_metadata,
)
from chunking.chunker import chunk_text
from embeddings.vector_store import VectorStore
from retrieval.retriever import Retriever
from generation.generator import Generator
from app.config import RAW_DOCS_DIR, TOP_K


router = APIRouter()


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str


class UploadResponse(BaseModel):
    message: str
    total_chunks: int


def register_routes(
    retriever: Retriever,
    generator: Generator,
    vector_store: VectorStore,
):
    @router.post("/upload", response_model=UploadResponse)
    async def upload_document(file: UploadFile = File(...)):
        RAW_DOCS_DIR.mkdir(parents=True, exist_ok=True)

        file_path = RAW_DOCS_DIR / file.filename

        if file_path.exists():
            raise HTTPException(
                status_code=400,
                detail="File already exists",
            )

        # Save file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Ingestion pipeline
        doc = load_document(file_path)
        cleaned = clean_text(doc["content"])
        chunks = chunk_text(cleaned)

        doc_meta = build_document_metadata(
            doc["file_name"],
            doc["source"],
        )

        chunk_metas = [
            build_chunk_metadata(doc_meta, i)
            for i in range(len(chunks))
        ]

        embeddings = retriever.embedder.embed_texts(chunks)
        vector_store.add(embeddings, chunks, chunk_metas)


        return UploadResponse(
            message="Document uploaded and indexed successfully",
            total_chunks=len(chunks),
        )

    @router.post("/query", response_model=QueryResponse)
    def query_knowledge_base(request: QueryRequest):
        retrieved = retriever.retrieve(
            query=request.question,
            top_k=TOP_K,
        )

        answer = generator.generate_answer(
            question=request.question,
            contexts=retrieved,
        )

        return QueryResponse(answer=answer)

    return router



