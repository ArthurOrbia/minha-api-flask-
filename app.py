from flask import Flask, jsonify, request
from notion_client import Client

app = Flask(__name__)

# Configuração (VOCÊ VAI AJUSTAR AQUI)
TOKEN_NOTION = "ntn_m98866820446i8eef1p2rxFgu2lpeDyHD9Wj9DSnnIZ7v7"  # Cole SEU token aqui
LINK_TABELA = "https://www.notion.so/1bc24d4acbbc8090a3a8e9bf10279463"  # Cole o link da SUA tabela

notion = Client(auth=TOKEN_NOTION)

@app.route('/', methods=['POST'])
def bot():
    try:
        pergunta = request.json.get("message", "").lower()
        
        # Extrai o termo de busca (ex: "Qual o documento sobre contratos?" → "contratos")
        termo_busca = pergunta.split("sobre")[-1].strip()
        
        if termo_busca:
            # Busca no Notion (só na coluna "Nome do documento")
            resultados = notion.databases.query(
                database_id=LINK_TABELA.split('/')[-1].split('?')[0],
                filter={
                    "property": "Nome do documento",  # Nome exato da coluna
                    "title": {
                        "contains": termo_busca
                    }
                }
            )
            
            # Formata a resposta
            documentos = []
            for item in resultados.get("results", []):
                nome = item["properties"]["Nome do documento"]["title"][0]["plain_text"]
                documentos.append(f"📄 {nome}")
            
            return jsonify({
                "response": "🔍 Resultados:\n" + "\n".join(documentos) if documentos else "Nenhum documento encontrado."
            })
            
        return jsonify({
            "response": "Pergunte assim: 'Qual o documento sobre [assunto]?'"
        })
    
    except Exception as e:
        return jsonify({
            "response": f"⚠️ Erro: {str(e)}"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)