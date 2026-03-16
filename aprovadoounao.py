
respostas = []

rc1 = 1
rc2 = 2
rc3 = 1
rc4 = 2
rc5 = 3
rc6 = 4
rc7 = 1
rc8 = 2
rc9 = 2
rc10 = 2
respostas_corretas = [rc1,rc2,rc3,rc4,rc5,rc6,rc7,rc8,rc9,rc10]

while True:
    print("Questionário\n")
    
    print("Pergunta1")
    print("O que é uma variável? (P1)")
    print("1) Um lugar para guardar dados | [1]")
    print("2) Um tipo de computador | [2]")
    print("3) Um sistema operacional | [3]")
    print("4) Um periférico | [4]")
    
    r1 = int(input("\nSua resposta: "))
    respostas.append(r1)
    
    print("\nPergunta 2:")
    print("O que é um algoritmo?")
    print("1) Um tipo de computador | [1]")
    print("2) Um conjunto de passos para resolver um problema | [2]")
    print("3) Um programa de edição de texto | [3]")
    print("4) Um tipo de memória do computador | [4]")
    
    r2 = int(input("\nSua resposta: "))
    respostas.append(r2)
    
    print("\nPergunta 3:")
    print("O que é uma entrada (input) em um algoritmo?")
    print("1) O resultado final do programa | [1]")
    print("2) Um erro no código | [2]")
    print("3) Um dado que o usuário ou sistema fornece ao programa | [3]")
    print("4) Um tipo de variável | [4]")
    
    r3 = int(input("\nSua resposta: "))
    respostas.append(r3)
    
    print("\nPergunta 4:")
    print("O que é uma estrutura de repetição (loop)?")
    print("1) Um erro que trava o computador | [1]")
    print("2) Um comando que executa um bloco de código várias vezes | [2]")
    print("3) Uma variável que guarda números inteiros | [3]")
    print("4) O nome dado ao teclado e mouse | [4]")
    
    r4 = int(input("\nSua resposta: "))
    respostas.append(r4)

    print("\nPergunta 5:")
    print("Qual é a função de uma estrutura condicional (if/else)?")
    print("1) Somar dois números automaticamente | [1]")
    print("2) Repetir o código para sempre | [2]")
    print("3) Tomar decisões no código baseadas em uma condição | [3]")
    print("4) Deletar arquivos do sistema | [4]")
    
    r5 = int(input("\nSua resposta: "))
    respostas.append(r5)

    print("\nPergunta 6:")
    print("O que é uma 'String' na programação?")
    print("1) Um tipo de dado usado para textos | [1]")
    print("2) Um cabo de conexão de rede | [2]")
    print("3) Um número decimal | [3]")
    print("4) Uma peça física do processador | [4]")
    
    r6 = int(input("\nSua resposta: "))
    respostas.append(r6)

    print("\nPergunta 7:")
    print("O que significa 'compilar' um programa?")
    print("1) Traduzir o código para uma linguagem que o computador entende | [1]")
    print("2) Desligar o computador com segurança | [2]")
    print("3) Escrever o código em um papel | [3]")
    print("4) Aumentar a velocidade da internet | [4]")
    
    r7 = int(input("\nSua resposta: "))
    respostas.append(r7)

    print("\nPergunta 8:")
    print("O que é um valor Booleano?")
    print("1) Um número muito grande | [2]")
    print("2) Um tipo de dado que pode ser apenas Verdadeiro ou Falso | [2]")
    print("3) O nome de um monitor antigo | [3]")
    print("4) Uma lista de nomes | [4]")
    
    r8 = int(input("\nSua resposta: "))
    respostas.append(r8)

    print("\nPergunta 9:")
    print("O que é um erro de sintaxe?")
    print("1) Um problema na conexão com a internet | [1]")
    print("2) Um erro nas regras de escrita da linguagem de programação | [2]")
    print("3) Quando o computador esquenta demais | [3]")
    print("4) Um vírus no sistema operacional | [4]")
    
    r9 = int(input("\nSua resposta: "))
    respostas.append(r9)

    print("\nPergunta 10:")
    print("O que é uma saída (output) em um algoritmo?")
    print("1) O momento em que o usuário fecha o programa | [1]")
    print("2) O dado ou resultado exibido pelo programa após o processamento | [2]")
    print("3) O botão de ligar o computador | [3]")
    print("4) Uma forma de apagar o código-fonte | [4]")
    
    r10 = int(input("\nSua resposta: "))
    respostas.append(r10)
    
    nota = 0
    for i in range(len(respostas_corretas)):
        if respostas[i] == respostas_corretas[i]:
            nota += 1
    
    print("RESULTADO\n")
    print(f"Você acertou {nota} questões")
    
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
    
    dnv = int(input("\nDeseja responder o questionário novamente? Sim[1] | Não[2] "))
    if dnv == '2':
        break
    else:
        respostas = []
        continue
    
    