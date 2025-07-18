from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/devast', methods=['POST'])
def webhook():
    data = request.json
    
    # Обработка данных от игры
    if 'players' in data:
        commands = []
        
        # Пример: выдаем предмет всем игрокам
        for player in data['players']:
            player_id = player.get('gid')
            login = player.get('login', '')
            
            # Формируем команду выдачи предмета
            commands.append(f"!item-to={player_id}:{login}:wood*10")
        
        # Отправляем команды в игру
        return jsonify({
            "type": "commands",
            "content": commands
        })
    
    return jsonify({"type": "commands", "content": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
