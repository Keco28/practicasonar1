import pygame
import os
from time import sleep

class Juego():
    def __init__(self, tablero, tamaño_pantalla):
        self.tablero = tablero
        self.tamaño_pantalla = tamaño_pantalla
        self.tamañoImg = self.tamaño_pantalla[0] // self.tablero.getTamaño()[1], self.tamaño_pantalla[1] // self.tablero.getTamaño()[0]
        self.cargarImagenes()

    def run(self):                                                          #Método principal del juego
        pygame.init()
        self.pantalla = pygame.display.set_mode(self.tamaño_pantalla)
        jugando = True
        while jugando:                                                      #While principal del juego
            for evento in pygame.event.get():                               #Se revisa cada evento del juego hasta que se llegue a alguno de los posibles finales
                if(evento.type == pygame.QUIT):
                    jugando = False
                if(evento.type == pygame.MOUSEBUTTONDOWN):                  #Se revisa el click hecho sobre el tablero
                    posicion = pygame.mouse.get_pos()
                    clickDerecho = pygame.mouse.get_pressed()[2]            #True si fue click derecho (Colocar una bandera)
                    self.handleClick(posicion, clickDerecho)                #Se envían los parámetros correspondientes a este click
            self.dibujar()
            pygame.display.flip()
            if(self.tablero.getGanar()):                                    #Si el número de casillas clickeadas es igual al número de casillas donde no hay bombas
                sonido = pygame.mixer.Sound("win.wav")                      #Significa que ganó, el juego terminará después de un sonido de victoria
                sonido.play()
                sleep(2)
                jugando = False
        pygame.quit()

    def dibujar(self):                                                      #Se encarga de dibujar en el tablero principal del juego
        topIzq = (0, 0)                                                     #La imagen correspondiente a la acción hecha
        tamaño = self.tablero.getTamaño()
        for fila in range(tamaño[0]):
            for col in range(tamaño[1]):
                pieza = self.tablero.getPieza((fila, col))
                imagen = self.getImagen(pieza)
                self.pantalla.blit(imagen, topIzq)
                topIzq = topIzq[0] + self.tamañoImg[0], topIzq[1]
            topIzq = 0, topIzq[1] + self.tamañoImg[1]

    def cargarImagenes(self):                                               #Crea un diccionario con todas las imágenes disponibles para su previo acceso
        self.imagenes = {}
        for archivo in os.listdir("imagenes"):
            if(not archivo.endswith(".png")):
                continue
            imagen = pygame.image.load(r"imagenes/" + archivo)
            imagen = pygame.transform.scale(imagen, self.tamañoImg)
            self.imagenes[archivo.split(".")[0]] = imagen

    def getImagen(self, pieza):                                             #Devuelve la imagen correspondiente al evento disparado sobre una pieza
        if(pieza.getClicked()):
            string = "bomb-at-clicked-block" if pieza.getTieneBomba() else str(pieza.getNumAlr())
        else:
            string = "flag" if pieza.getFlagged() else "empty-block"
        return self.imagenes[string]

    def handleClick(self, posicion, clickDerecho):
        if(self.tablero.getLost()):
            return
        index = posicion[1] // self.tamañoImg[1], posicion[0] // self.tamañoImg[0]
        #print(index)
        pieza = self.tablero.getPieza(index)
        self.tablero.handleClick(pieza, clickDerecho)