from grafo import Grafo
from estrutura_dados import Pilha


g = Grafo()




class BuscaProfundidade:

    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(self.inicio)


    def buscar(self):
        topo = self.pilha.ver_topo()
        print(f'topo: {topo.rotulo}')

        for adj in topo.adjacentes:
            if not adj.vertice.visitado:
                print(f'Empilhou: {adj.vertice.rotulo}')
                self.pilha.empilhar(adj.vertice)
                adj.vertice.visitado = True
                self.buscar()
        print(f'Desempilhou: {self.pilha.desempilhar().rotulo}')



bf = BuscaProfundidade(g.arad)

bf.buscar()