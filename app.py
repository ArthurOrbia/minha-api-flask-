from flask import Flask, jsonify, request
from notion_client import Client

app = Flask(__name__)

# Inicializar o cliente do Notion com o token fornecido
notion = Client(auth="ntn_L9886682044bgWRgx2ZwktT5fd0LLH6sKarImTF9sO1eYu")

@app.route('/', methods=['GET', 'HEAD', 'POST'])
def home():
    if request.method == 'GET' or request.method == 'HEAD':
        # Resposta para requisições GET e HEAD
        return "Bem-vindo ao Bot Poe!", 200
    elif request.method == 'POST':
        # Dados enviados pelo Poe
        data = request.json
        user_message = data.get("message", "")

        # Lógica do bot (exemplo simples)
        if user_message.lower() == "oi":
            response = "Olá! Como posso ajudar?"
        elif "notion" in user_message.lower():
            try:
                # Extrair o page_id do link fornecido
                page_id = "1bc24d4acbbc8090a3a8e9bf10279463"
                page = notion.pages.retrieve(page_id)
                response = f"Aqui estão os dados da página do Notion: {page}"
            except Exception as e:
                response = f"Erro ao acessar o Notion: {str(e)}"
        else:
            response = "Desculpe, não entendi. Pode repetir?"

        # Retornar a resposta para o Poe
        return jsonify({"response": response})

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