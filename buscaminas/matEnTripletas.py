from tripleta import Tripleta

class MatEnTripletas():

    """Constructor dónde definimos una lista donde
        guardaremos las tripletas"""
    def __init__(self, fila, col, value):
        self.lista = []
        tripleta = Tripleta(fila, col, value)
        self.lista.append(tripleta)

    def numero_filas(self):
        return self.lista[0].get_fila()

    def numero_col(self):
        return self.lista[0].get_col()

    def numero_values(self):
        return self.lista[0].get_value()

    def asigna_tripleta(self, tripleta, k):
        self.lista[k] = tripleta

    def retorna_num_tripleta(self):
        return self.lista[0].get_value()

    def retorna_tripleta(self, k):
        return self.lista[k]

    def retorna_tripleta(self, fila, col):
        for i in range(1, len(self.lista)):
            if(fila == self.lista[i].get_fila() and col == self.lista[i].get_col()):
                return self.lista[i]

    def asigna_numero_tripletas(self, k):
        self.lista[0].set_value(k)

    def muestra_matriz(self):
        aux = self.lista
        for i in range(1, len(self.lista)):
            print(aux[i].get_fila(), aux[i].get_col(), aux[i].get_value())

    def inserta_tripleta(self, tripleta):
        tx = self.retorna_tripleta(0)
        p = tx.get_value()
        i = 1
        t = self.retorna_tripleta(i)
        while ( i <= p and t.get_fila() < tripleta.get_fila()):
            i += 1
            t = self.retorna_tripleta(i)
        while (i <= p and t.get_fila() == tripleta.get_fila()
        and t.get_col() < tripleta.get_col()):
            i += 1
            t = self.retorna_tripleta(i)
        p = p + 1
        self.lista.insert(i, tripleta)
        self.asigna_numero_tripletas(p)

    def agrega_tripleta(self, tripleta):
        self.lista.append(tripleta)
