from fila import Fila

class Bfs(object):


    def __init__(self,grafo,vertice):

        self.fila = Fila()

        self.auxDist = []
        for i in range(len(grafo)):
            self.auxDist.append([])

        cont = 1
        self.vetor_distancias = ([0]*len(grafo))
        self.vetor_visitacao = ([-1]*len(grafo))

        self.fila.QEUEput(vertice)
        self.auxDist[0].append(vertice)
        self.vetor_visitacao[vertice]=cont

        cont+=1
        distancia=0

        while self.fila.QEUEempty() != 0:
            v = self.fila.QEUEget()

            for i in grafo[v]:
                if self.vetor_visitacao[i] == -1:
                    self.vetor_visitacao[i] = cont
                    cont = cont + 1

                    if len(grafo[i]) > 0:
                        #so insiro na fila caso o vertice visitado tenha um caminho para outro vertice
                        # e se algo for inserido na fila a distancia aumenta
                        self.fila.QEUEput(i)
                        self.auxDist[distancia+1].append(i)
            distancia += 1




            print("\n Distancia " + str(distancia) + " cidades " + str(len(grafo[v])) + " Fila-> " + str(self.fila))

        print("\n" + str(self.auxDist))

        cont = 0
        for i in self.auxDist:
            soma =0
            for j in i:
                soma = soma + len(grafo[j])
            self.vetor_distancias[cont] = soma
            cont +=1


        self.fila.QEUEfree()

    def get_distancias(self):

        return print(str(self.vetor_visitacao) + "\n\n" + str(self.vetor_distancias))

