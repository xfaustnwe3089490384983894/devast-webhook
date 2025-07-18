from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Модель для входящих данных
class WebhookRequest(BaseModel):
    action: str = None  # Например, !item-to=...
    player_id: int = None
    login: str = None
    item: str = None
    quantity: int = None

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.post("/devast")
async def webhook(request: WebhookRequest):
    # Если есть действие !item-to, формируем команду
    if request.action and "item-to" in request.action.lower():
        command = f"!item-to={request.player_id}:[{request.login}]:{request.item}*{request.quantity}"
        return {
            "commands": [command],
            "filter": {"players": [{"gid": request.player_id}]}
        }
    # Если действия нет, возвращаем дефолтные команды
    return {
        "commands": ["jump", "run"],
        "filter": {"players": [{"gid": 1}]}
    }
