class ChatBot:
    def __init__(self, personalidade):
        self.personalidade = personalidade
        self.historico = []

    def responder(self, pergunta): # Resposta gerada dependendo do humor
        pass

class Historico:
    def __init__(self):
        self.mensagens = []

    def adicionar(self, entrada, resposta):
        self.mensagens.append((entrada, resposta))

class Personalidade:
    def __init__(self, estilo):
        self.estilo = estilo  # "formal", "engracada", "rude"

    def gerar_resposta(self, topico, pergunta): # responde com base no "humor"
        pass

class Servicos:  # Módulo para organizar perguntas e respostas (Pix, Cartão, Conta, Empréstimo)
    dados = {
        "pix": {...},
        "cartao": {...},
        "conta": {...},
        "emprestimo": {...}
    }
