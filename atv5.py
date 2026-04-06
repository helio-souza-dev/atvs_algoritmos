#ler dois produtos
#armazenar em uma lista
#exiba os dados de dois produtos

produto1 = []
produto2 = []
produtos = [produto1, produto2]


terminou = False


nome_prod1 = input("Digite o nome do primeiro produto: ")
preco_prod1 = int(input("Digite o preço do primeiro produto "))



nome_prod2 = input("Digite o nome do primeiro produto: ")
preco_prod2 = int(input("Digite o preço do segundo produto "))

produto1.append([nome_prod1, preco_prod1])
produto2.append([nome_prod2, preco_prod2]) 

for item in produtos:
    print(item)
    