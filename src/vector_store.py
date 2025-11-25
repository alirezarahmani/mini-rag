import json
import faiss
import numpy as np
from typing import List, Dict, Tuple
from .embeddings import get_embedding
from .config import VECTOR_INDEX_PATH, METADATA_PATH

class ListingVectorStore:
    def __init__(self, dim: int = 1536):
        self.dim = dim
        self.index = faiss.IndexFlatIP(dim)
        self.metadata: List[Dict] = []

    def add_listings(self, listings: List[Dict]):
        vectors = []
        for listing in listings:
            text = self._listing_to_text(listing)
            emb = get_embedding(text)
            vectors.append(emb)
            self.metadata.append({
                "listing_id": listing["listing_id"],
                "mls_number": listing["mls_number"],
                "address": listing["address"],
                "list_price": listing["list_price"],
                "summary": text
            })
        mat = np.array(vectors).astype("float32")
        faiss.normalize_L2(mat)
        self.index.add(mat)

    def search(self, query: str, top_k: int = 5) -> List[Tuple[Dict, float]]:
        q_emb = np.array([get_embedding(query)]).astype("float32")
        faiss.normalize_L2(q_emb)
        scores, idxs = self.index.search(q_emb, top_k)
        results = []
        for score, idx in zip(scores[0], idxs[0]):
            if idx == -1:
                continue
            results.append((self.metadata[idx], float(score)))
        return results

    def save(self):
        faiss.write_index(self.index, VECTOR_INDEX_PATH)
        with open(METADATA_PATH, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)

    def load(self):
        self.index = faiss.read_index(VECTOR_INDEX_PATH)
        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

    @staticmethod
    def _listing_to_text(listing: Dict) -> str:
        return (
            f"MLS {listing['mls_number']} at {listing['address']}. "
            f"Price {listing['list_price']} CAD. "
            f"{listing['bedrooms']} bed, {listing['bathrooms']} bath {listing['property_type']}. "
            f"Description: {listing['description']}. "
            f"Features: {', '.join(listing.get('features', []))}."
        )
