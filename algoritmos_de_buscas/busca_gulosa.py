from estrutura_dados import VetorOrdenado
from grafo import Grafo

class BuscaGulosa:

    def __init__(self, objetivo):
        self.objetivo = objetivo

    def buscar(self, atual):
        print(atual.rotulo)
        if atual is self.objetivo:
            print('Valor encontrado')

        else:
            vetor = VetorOrdenado(len(atual.adjacentes))
            for adj in atual.adjacentes:

                print(f"Adjacente: {adj.vertice.rotulo} - {adj.vertice.distancia_objetivo}")
                if not adj.vertice.visitado:
                    adj.vertice.visitado = True
                    vetor.inserir_valor(adj.vertice)

            print("")
            if vetor.valores[0] != None:
                self.buscar(vetor.valores[0])


g = Grafo()

bg = BuscaGulosa(g.bucharest)

bg.buscar(g.arad)