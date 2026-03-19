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
        
def setup()

root.mainloop()
