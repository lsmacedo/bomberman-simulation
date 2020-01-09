from constantes import Constantes

class Posicao:

    def __init__(self, linha, coluna, tipo, momento_criacao = None):
        self.linha = linha
        self.coluna = coluna
        self.tipo = tipo
        self.momento_criacao = momento_criacao

    def explodir(self):
        if (self.tipo != Constantes.OBSTACULO):
            self.tipo = Constantes.VAZIO