gatos = ["perola", "estrela"]

print(gatos)
while True:
    
    try:
        quantidade = int(input("Digite a quantidade de gatos que você quer adicionar: "))
        for i in range(quantidade):
            nomes = input("digite o nome do seu gato: ")
            gatos.append(nomes)
        
        print("deseja ver a lista de gatos?")
        decisao = int(input("Sim [1] | Não [2]"))
            
        if decisao == 1:
            print(gatos)
            fim = int(input("deseja sair? Sim[1] Não[2]"))
            if fim == 1:
                break
            else:
                continue
        else:
            break
                
    except ValueError:
        print("Você precisa digitar um inteiro")
        



