from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.post("/devast")
async def webhook():
    return {
        "commands": ["jump", "run"],
        "filter": {"players": [{"gid": 1}]}
    }
