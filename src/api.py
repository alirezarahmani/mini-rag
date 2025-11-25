from fastapi import FastAPI
from pydantic import BaseModel
from .rag import CreaRag

app = FastAPI(title="CREA MLS RAG API")
rag = CreaRag()

class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    result = rag.answer(req.query)
    return AskResponse(answer=result["answer"])
