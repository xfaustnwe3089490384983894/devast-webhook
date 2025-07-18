from fastapi import FastAPI

app = FastAPI()

@app.post("/devast")
async def webhook():
    return {
        "type": "commands",
        "content": ["jump", "run"]
    }
