from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Эндпоинт для проверки состояния (для Render)
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

# Основной вебхук для Devast.io
@app.route('/devast', methods=['POST'])
def devast_webhook():
    data = request.json
    
    # Проверяем, что это данные от игры
    if 'players' not in data:
        return jsonify({"type": "commands", "content": []})
    
    commands = []
    
    # Пример: выдаем предмет всем игрокам
    for player in data['players']:
        player_id = player.get('gid')
        login = player.get('login', '')
        
        # Формируем команду выдачи предмета
        # Формат: !item-to=ID_игрока:Логин:Предмет*Количество
        commands.append(f"!item-to={player_id}:{login}:wood*10")
    
    # Отправляем команды в игру
    return jsonify({
        "type": "commands",
        "content": commands
    })

if __name__ == '__main__':
    # Используем порт из переменной окружения (для Render)
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
