class Peca:
    
    def __init__(self, casa_padrao, cor):
        self.tipo = self.__class__.__name__
        self.casa_padrao = casa_padrao
        self.cor = cor
    
    def __str__(self):
        return f"{self.tipo} {self.cor} em {self.posicao_atual}"
    
    def getSimbolo(self):
        return "?"
    
class Peao(Peca):
    
    def posicoes_possiveis(self):
        
        return []
    
    def getSimbolo(self):
        return "♙" if self.cor == "branco" else "♟"
        
class Torre(Peca):
    
    def posicoes_possiveis(self):
        
        return []
    
    def getSimbolo(self):
        return "♖" if self.cor == "branco" else "♜"

class Cavalo(Peca):
    
    def posicoes_possiveis(self):
        
        return []
    
    def getSimbolo(self):
        return "♘" if self.cor == "branco" else "♞"
    
class Bispo(Peca):
    
    def posicoes_possiveis(self):
        
        return []
    
    def getSimbolo(self):
        return "♗" if self.cor == "branco" else "♝"
    
class Rainha(Peca):
    
    def posicoes_possiveis(self):
        
        return []
    
    def getSimbolo(self):
        return "♕" if self.cor == "branco" else "♛"

class Rei(Peca):
    
    def posicoes_possiveis(self):
        
        return []
    
    def getSimbolo(self):
        return "♔" if self.cor == "branco" else "♚"