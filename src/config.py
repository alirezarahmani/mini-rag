import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4.1-mini")

VECTOR_INDEX_PATH = os.getenv("VECTOR_INDEX_PATH", "data/faiss_index.bin")
METADATA_PATH = os.getenv("METADATA_PATH", "data/metadata.json")
LISTINGS_PATH = os.getenv("LISTINGS_PATH", "data/listings.json")
TOP_K = int(os.getenv("TOP_K", "5"))
