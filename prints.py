# end= (define o que vai ter no final do print)
print()
print("exemplo com end")
print("oi", end=" ")
print("helio")

#sep define oq vai ficar entre os argumentos
print()
print("exemplo com com sep")
print("teste2", "teste3", sep="-")

#{} vc pode usar argumentos dentro do .format() em sequencia da string dentro dos argumentos do print para preencher os {}
nome = "helio"
idade = 6
print()
print("exemplo com .format")
print("olá {} voce foi aprovado com {}".format(nome, idade))


#print(f"") (f-strings) permite vc usar variaveis dentro da propria string dentro do argumento do print
print()
print("exemplo com f")
print(f"olá {nome}")

# usando % como o .format
# %s é para strings %d para inteiros
#ele executa na ordem dos argumentos (n1, n2, i1, i2)...
nome2 = "ronaldo"
print()
print("exemplo com %")
print("olá %s e %s voce tem %d" % (nome, nome2, idade))

#combinando sep, end, f-string
print()
print(f"olá {nome}", "sol", end=" ", sep="-")

print()
print("olá {}, voce tem {}".format(nome, idade), "sete anos", sep="-")
#
print()


# formatacao de casas decimais

decimal = 3.14159265359

#o f-decimal pode ser seguido de numeros para indicar alguns metodos
# numero:.0f = arredonda para o inteiro mais próximo
# numero:.1f ao infinito limita o numero de casas decimais a serem retornadas

#sintaxe basica: print(f"(string) {(numero decimal):.(numero inteiro de casas decimais)f}")

print(f"o decimal {decimal:.12f} arredondado é igual a: {decimal:.0f}")
print()

decimais = [3.14, 1.25, 1.35, 1.55]

for i in range(len(decimais)):
    print(f"o decimal {decimais[i]} posicao na lista {i + 1} arredondado é {decimais[i]:.0f}")
    

