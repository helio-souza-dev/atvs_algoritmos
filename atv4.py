print("bem vindo ao restaurante")

terminou = False
produto = [] # [0] = código – [1] desc – [2] preco
contador_codigo = 1

while not terminou:
    codigo = contador_codigo
    
    desc = input("digite a descrição do produto: ")
    
    preco = int(input("digite o valor do produto: "))
    
    produto.append([codigo, desc, preco])

    escolha = int(input("Deseja adicionar mais um produto? Sim [1] | Não [2]: "))
    if escolha == 2:
        terminou = True

for item in produto:
    print(f"Id: {item[0]}, Descrição do produto: {item[1]}, Preço do produto: {item[2]}")
