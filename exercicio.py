dados = []

def ver_lista():
    opt = int(input("deseja ver a lista? Sim[1] Não[2]"))
    if opt == 1:
        print(f"A lista de dados: {dados}")
    elif opt ==2:
        return
        
while True:
    print("Cadastro")
    nome = input("Digite seu nome: ")
    dados.append(nome)
    
    email = input("Digite seu email: ")
    dados.append(email)
    
    telefone = int(input("Digite seu numero: "))
    dados.append(telefone)
    
    print("\nDeseja adicionar mais nomes a lista?")
    escolha = int(input("Sim [1] Não [2]"))
    if escolha == 1:
        continue
    elif escolha == 2:
        ver_lista()
        break
    
