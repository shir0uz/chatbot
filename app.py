from flask import Flask, request, jsonify
from chatbot import Servicos, ChatBot  # importa seu código

app = Flask(__name__)

# Inicializa o bot
servicos = Servicos()
bot = ChatBot("formal", servicos)  # personalidade inicial = formal

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    pergunta = data.get("pergunta", "")
    resposta = bot.responder(pergunta)
    return jsonify({"resposta": resposta})

@app.route("/mudar_personalidade", methods=["POST"])
def mudar_personalidade():
    data = request.json
    nova = data.get("personalidade", "formal")
    bot.mudar_personalidade(nova)
    return jsonify({"status": "ok", "personalidade": nova})

@app.route("/historico", methods=["GET"])
def historico():
    return jsonify({
        "historico": [
            {"usuario": entrada, "bot": resposta}
            for entrada, resposta in bot.historico
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
