Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, jsonify
... from notion_client import Client
... 
... app = Flask(__name__)
... 
... # Inicializar o cliente do Notion
... notion = Client(auth="seu_token_aqui")
... 
... @app.route('/')
... def home():
...     return "Bem-vindo ao Bot Poe!"
... 
... @app.route('/notion-page')
... def notion_page():
...     page_id = "seu_page_id_aqui"
...     page = notion.pages.retrieve(page_id)
...     return jsonify(page)
... 
... if __name__ == '__main__':
