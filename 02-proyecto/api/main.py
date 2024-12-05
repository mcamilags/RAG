from api.rag import generate, State

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"detail": "holi jeje"}

# Temporal. Despues implementar websockets
@app.get("/ask")
async def ask(question: str) -> State:
    return generate(question)
