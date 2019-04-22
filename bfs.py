from fila import Fila

class Bfs(object):


    def __init__(self,grafo,vertice):

        fila = Fila()

        #lista para guardar os vertices por distancia
        auxDist = []
        for i in range(len(grafo)):
            auxDist.append([])

        cont = 1
        self.__vetor_distancias = ([0]*len(grafo))
        self.__vetor_visitacao = ([-1]*len(grafo))

        fila.QEUEput(vertice)
        fila.QEUEput(-1) # separa a fila por camada

        self.__vetor_visitacao[vertice] = cont

        cont+=1
        distancia=0

        while fila.QEUEempty() != 0:
            v = fila.QEUEget()

            #se o v for igual a -1 significa que e o fim da fila
            if v != -1:
                camada = fila.QEUEget()

                #aumenta a distancia caso a camada = -1,
                aux=distancia
                if camada == -1:
                    distancia += 1
                else:
                    #se a camada nao for igual a -1, ela e inserida novamente no inicio da fila,
                    # pois se trata de um vertice
                    fila.addInicioDaFila(camada)

                #preenche o vetor de visitaçao
                for i in grafo[v]:
                    if self.__vetor_visitacao[i] == -1:
                        self.__vetor_visitacao[i] = cont
                        cont = cont + 1
                        fila.QEUEput(i)

                #verifico se minha distancia mudou
                #caso a distancia tenha mudado, insiro meus vertices pertencentes a distancia
                if aux !=distancia:
                    auxDist[distancia] = (fila.getFila())
                    fila.QEUEput(-1) # insiro no fim da fila para identificar que e outra camada


        #mantem na lista de distancia apenas, as listas nao nulas
        auxDist2 = []
        for i in auxDist:
            if len(i) != 0:
               auxDist2.append(i)

        #soma a quantidade de cidades por cada distancia
        cont = 0
        for i in auxDist2:
            soma =0
            for j in i:
                soma +=1
            self.__vetor_distancias[cont] = soma
            cont +=1

        fila.QEUEfree()

    def get_distancias(self):

        return self.__vetor_distancias

