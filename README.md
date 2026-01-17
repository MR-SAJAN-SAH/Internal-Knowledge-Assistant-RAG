# Internal Knowledge Assistant (Retrieval-Based)

A production-oriented internal document search and knowledge assistant that enables reliable question answering over company documents using semantic retrieval.  
The system is fully local, avoids generative hallucinations, and focuses on trustworthy, source-grounded results.

---

## Overview

Organizations store critical knowledge across unstructured documents such as PDFs, manuals, resumes, policies, and reports. Traditional keyword-based search is often inefficient and fails to capture semantic meaning.

This project implements an internal knowledge assistant that allows users to upload documents and query them using semantic similarity, returning the most relevant document excerpts with clear source attribution.

The system is intentionally designed without external LLM APIs, prioritizing data privacy, explainability, and reliability.

---

## Key Features

- Upload PDF and text documents via API
- End-to-end document ingestion pipeline
- Semantic search using vector embeddings
- Fast similarity search with FAISS
- Source-grounded responses with chunk excerpts
- No external API dependencies
- Modular, production-style architecture

---

## System Architecture

1. **Document Upload**
   - Users upload PDF or TXT documents via an API endpoint
   - Files are stored locally for traceability

2. **Ingestion & Processing**
   - Text extraction from text-based PDFs
   - Basic text cleaning and normalization
   - Chunking with configurable overlap

3. **Embedding & Indexing**
   - Text chunks are converted into dense vector embeddings
   - Embeddings are stored in an in-memory FAISS index
   - Chunk text and metadata are preserved for retrieval

4. **Query & Retrieval**
   - User queries are embedded
   - Top-k most similar chunks are retrieved
   - Results are ranked by semantic similarity

5. **Answer Construction**
   - Retrieved chunks are returned directly as readable excerpts
   - Each excerpt includes file name and chunk ID for transparency

---

## Why Retrieval-Based (No LLM)

This project deliberately avoids generative language models.

**Rationale:**
- Prevents hallucinated answers
- Preserves original document wording
- Avoids external API usage
- Aligns with enterprise privacy requirements
- Easier to validate and audit

In many real-world enterprise systems, retrieval reliability is preferred over generative responses.

---

## Folder Structure

internal-knowledge-assistant-rag/
│
├── app/ # API layer
├── ingestion/ # Document loading & cleaning
├── chunking/ # Text chunking logic
├── embeddings/ # Embedding & vector store
├── retrieval/ # Semantic retrieval
├── generation/ # Response formatting
├── data/
│ └── raw/ # Uploaded documents
├── tests/ # Unit & integration tests
├── Dockerfile
├── requirements.txt
└── README.md


Each module has a single responsibility to ensure clarity and maintainability.

---

## API Endpoints

### Upload Document

Uploads a document and indexes it for semantic search.

**Supported formats**
- `.pdf` (text-based PDFs only)
- `.txt`

**Response**
```json
{
  "message": "Document uploaded and indexed successfully",
  "total_chunks": 12
}



Searches indexed documents and returns relevant document excerpts with source references.

Request
{
  "question": "Who is Sajan?"
}

Response (Example)
Question: Who is Sajan?

Relevant information:

Source: Old_Resume_Sajan.pdf | Chunk 0
Sajan Sah is a B.Tech Computer Science student specializing in Applied Machine Learning...

Source: Old_Resume_Sajan.pdf | Chunk 2
He has experience building end-to-end machine learning systems including churn prediction...


How to Run Locally
1. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

2. Install dependencies
pip install -r requirements.txt

3. Run tests
pytest

4. Start the API server
python -m uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

Docker Support
docker build -t internal-knowledge-assistant .
docker run -p 8000:8000 internal-knowledge-assistant

Limitations

Only text-based PDFs are supported (scanned PDFs or images are not processed)

Vector index is stored in memory and not persisted

No summary or generative answers

Response quality depends on document quality and chunking parameters

These limitations are intentional and documented.

Possible Extensions

OCR support for scanned PDFs

Persistent FAISS index

Hybrid keyword + semantic search

Optionally local or on-prem LLM integration

Authentication and access control

What This Project Demonstrates

Practical understanding of information retrieval systems

Clean ML + backend integration

Awareness of enterprise constraints

Modular and maintainable system design

Production-style API development
