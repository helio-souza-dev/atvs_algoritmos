questionario = []

# usuário escolhe quantas perguntas quer
while True:
    try:
        quantidade = int(input("Quantas perguntas você deseja criar? "))
        if quantidade > 0:
            break
        else:
            print("Digite um número maior que 0.")
    except ValueError:
        print("Digite apenas números!")

# loop baseado na quantidade
for n in range(quantidade):
    print(f"\n--- Pergunta {n+1} ---")
    
    texto_pergunta = input("Digite o enunciado da pergunta: ")
    
    opcoes = []
    for i in range(1, 5):
        opt = input(f"Digite a opção {i}: ")
        opcoes.append(opt)
    
    while True:
        try:
            correta = int(input("Qual a opção correta? (1-4): "))
            if correta in [1, 2, 3, 4]:
                break
            else:
                print("Opção inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("Digite apenas números!")
    
    pergunta_completa = {
        "pergunta": texto_pergunta,
        "opcoes": opcoes,
    }
    
    questionario.append(pergunta_completa)
    print("Pergunta adicionada com sucesso!")

# exibir resultado final
print("\nQuestionário completo:")
numero = 1

for pergunta in questionario:
    print()
    print(numero, ".", pergunta["pergunta"])
    
    numero_opcao = 1
    for opcao in pergunta["opcoes"]:
        print("  ", numero_opcao, ")", opcao)
        numero_opcao += 1
    
    numero += 1