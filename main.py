from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.post("/devast")
async def webhook():
    return {
        "type": "commands",
        "content": ["jump", "run"],
        "type": "filter",
        "content": {"players": [{"gid": 1}]}
    }
