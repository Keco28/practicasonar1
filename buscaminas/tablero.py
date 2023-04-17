from pieza import Pieza
import random
from matEnTripletas import MatEnTripletas
from tripleta import Tripleta

"""Clase en la que se va a manejar el tablero en representación como 
   matriz en tripletas"""
class Tablero():
        def __init__(self, tamaño, minas):
            self.tamaño = tamaño            #Tamaño del tablero ingresado como una tupla
            self.minas = minas              #Número de minas en el tablero
            self.lost = False               #Atributo de perder
            self.ganar = False              #Atributo de ganar
            self.numClicked = 0             #Variable controladora del número casillas seleccionadas
            self.numNoBombs = 0             #Variable en donde se guarda el número de casillas en las que no hay bombas
            self.setTablero()

        def setTablero(self):
            self.numNoBombs = self.tamaño[0]*self.tamaño[1] - self.minas   #El número de casillas en las cuales no hay minas es igual a las dimensiones de la matriz menos el numero de bombas
            self.tablero = MatEnTripletas(self.tamaño[0], self.tamaño[1], self.minas)
            aux = []
            aux1 = []
            while True:         #While que genera de manera aleatoria las minas en el tablero
                a = (random.randint(0, self.tamaño[0] - 1), random.randint(0, self.tamaño[1] - 1))
                if(str(a) in aux): continue
                aux.append(str(a))
                aux1.append(a)
                if(len(aux) == self.minas):
                    break
            #print(aux)
            for fila in range(self.tamaño[0]):      #For que revisa cada posición del tablero para revisar en dónde hay una mina
                cont1 = fila
                for col in range(self.tamaño[1]):
                    tieneBomba = False
                    b = str((cont1, col))
                    if(b in aux):                   #Si la posición en la que se encuentra el ciclo coincide con alguna de las posiciones
                        tieneBomba = True           #en las que hay una bomba, el atributo tieneBomba es True, Flase de lo contrario
                    ficha = Pieza(tieneBomba)
                    tripleta = Tripleta(fila, col, ficha)
                    self.tablero.agrega_tripleta(tripleta)
            self.setVecinos()

        def setVecinos(self):           #método buscar el número de bombas alrededor de las piezas en el tablero
            for fila in range(self.tamaño[0]):
                for col in range(self.tamaño[1]):   #Recorremos pieza por pieza buscando el número de bombas alrededor
                    pieza = self.getPieza((fila, col))
                    vecinos = self.getListaDeVecinos((fila, col))
                    pieza.setVecinos(vecinos)       #Método seTVecinos de la clase pieza para contar el número de bombas alrededor

        def getListaDeVecinos(self, index): #Recorre pieza por pieza revisando cuales son las casillas que la rodean
            vecinos = []
            for fila in range(index[0] - 1, index[0] + 2):
                for col in range(index[1] - 1, index[1] + 2):
                    outOfBounds = fila < 0 or fila >= self.tamaño[0] or col < 0 or col >= self.tamaño[1]
                    igual = fila == index[0] and col == index[1]
                    if(igual or outOfBounds):
                        continue
                    vecinos.append(self.getPieza((fila, col)))
            return vecinos


        def getTamaño(self):
            return self.tamaño

        def getPieza(self, index):
            return self.tablero.retorna_tripleta(index[0], index[1]).get_value()

        def handleClick(self, pieza, flag):         #Método para revisar una pieza seleccionada
            if(pieza.getClicked() or (not flag and pieza.getFlagged())): #Si la pieza ya fue tocada o está señalada con una bandera no hace nada
                return
            if(flag):       #Si la pieza tiene una bandera, la quita
                pieza.toggleFlag()
                return
            pieza.click()
            if(pieza.getTieneBomba()): #Si la pieza tiene una bomba, pierde
                self.lost = True
                return
            self.numClicked += 1
            if(pieza.getNumAlr() != 0): #Si la pieza TIENE una bomba alrededor sale del método
                return
            for vecino in pieza.getVecinos():   #Si la pieza NO TIENE una bomba alrededor  entra de manera recursiva en sus vecinos hasta dar con las piezas que tienen bombas alrededor
                if(not vecino.getTieneBomba() and not vecino.getClicked()):
                    self.handleClick(vecino, False)

        def getLost(self):
            return self.lost

        def getGanar(self):
            return self.numNoBombs == self.numClicked
