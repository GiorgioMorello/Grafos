import numpy as np


class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0  
        self.fim = -1 
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=object)

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade



    def enfileirar(self, valor):
        if not self.fila_cheia():

            if self.capacidade == self.fim + 1:
                self.fim = -1
            self.fim += 1
            self.valores[self.fim] = valor
            self.numero_elementos += 1
        else:
            print('Fila cheia')

    def desenfileirar(self):
        if self.fila_vazia():
            print('Fila vazia')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1  
        if self.inicio == self.capacidade:  
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1

        return self.valores[self.inicio]

    def imprimir_fila(self):
        if self.fila_vazia():
            print('Fila vazia')
            return

        for i in range(self.fim + 1):
            print(self.valores[i].rotulo)







class Pilha:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def pilha_cheia(self):
        if self.capacidade == self.topo + 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if not self.pilha_cheia():
            self.topo += 1
            self.valores[self.topo] = valor
            return

        print('Pilha cheia')

    def desempilhar(self):
        if self.pilha_vazia():
            pass

        else:
            temp = self.valores[self.topo]
            self.topo -= 1
            return temp

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1






class VetorOrdenado:

    def __init__(self, capacidade, is_greedy_search=False):
        self.capacidade = capacidade
        self.ultima_pos = -1
        self.valores = np.empty(self.capacidade, dtype=object)
        self.is_greedt_search = is_greedy_search


    def listar_valores(self):
        if self.ultima_pos == -1:
            print('Vetor vazio')

        else:
            for i in range(self.ultima_pos + 1):
                print(i, '--', self.valores[i].rotulo)


    def inserir_valor(self, valor):
        if self.capacidade == self.ultima_pos + 1:
            print('Vetor cheio')
            return

        posicao = 0
        for i in range(self.ultima_pos + 1):
            posicao = i

            if self.is_greedt_search:
                if self.valores[i].custo_total > valor.custo_total:
                    break

            else:

                if self.valores[i].distancia_objetivo > valor.distancia_objetivo:
                    break

            if posicao == self.ultima_pos:
                posicao += 1

        x = self.ultima_pos


        while x >= posicao:

            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_pos += 1
