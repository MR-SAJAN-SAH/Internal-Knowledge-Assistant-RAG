# app/config.py

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DOCS_DIR = DATA_DIR / "raw"

# Embeddings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Retrieval
TOP_K = 5

# LLM
LLM_MODEL = "gpt-4o-mini"


