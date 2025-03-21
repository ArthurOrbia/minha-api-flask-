from flask import Flask, jsonify, request
from notion_client import Client

app = Flask(__name__)

# Inicializar o cliente do Notion com o token fornecido
notion = Client(auth="ntn_L9886682044bgWRgx2ZwktT5fd0LLH6sKarImTF9sO1eYu")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Resposta padrão para requisições POST
        return jsonify({"message": "Bot está online!"})
    return "Bem-vindo ao Bot Poe!"

@app.route('/notion-page', methods=['GET', 'POST'])
def notion_page():
    try:
        # Extrair o page_id do link fornecido
        page_id = "1bc24d4acbbc8090a3a8e9bf10279463"
        page = notion.pages.retrieve(page_id)
        return jsonify(page)
    except Exception as e:
        # Retornar uma mensagem de erro em caso de falha
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)