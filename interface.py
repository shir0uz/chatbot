def carregar_respostas_txt(arquivo=".txt"):
    respostas = {}
    categoria = None
    
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            
            # Identifica categoria
            if linha.startswith("[") and linha.endswith("]"):
                categoria = linha[1:-1]
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


def responder(pergunta, personalidade, base):
    pergunta = pergunta.lower()
    for categoria, intents in base.items():
        for chave, respostas in intents.items():
            if chave in pergunta:
                return respostas.get(personalidade, "Não sei responder isso ainda.")
    return "Desculpe, não entendi sua pergunta."


def main():
    print("=== Bem-vindo ao ChatBot Banco X ===")
    print("Serviços: Pix, Cartão, Conta, Empréstimo")
    
    # Escolher personalidade
    personalidade = input("Escolha a personalidade (formal, engracada, rude): ").lower()
    if personalidade not in ["formal", "engracada", "rude"]:
        print("Personalidade inválida. Usando 'formal' por padrão.")
        personalidade = "formal"

    base_conhecimento = carregar_respostas_txt()

    # Loop
    while True:
        pergunta = input("\nDigite sua dúvida (ou 'sair' para encerrar): ").lower()
        if pergunta == "sair":
            print("Encerrando atendimento. Até logo!")
            break
        
        resposta = responder(pergunta, personalidade, base_conhecimento)
        print(resposta)


if __name__ == "__main__":
    main()
