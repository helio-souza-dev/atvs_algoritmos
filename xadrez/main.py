# main.py

import tkinter as tk
from Pecas import Peao, Torre, Cavalo, Bispo, Rainha, Rei # Importa suas classes de peça

class XadrezApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Xadrez Drag & Drop")
        self.tamanho_casa = 60
        self.tamanho_tabuleiro = 8 * self.tamanho_casa

        # --- 1. Estado do Arrasto (Nossa "Memória") ---
        self.peca_arrastada = None  # Objeto da peça (ex: o Peao)
        self.item_canvas_arrastado = None # ID do texto/imagem no Canvas
        self.linha_origem = None
        self.coluna_origem = None

        # --- 2. Lógica do Tabuleiro (A Matriz) ---
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pecas()

        # --- 3. Interface Gráfica (O Canvas) ---
        # Criamos o Canvas onde tudo será desenhado
        self.canvas = tk.Canvas(root, width=self.tamanho_tabuleiro, height=self.tamanho_tabuleiro)
        self.canvas.pack()

        # Desenha o fundo (quadrados) e as peças nas posições iniciais
        self.desenhar_tabuleiro()
        self.desenhar_pecas()

        # --- 4. Vincular Eventos do Mouse ao Canvas ---
        # <Button-1>: Clique com o botão esquerdo (Começar a arrastar)
        self.canvas.bind("<Button-1>", self.ao_clicar)
        # <B1-Motion>: Mover o mouse segurando o botão esquerdo (Arrastar)
        self.canvas.bind("<B1-Motion>", self.ao_arrastar)
        # <ButtonRelease-1>: Soltar o botão esquerdo (Largar a peça)
        self.canvas.bind("<ButtonRelease-1>", self.ao_soltar)

    def setup_pecas(self):
        # Coloca as peças nas posições iniciais na matriz lógica
        ordem_pecas = [Torre, Cavalo, Bispo, Rainha, Rei, Bispo, Cavalo, Torre]
        for i in range(8):
            self.tabuleiro[0][i] = ordem_pecas[i]((0, i), "preto")
            self.tabuleiro[1][i] = Peao((1, i), "preto")
            self.tabuleiro[6][i] = Peao((6, i), "branco")
            self.tabuleiro[7][i] = ordem_pecas[i]((7, i), "branco")

    def desenhar_tabuleiro(self):
        # Desenha apenas os quadrados de fundo (estáticos)
        for linha in range(8):
            for coluna in range(8):
                cor = "#eeeed2" if (linha + coluna) % 2 == 0 else "#769656"
                x1 = coluna * self.tamanho_casa
                y1 = linha * self.tamanho_casa
                x2 = x1 + self.tamanho_casa
                y2 = y1 + self.tamanho_casa
                # Desenha um retângulo no Canvas
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="")

    def desenhar_pecas(self):
        # Limpa todas as peças fixas do Canvas antes de redesenhar
        self.canvas.delete("peca") 

        for linha in range(8):
            for coluna in range(8):
                peca = self.tabuleiro[linha][coluna]
                if peca:
                    x = (coluna * self.tamanho_casa) + (self.tamanho_casa // 2)
                    y = (linha * self.tamanho_casa) + (self.tamanho_casa // 2)
                    cor_texto = "white" if peca.cor == "branco" else "black"
                    
                    # Cria o texto Unicode no Canvas e dá a tag "peca" para podermos deletar depois
                    self.canvas.create_text(x, y, text=peca.getSimbolo(), font=("Arial", 30), fill=cor_texto, tags="peca")

    # --- LÓGICA DO MOUSE ---

    def ao_clicar(self, event):
        # 1. Converte (x, y) do clique para linha/coluna
        coluna = event.x // self.tamanho_casa
        linha = event.y // self.tamanho_casa

        # 2. Pega a peça na matriz lógica
        peca = self.tabuleiro[linha][coluna]

        if peca:
            # 3. Inicia o estado de arrasto
            self.peca_arrastada = peca
            self.linha_origem = linha
            self.coluna_origem = coluna
            
            # Remove temporariamente a peça da matriz lógica (está na mão)
            self.tabuleiro[linha][coluna] = None
            
            # Redesenha o tabuleiro para que a casa de origem fique vazia
            self.desenhar_pecas()

            # 4. Cria a peça de arrasto (que segue o mouse) no Canvas
            cor_texto = "white" if peca.cor == "branco" else "black"
            self.item_canvas_arrastado = self.canvas.create_text(
                event.x, event.y, # Começa exatamente onde clicou
                text=peca.getSimbolo(), font=("Arial", 35), # Um pouco maior para destacar
                fill=cor_texto, tags="arrasto"
            )

    def ao_arrastar(self, event):
        if self.peca_arrastada:
            # Move o item do Canvas para a nova posição do mouse
            # event.x e event.y são as coordenadas atuais do mouse
            self.canvas.coords(self.item_canvas_arrastado, event.x, event.y)

    def ao_soltar(self, event):
        if self.peca_arrastada:
            # 1. Converte (x, y) final para linha/coluna de destino
            coluna_destino = event.x // self.tamanho_casa
            linha_destino = event.y // self.tamanho_casa

            # 2. Garante que soltou dentro do tabuleiro (opcional mas boa prática)
            if 0 <= linha_destino < 8 and 0 <= coluna_destino < 8:
                # *Aqui entrará a validação da regra de movimento no futuro*
                # Por enquanto, aceita qualquer lugar

                # 3. Move a peça para o destino na matriz lógica
                self.tabuleiro[linha_destino][coluna_destino] = self.peca_arrastada
            
            else:
                # Soltou fora, devolve para a origem
                self.tabuleiro[self.linha_origem][self.coluna_origem] = self.peca_arrastada

            # 4. Limpa o estado de arrasto
            self.canvas.delete(self.item_canvas_arrastado) # Remove peça temporária
            self.peca_arrastada = None
            self.item_canvas_arrastado = None
            
            # 5. Redesenha as peças fixas nas novas posições
            self.desenhar_pecas()

if __name__ == "__main__":
    root = tk.Tk()
    app = XadrezApp(root)
    root.mainloop()