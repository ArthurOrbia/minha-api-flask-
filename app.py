from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    data = request.json  # Dados do Poe
    user_message = data.get("message", "").lower()

    if user_message == "oi":
        return jsonify({"response": "Olá! Eu sou seu bot. 😊"})  # ✅ Formato para o Poe
    else:
        return jsonify({"response": "Não entendi. Diga 'oi'!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)