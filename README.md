# 📦 CREA MLS RAG Playground

### Tiny Real-Estate RAG Demo Using Python, FAISS, and OpenAI Embeddings

A minimal yet practical RAG system built around **CREA MLS-style listings**, using:

-   Python
    
-   FAISS (vector search)
    
-   FastAPI
    
-   OpenAI embeddings + chat models
    

This repo is built as a companion to the article:

👉 **RAG Explained: Engineering Scalable Search Without Hallucinations**  
[https://nidly.substack.com/p/rag-explained-engineering-scalable?r=a3p8i](https://nidly.substack.com/p/rag-explained-engineering-scalable?r=a3p8i)

If you're coming from that post, this is the hands-on demo.

If not, go read the post. You’ll understand RAG better in 10 minutes
----------

## 🚀 What This Repo Shows

This project gives you a simple but realistic end-to-end pipeline:

1.  **Fake CREA listings** (structured JSON)
    
2.  **Text → Embedding conversion**
    
3.  **FAISS index for similarity search**
    
4.  **Retrieval pipeline (Top-K)**
    
5.  **RAG assembly layer for clean prompts**
    
6.  **FastAPI endpoint: `/ask`**
    

All in less than 300 lines of code.  
No frameworks. No junk. Just engineering.

----------

## 🧩 Project Structure

```
crea-mls-rag-playground/
  ├── data/
  │    └── listings.json        ← sample CREA-style listings
  ├── src/
  │    ├── config.py            ← env, config
  │    ├── embeddings.py        ← embedding helper
  │    ├── vector_store.py      ← FAISS index builder & search
  │    ├── ingest_crea_listings.py
  │    ├── rag.py               ← retrieval + generation
  │    └── api.py               ← FastAPI server
  ├── requirements.txt
  ├── README.md   (this file)

```

----------

## ⚡ Quickstart

Install deps:

```bash
pip install -r requirements.txt

```

Create embeddings + FAISS index:

```bash
python -m src.ingest_crea_listings

```

Run API:

```bash
uvicorn src.api:app --reload

```

Query:

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "show me condos with ocean view"}'

```

----------

## 🧠 Why Real Estate?

Real estate has:

-   Rich structured metadata
    
-   Semi-structured descriptions
    
-   High-variance natural language
    
-   Real-world need for relevance ranking
    

It’s the perfect playground for understanding embeddings, vector-search, and RAG…  
and honestly،

----------

## 🤝 About the Author

Built by **Alireza Rahmani Khalili**  
Principal Software Engineer • AI Engineering • DDD • MLS Systems

-   Substack: **[https://nidly.substack.com](https://nidly.substack.com/)**
    
-   LinkedIn: **[https://www.linkedin.com/in/alirezarahmani/](https://www.linkedin.com/in/alirezarahmani/)**
    
-   Personal Website: **[https://alirezarahmani.com](https://alirezarahmani.com/)**
    

Alireza writes about:

-   AI engineering
    
-   Vector databases
    
-   Domain-Driven Design
    
-   Real-estate listing systems
    
-   Building nation-scale data pipelines
    

If you're into engineering that actually works in production, subscribe.  
