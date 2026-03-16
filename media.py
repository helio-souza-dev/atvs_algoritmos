numeros = []

while True:
    n = int(input("Digite um numero: "))
    numeros.append(n)

    resp = int(input("Quer mais um numero? Sim[1] | Não[2]: "))

    if resp == 2:
        break

soma = 0
for n in numeros:
    soma += n

media = soma / len(numeros)

print("Números:", numeros)
print("Media:", media)