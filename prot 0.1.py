import os  # eu só consegui fazer funcionar a leitura de arquivo txt com o caminho absoluto (localização exata do arquivo) e essa biblioteca permite fazer esse caminho em qualquer computador
def chat(num_opcoes):    # função que recebe o número de opções e retorna a escolhida
    while True:
        try:          # loop de entrada de usuário que garante entradas válidas
            user_input = str(input())
            if user_input in [str(i) for i in range(0, num_opcoes + 1)]:
                return user_input
            else:
                raise ValueError
        except ValueError:
            print("Entrada inválida, por favor insira uma opção adequada.")



while True:
    print("Por favor selecione a personalidade de atendimento que deseja receber: 1. Formal e Preciso ; 2. Amigável, Acolhedora e Informal ; 3. Direto e Rápido ; 4. Mentor e Empreendedor. Caso a qualquer momento deseje sair da conversa, digite '0'.")
    persona = chat(4)

    if persona == '1':   # escolha da personalidade Sr.Bot
        print("Olá, sou o Sr.Bot, seu assistente da sua sessão de atendimento atual. Em que posso ajudar?", "\n", "1. Conta ; 2. Cartão ; 3. Empréstimo.")
        pergunta = chat(3)
        if pergunta == '1':     # identificação do arquivo txt conta baseado na escolha do usuário
            file_path = os.path.join(os.path.dirname(__file__), 'srbotconta.txt')   # local do arquivo
            with open(file_path, 'r', encoding='utf-8') as f:   # extrai o conteúdo do arquivo
                conteudo = f.readlines()       #leitura do arquivo txt
                print(conteudo[2]) # pergunta 1

    elif persona == '2':
        print("E aí, tudo bem? Eu sou a Amiga.Bot, sua assistente virtual super legal! Como posso te ajudar hoje?", "\n", "1. Conta ; 2. Cartão ; 3. Empréstimo.")
        pergunta = chat(3)
        if pergunta == '1':
            pass

    if persona == '0' or pergunta == '0':  # condição de saída do programa
        print("Sessão encerrada. Obrigado por utilizar nossos serviços.")
        break