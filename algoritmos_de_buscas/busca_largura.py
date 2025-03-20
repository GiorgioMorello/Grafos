from grafo import Adjacente, Grafo
from estrutura_dados import FilaCircular, Pilha





class BuscaLargura:

    def __init__(self, inicio):
        self.fila = FilaCircular(20)
        self.inicio = inicio
        self.inicio.visitado = True
        self.fila.enfileirar(inicio)



    def buscar(self):
        primeiro = self.fila.primeiro()

        if primeiro == -1:
            return

        print(f'Primeiro valor da fila: {primeiro.rotulo}')
        for adj in primeiro.adjacentes:
            print(adj.vertice.rotulo)
            if not adj.vertice.visitado:

                adj.vertice.visitado = True
                self.fila.enfileirar(adj.vertice)
        print()
        self.fila.desenfileirar()
        self.buscar()


g = Grafo()

bl = BuscaLargura(g.arad)
bl.buscar()






