from fila import Fila

class Bfs(object):


    def __init__(self,grafo,vertice):

        fila = Fila()
        #lista para auxiliar a calcular as distancias
        auxDist = []
        for i in range(len(grafo)):
            auxDist.append([])

        cont = 1
        self.vetor_distancias = ([0]*len(grafo))
        self.vetor_visitacao = ([-1]*len(grafo))

        fila.QEUEput(vertice)
        auxDist[0].append(vertice)
        self.vetor_visitacao[vertice]=cont

        cont+=1
        distancia=0

        while fila.QEUEempty() != 0:
            v = fila.QEUEget()

            for i in grafo[v]:
                if self.vetor_visitacao[i] == -1:
                    self.vetor_visitacao[i] = cont
                    cont = cont + 1

                    if len(grafo[i]) > 0:
                        #so insiro na fila caso o vertice visitado tenha um caminho para outro vertice
                        # e se algo for inserido na fila a distancia aumenta
                        fila.QEUEput(i)
                        auxDist[distancia+1].append(i)

            distancia += 1 # para cada pulo uma distancia

            print("\n Distancia " + str(distancia) + " cidades " + str(len(grafo[v])) + " Fila-> " + str(fila))

        print("\n" + str(auxDist))

        #mantem na lista de distancia apenas as listas nao nulas
        auxDist2 = []
        for i in auxDist:
            if len(i) != 0:
               auxDist2.append(i)

        print("\n" + str(auxDist2))

        #soma a quantidade de cidades por cada distancia
        cont = 0
        for i in auxDist:
            soma =0
            for j in i:
                soma = soma + len(grafo[j])
            self.vetor_distancias[cont] = soma
            cont +=1


        fila.QEUEfree()

    def get_distancias(self):

        return print(str(self.vetor_visitacao) + "\n\n" + str(self.vetor_distancias))

