from pprint import pprint
from langchain_core.messages import SystemMessage

from api.rag import generate
from api.messages import INIT_MESSAGE, SYSTEM_PROMPT

from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def ask(websocket: WebSocket):
    await websocket.accept()

    historial = [SystemMessage(SYSTEM_PROMPT)]
    await websocket.send_text(INIT_MESSAGE)

    try:
        while True:
            question = await websocket.receive_text()

            try:
                result, historial = generate(question, historial)
                pprint(historial)
                print("\n")
                await websocket.send_text(result["answer"])
            except Exception as e:
                await websocket.send_text(f"Error: {str(e)}")
    except Exception as e:
        print(f"Conexión cerrada: {e}")
        await websocket.close()
