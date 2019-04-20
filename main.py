from lista import Lista
from bfs import Bfs

grafo = Lista(12)

grafo.addAresta(1,9)
grafo.addAresta(9,3)
grafo.addAresta(9,7)
grafo.addAresta(9,0)
grafo.addAresta(0,8)
grafo.addAresta(8,6)
grafo.addAresta(0,4)
grafo.addAresta(4,5)
grafo.addAresta(4,2)
grafo.addAresta(1,10)
grafo.addAresta(10,11)


vetor = Bfs(grafo.getLista(),1)
grafo.mostraLista()
print("\n")
vetor.get_distancias()