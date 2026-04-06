# 16. Buscar contato e mostrar dados
# Escreva um código que:
# Solicite um nome ao usuário 
# Procure esse nome na agenda 
# Se encontrar, mostre todos os dados 
# Caso contrário, informe "Contato não encontrado" 


usuarios = [
    {"nome": "helio", "senha": 123, "id_user": 1},
    {"nome": "resenha", "senha": 1234, "id_user": 2}
]

dados_usuarios = [
    {"cpf": "xxx.xxx.xxx-xx", "telefone": "xx.xxxx.xxxx", "id": {"id_user"}},
    {"cpf": "xxx.xxx.xxx-xx", "telefone": "xx.xxxx.xxxx", "id": {"id_user"}}
]

sessao = False

terminou = False

while not terminou:
    nome = input("Digite o seu nome: ")
    senha = input("Digite sua senha: ")
    
    for usuario in usuarios:
        if usuario["nome"] == nome:
            if senha["senha"] == senha:
                print("Acesso liberado")
                sessao = True
                print(usuario)
            else:
                print("Senha errada tente novamente")
                continue
            