from flask import Flask, jsonify, request
from notion_client import Client

app = Flask(__name__)

# Configuração do Notion (USE SEUS DADOS AQUI)
NOTION_TOKEN = "ntn_m98866820446i8eef1p2rxFgu2lpeDyHD9Wj9DSnnIZ7v7"
PAGE_ID = "1bc24d4acbbc8090a3a8e9bf10279463"

# Inicializa o cliente do Notion
notion = Client(auth=NOTION_TOKEN)

@app.route('/', methods=['POST'])
def handle_request():
    # Recebe a mensagem do usuário pelo Poe
    user_message = request.json.get("message", "").strip().lower()

    # Lógica de resposta
    if user_message == "oi":
        return jsonify({
            "response": "Olá! Eu sou seu assistente do Notion. 😊 Digite 'notion' para ver seus dados."
        })

    elif user_message == "notion":
        try:
            # Acessa a página no Notion
            page = notion.pages.retrieve(PAGE_ID)
            
            # Extrai o título da página (se existir)
            page_title = page.get("properties", {}).get("title", {}).get("title", [{}])[0].get("plain_text", "Sem título")
            
            return jsonify({
                "response": f"📝 Página do Notion: {page_title}\n\nDados completos: {page}"
            })
            
        except Exception as error:
            return jsonify({
                "response": f"❌ Erro ao acessar o Notion: {str(error)}"
            })

    else:
        return jsonify({
            "response": "🤔 Não entendi. Tente 'oi' ou 'notion'."
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)