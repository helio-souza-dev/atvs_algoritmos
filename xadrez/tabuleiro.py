from Pecas import Peao, Torre, Cavalo, Bispo, Rei, Rainha
import tkinter as tk

root = tk.Tk()
root.title("Tabuleiro de Xadrez")

# Tamanho de cada casa em pixels
tamanho_casa = 60

meu_peao = Peao("A2", "Branco")

for linha in range(8):
    for coluna in range(8):
        # Lógica para alternar as cores: 
        # Se a soma da linha + coluna for par, a cor é clara; se ímpar, escura.
        cor = "#eeeed2" if (linha + coluna) % 2 == 0 else "#769656"
        
        casa = tk.Frame(root, width=tamanho_casa, height=tamanho_casa, bg=cor)
        casa.grid(row=linha, column=coluna)
        
def setup():
    # Cria a matriz 8x8 vazia
    tabuleiro = [[None for _ in range(8)] for _ in range(8)]
    ordem_pecas = [Torre, Cavalo, Bispo, Rainha, Rei, Bispo, Cavalo, Torre]
    
    for i in range(8):
        # 1. Instancia as peças (Brancas na linha 7, Pretas na linha 0)
        # Passamos a posição no formato (linha, coluna)
        tabuleiro[0][i] = ordem_pecas[i]((0, i), "preto")
        tabuleiro[1][i] = Peao((1, i), "preto")
        
        tabuleiro[6][i] = Peao((6, i), "branco")
        tabuleiro[7][i] = ordem_pecas[i]((7, i), "branco")
    
    return tabuleiro

# Chama o setup para ter os objetos das peças
meu_tabuleiro = setup()
root.mainloop()
