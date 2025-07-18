from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/devast")
async def handle_webhook(request: Request):
    data = await request.json()
    print("Получено от игры:", data)

    return JSONResponse({
        "type": "commands",
        "content": ["move", "attack"]
    })
