questionario = []

while True:
    # criar perguntas
    texto_pergunta = input("\nDigite o enunciado da pergunta (digite 'sair' para finalizar o loop)")
    if texto_pergunta.lower() == "sair":
        break
    
    opcoes = []
    for i in range(1, 5):
        opt = input(f"Digite a questão {i}")
        opcoes.append(opt)
    
    while True:
        try:
            correta = int(input("Qual a opção correta? (1-4): "))
            if correta in [1, 2, 3, 4]:
                break  # opção válida, sai do loop de validação
            else:
                print("Opção inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("Digite apenas números!")
    
    pergunta_completa = {
        "pergunta": texto_pergunta,
        "opcoes": opcoes,
        "correta": correta
    }
    
    questionario.append(pergunta_completa)
    print("Pergunta completa adicionada com sucesso.")

print("\nQuestionário completo:")
for idx, q in enumerate(questionario, 1):
    print(f"{idx}. {q['pergunta']} -> {q['opcoes']} (Correta: {q['correta']})")
        