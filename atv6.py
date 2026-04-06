produtos = []
contador_id = 1

terminou = False

while not terminou:
    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço do produto: "))
    
    produto = {
        "nome": nome,
        "preco": preco,
        "id": contador_id
    }
    
    produtos.append(produto)
    contador_id += 1
    
    escolha = input("Deseja adicionar mais um produto? Sim [s] | Não [n]: ")
    if escolha.lower() == "s":
        continue
    elif escolha.lower() == "n":
        terminou = True

for item in produtos:
    print(f"Nome do produto: {item['nome']} | Preço: {item['preco']} | Id: {item['id']}")