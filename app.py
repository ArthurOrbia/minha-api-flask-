from flask import Flask, jsonify
from notion_client import Client

app = Flask(__name__)

# Inicializar o cliente do Notion com o token fornecido
notion = Client(auth="ntn_L9886682044bgWRgx2ZwktT5fd0LLH6sKarImTF9sO1eYu")

@app.route('/')
def home():
    return "Bem-vindo ao Bot Poe!"

@app.route('/notion-page')
def notion_page():
    # Extrair o page_id do link fornecido
    page_id = "1bc24d4acbbc8090a3a8e9bf10279463"
    page = notion.pages.retrieve(page_id)
    return jsonify(page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)