from services import  Service

def main():
    op=-1
    while op !=0:

        print("Escolha uma opçao: \n")
        print("1  - Entrar com o valores atraves de um arquivo '.txt' : \n")
        print("2 - Entrar com os valores a partir do terminal: \n")
        print("3 - para sair digite 0: \n")
        op = int(input(""))

        if op == 1:
            print("-------------------------------------------------------------------")
            #ler os numeros atraves do arquivo .txt
            #caso queira mudar, basta alterar o arquivo
            arq = open('./vetor.txt')
            numeros = arq.read()
            arq.close()
            vetor = list(map(int, numeros.split(",")))
            print("Vetor de Entrada -> " + str(vetor))
            grafo = Service()
            capital = grafo.verificaCapital(vetor)

            if capital != False:
                vetorDistancias = grafo.transformaVetor(vetor, capital)
                print("\nvetor de Distancias -> " + str(vetorDistancias) + "\n")
                grafo.traduzVetor(vetorDistancias)
            print("\n")

            print("-------------------------------------------------------------------")


        elif op == 2:
            print("-------------------------------------------------------------------")

            numeros  = input("Digite uma sequencia de numeros no seguinte padrão: 'x,y,z,.., w,' :\n ")
            vetor = list(map(int,numeros.split(",")))
            grafo = Service()
            print("\nVetor de Entrada-> " + str(vetor) + "\n")
            capital = grafo.verificaCapital(vetor)

            if capital != False:
                vetorDistancias = grafo.transformaVetor(vetor,capital)
                print("vetor de Distancias -> " + str(vetorDistancias))
                grafo.traduzVetor(vetorDistancias)
            print("\n")
            print("-------------------------------------------------------------------")

        elif op == 0:
            print("Exit\n")
            op=0
        else:
            print("Digite uma opcao valida\n")

if __name__=='__main__':
    main()