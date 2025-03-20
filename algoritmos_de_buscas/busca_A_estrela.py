from estrutura_dados import VetorOrdenado
from grafo import Grafo

class BuscaAEstrela:

    def __init__(self, objetivo):
        self.objetivo = objetivo

    def buscar(self, inicio):
        if inicio is self.objetivo:
            print(f'Objetivo encontrado: {inicio.rotulo}')

        else:
            print(inicio.rotulo)
            inicio.visitado = True
            v = VetorOrdenado(len(inicio.adjacentes), is_greedy_search=True)

            for adj in inicio.adjacentes:
                if not adj.vertice.visitado:
                    adj.vertice.visitado = True
                    adj.vertice.custo_total = adj.custo + adj.vertice.distancia_objetivo
                    print(adj.vertice.custo_total)
                    v.inserir_valor(adj.vertice)

            print("")

            if v.valores[0] != None:
                self.buscar(v.valores[0])




g = Grafo()

bg = BuscaAEstrela(g.bucharest)
bg.buscar(g.arad)