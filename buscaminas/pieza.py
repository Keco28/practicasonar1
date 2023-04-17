class Pieza():
    def __init__(self, tieneBomba):
        self.tieneBomba = tieneBomba
        self.clicked = False
        self.flagged = False

    def getTieneBomba(self):                #Método para revisar si la pieza tiene bomba
        return self.tieneBomba

    def getClicked(self):                   #Método para revisar si la pieza ya fue clickeada
        return self.clicked

    def getFlagged(self):                   #Método para revisar si la pieza fue marcada con una bandera
        return self.flagged

    def setVecinos(self, vecinos):          #Método para delimitar el numero de vecinos
        self.vecinos = vecinos
        self.setNumAlr()

    def setNumAlr(self):                    #Contar el número de bombas en los vecinos aledaños
        self.numAlr = 0
        for pieza in self.vecinos:
            if(pieza.getTieneBomba()):
                self.numAlr += 1

    def getNumAlr(self):
        return self.numAlr

    def toggleFlag(self):                  #Cambia el estado de una ficha marcada con una bandera
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def getVecinos(self):
        return self.vecinos
