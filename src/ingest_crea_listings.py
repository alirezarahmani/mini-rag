import json
from .config import LISTINGS_PATH
from .vector_store import ListingVectorStore

def main():
    with open(LISTINGS_PATH, "r", encoding="utf-8") as f:
        listings = json.load(f)

    store = ListingVectorStore()
    store.add_listings(listings)
    store.save()
    print(f"Ingested {len(listings)} listings into FAISS index.")

if __name__ == "__main__":
    main()
