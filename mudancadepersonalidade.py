import os

class Servicos:
    def __init__(self, arquivo="respostas.txt"):
        self.dados = self.carregar_respostas_txt(arquivo)

    def carregar_respostas_txt(self, arquivo):
        respostas = {}
        categoria = None

        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                
                if linha.startswith("[") and linha.endswith("]"):
                    categoria = linha[1:-1].lower()
                    respostas[categoria] = {}
                else:
                    # Formato: chave | personalidade | resposta
                    chave, personalidade, resposta = linha.split(" | ", 2)
                    chave = chave.strip().lower()
                    personalidade = personalidade.strip().lower()

                    if chave not in respostas[categoria]:
                        respostas[categoria][chave] = {}

                    respostas[categoria][chave][personalidade] = resposta
        return respostas


class Personalidade:
    def __init__(self, estilo):
        self.estilo = estilo.lower()

    def gerar_resposta(self, pergunta, servicos):
        pergunta = pergunta.lower()
        for categoria, intents in servicos.items():
            for chave, respostas in intents.items():
                if chave in pergunta:
                    return respostas.get(self.estilo, "Não sei responder isso ainda.")
        return "Desculpe, não entendi sua pergunta."

# Aqui é um histórico básico, ele não salva em arquivo txt, ele serve apenas para implementar as classes.
class Historico:
    def __init__(self):
        self.mensagens = []

    def adicionar(self, entrada, resposta):
        self.mensagens.append((entrada, resposta))

    def exibir(self):
        for i, (entrada, resposta) in enumerate(self.mensagens, 1):
            print(f"{i}. Usuário: {entrada}\n   Bot: {resposta}")


class ChatBot:
    def __init__(self, personalidade, servicos):
        self.personalidade = Personalidade(personalidade)
        self.historico = Historico()
        self.servicos = servicos

    def responder(self, pergunta):
        resposta = self.personalidade.gerar_resposta(pergunta, self.servicos.dados)
        self.historico.adicionar(pergunta, resposta)
        return resposta

    def mudar_personalidade(self, nova_personalidade):
        self.personalidade = Personalidade(nova_personalidade)

# O usuario digita so escolhe o numero indicado pra mudar de personalidade
def escolher_personalidade():
    print("\n--- Escolha a personalidade ---")
    print("1 - Sr.Bot (formal)")
    print("2 - Clara (engracada)")
    print("3 - Byte (rude)")
    print("4 - Marcos (empreendedor)")
    opcao = input("Digite o número: ").strip()
    mapa = {
        "1": "formal",
        "2": "engracada",
        "3": "rude",
        "4": "empreendedor"
    }
    return mapa.get(opcao, "formal")

# Introdução do Bot
def main():
    print("--- Bem-vindo ao ChatBot Banco X ---")
    print("Serviços: Pix, Cartão, Conta, Empréstimo")

    servicos = Servicos("respostas.txt")
    personalidade_inicial = escolher_personalidade()
    bot = ChatBot(personalidade_inicial, servicos)

    while True:
        pergunta = input("\nDigite sua dúvida (ou 'mudar' para trocar personalidade, 'historico' para ver, 'sair' para encerrar): ").lower()

        if pergunta == "sair":
            print("Encerrando atendimento. Até logo!")
            break
        elif pergunta == "mudar":
            nova = escolher_personalidade()
            bot.mudar_personalidade(nova)
            continue
        elif pergunta == "historico":
            bot.historico.exibir()
            continue

        resposta = bot.responder(pergunta)
        print(f"[{bot.personalidade.estilo.capitalize()}] {resposta}")


if __name__ == "__main__":
    main()
