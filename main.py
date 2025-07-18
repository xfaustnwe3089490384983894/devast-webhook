from fastapi import FastAPI

app = FastAPI()

@app.post("/devast")
async def webhook():
    return {
        "type": "commands",
        "content": ["jump", "run"],
        "type": "filter",
        "content": {"players": [{"gid": 1}]}
    }
