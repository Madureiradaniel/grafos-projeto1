from lista import Lista
from bfs import Bfs

class Service(object):

    def transformaVetor(self,vetor,capital):

        lista = Lista(len(vetor))
        for i in range(len(vetor)):
            if vetor[i] != i:
                lista.addAresta(vetor[i],i)

        print("\n Lista de Adjacencia Gerada A partir do Vetor")
        lista.mostraLista()

        distancias = Bfs(lista.getLista(),capital)

        return distancias.get_distancias()

    def verificaCapital(self,vetor):

        count = 0
        capital =-1

        for i in range(len(vetor)):
            if vetor[i] == i:
                count += 1
                capital = i

        if count == 1:
            print(str(capital) + " E a capital !")
            return capital
        elif count > 1:
            print("Seu array possui mais de uma capital, insira um array valido com apenas uma capital \n")
            return False
        elif count == 0:
            print("Seu array nao possui uma capital, insira um array valido com uma capital \n")
            return False

    def traduzVetor(self,vetorDistancia):

        for i in range(len(vetorDistancia)):

            if vetorDistancia[i] !=0 :
                print("Existe " + str(vetorDistancia[i]) + " cidade(s)" + " a " + str(i+1) + " distancia(s) da capital!\n")
