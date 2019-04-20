class Lista(object):

    def __init__(self,vertices):

        self.__lista = []

        for i in range(vertices):
            self.__lista.append([])


    def addAresta(self,v,w):

        # verifica se a aresta ja foi adicionada, para nao adicionar 2x
        # coloca os vizinhos em ordem crescente para cada vertice
        if w not in self.__lista[v]:
            self.__lista[v].append(w)
            self.__lista[v].sort()

    def mostraLista(self):

        j = 0
        for i in self.__lista:
            print(str(j) + " -> " + str(i))
            j = j + 1

    def getLista(self):
        return self.__lista

