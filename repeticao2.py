gatos = ["perola", "neto"]

#exemplo sort
gatos.sort(reverse=True)
print(gatos)

#exemplo count()
frutas = ["maca", "banana", "maca"]

bananas_contadas = frutas.count("banana")
print(f"\no numero de bananas em {frutas} é {bananas_contadas}")

#exemplo do index()
indice_gato = gatos.index("perola")
print(f"\na posição do gato {gatos[0]} na lista é {indice_gato + 1}")

#reverse()

gatos2 = ["gato", "gata"]
gatos2.reverse()
print(f"a lista de gatos ao inverso é {gatos2}")
# só altera a lista original, não retorna nada.

# union e intersection, difference
a = {1, 2, 3}
b = {1, 4, 6}

# só funciona em conjuntos {}

#uniao
uniao = a | b # | = .union()
uniao2 = a.union(b) # una os dois conjuntos
print(uniao)
print(uniao2) 

#intersecçao
interseccao = a & b # & = .intersection()
interseccao2 = a.intersection(b) # o que tem no a e tem no b
print(interseccao)
print(interseccao2)

#diferenca

diferenca = a - b # - = .difference()
diferenca2 = a.difference(b) # o que tem no a que não tem no b
print(diferenca)
print(diferenca2)

