from constantes import Constantes
from posicao import Posicao

class Grid:

    def __init__(self, linhas_arr, segundos):
        self.total_segundos = segundos
        self.segundo_atual = 1

        self.posicoes = [[None for j in range(len(linhas_arr[0]))] for i in range(len(linhas_arr))]
        self.bombas = []
        self.__determinar_posicoes(linhas_arr)

        print('')
        print('Segundo 0')
        print(self)

    def __determinar_posicoes(self, linhas_arr):
        for l, linha in enumerate(linhas_arr):
            for c, celula in enumerate(linha):
                posicao = Posicao(l, c, celula, 0)
                self.posicoes[l][c] = posicao
                if (celula == Constantes.BOMBA): 
                    self.bombas.append(posicao)
    
    def passar_segundos(self, num_segundos):
        for i in range(num_segundos):
            self.passar_segundo()
  
    def passar_segundo(self):
        for bomba in self.bombas:
            if (bomba.momento_criacao + 3 == self.segundo_atual):
                self.explodir(bomba)
        
        if (self.segundo_atual % 2 == 0 and self.segundo_atual >= 2):
            self.implantar_bombas()

        print('')
        print('Segundo ' + str(self.segundo_atual))
        print(self)

        self.segundo_atual += 1

    def explodir(self, bomba):
        # Explodindo de posicao atual ate direita
        for c in range(bomba.coluna, len(self.posicoes[bomba.linha])):
            posicao = self.posicoes[bomba.linha][c]
            if (posicao.tipo != Constantes.OBSTACULO):
                posicao.explodir()
            else: break

        # Explodindo de posicao atual ate esquerda
        for c in range(bomba.coluna, -1, -1):
            posicao = self.posicoes[bomba.linha][c]
            if (posicao.tipo != Constantes.OBSTACULO):
                posicao.explodir()
            else: break

        # Explodindo de posicao atual ate topo
        for l in range(bomba.linha, len(self.posicoes)):
            posicao = self.posicoes[l][bomba.coluna]
            if (posicao.tipo != Constantes.OBSTACULO):
                posicao.explodir()
            else: break

        # Explodindo de posicao atual ate topo
        for l in range(bomba.linha, -1, -1):
            posicao = self.posicoes[l][bomba.coluna]
            if (posicao.tipo != Constantes.OBSTACULO):
                posicao.explodir()
            else: break
        
        bomba.explodir()

    def implantar_bombas(self):
        for l, linha in enumerate(self.posicoes):
            for c, celula in enumerate(linha):
                if (self.posicoes[l][c].tipo == Constantes.VAZIO):
                    posicao = Posicao(l, c, Constantes.BOMBA, self.segundo_atual)
                    self.posicoes[l][c] = posicao
                    self.bombas.append(posicao)

    def __str__(self):
        str = ''
        for linha in self.posicoes:
            str += ''
            for celula in linha:
                str += celula.tipo
            str += '\n'
        return str
        