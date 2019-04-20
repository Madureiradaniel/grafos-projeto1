class Fila(object):

    def __init__(self):

        self.dados = []

    def __str__(self):

        return "%s" % (self.dados)

    def QEUEput(self, elemento):

        self.dados.append(elemento)

    def QEUEget(self):

        return self.dados.pop(0)

    def QEUEfree(self):

        del self.dados[:]
        del self.dados

    def QEUEempty(self):

        if len(self.dados) == 0:
            return 0