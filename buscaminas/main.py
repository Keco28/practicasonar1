import pygame, sys
from pygame.locals import *
import turtle
from juego import Juego
from tablero import Tablero


mainClock = pygame.time.Clock()


pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)
font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    global click
    while True:

        background = pygame.image.load(r"imagenes/" + "img.png").convert()
        screen.fill((100, 100, 100))
        screen.blit(background, [0, 0])
        draw_text('Menú Principal', font, (0, 0, 0), screen, 200, 20)
        draw_text('Por Favor elija una Dificultad', font, (0, 0, 0), screen, 160, 50)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 100, 200, 50)
        button_2 = pygame.Rect(150, 170, 200, 50)
        button_3 = pygame.Rect(150, 240, 200, 50)
        button_4 = pygame.Rect(150, 310, 200, 50)
        button_5 = pygame.Rect(30, 450, 100, 30)
        button_6 = pygame.Rect(400, 450, 70, 30)
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        pygame.draw.rect(screen, (0, 0, 0), button_4)
        pygame.draw.rect(screen, (0, 0, 0), button_5)
        pygame.draw.rect(screen, (0, 0, 0), button_6)
        draw_text('Facil', font, (255, 255, 255), screen, 235, 120)
        draw_text('Medio', font, (255, 255, 255), screen, 230, 190)
        draw_text('Dificil', font, (255, 255, 255), screen, 230, 260)
        draw_text('Personalizado', font, (255, 255, 255), screen, 205, 330)
        draw_text('¿Como jugar?', font, (255, 255, 255), screen, 35, 458)
        draw_text('Salir', font, (255, 255, 255), screen, 420, 458)
        if button_1.collidepoint((mx, my)) and click:
            game(1)
        if button_2.collidepoint((mx, my)) and click:
            game(2)
        if button_3.collidepoint((mx, my)) and click:
            game(3)
        if button_4.collidepoint((mx, my)) and click:
            game(4)
        if button_5.collidepoint((mx, my)) and click:
            instrucciones()
        if button_6.collidepoint((mx, my)) and click:
            pygame.quit()
            sys.exit()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                click = True

        pygame.display.update()
        mainClock.tick(60)


def game(i):
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('game', font, (255, 0, 0), screen, 220, 20)
        if i == 1:
            tablero(8, 8, 10)
        elif i == 2:
            tablero(16, 16, 40)
        elif i == 3:
            tablero(30, 16, 99)
        elif i == 4:
            sc = turtle.Screen()
            sc.setup(300, 300)
            n = int(turtle.textinput("ingrese los datos en numeros", "filas"))
            m = int(turtle.textinput("ingrese los datos en numeros", "columnas"))
            k = int(turtle.textinput("ingrese los datos en numeros", "bombas"))
            sc.bye()
            tablero(n, m, k)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def tablero(i, j, k):
    tamaño = (i, j)
    prob = k
    tablero = Tablero(tamaño, prob)
    tamaño_pantalla = (500, 500)
    juego = Juego(tablero, tamaño_pantalla)
    juego.run()
    mainClock.tick(60)


def instrucciones():
    running = True
    while running:
        screen.fill((100, 100, 100))
        draw_text('¿Como jugar?', font, (255, 255, 255), screen, 200, 20)
        draw_text(a, font, (255, 255, 255), screen, 10, 90)
        draw_text(b, font, (255, 255, 255), screen, 10, 110)
        draw_text(w, font, (255, 255, 255), screen, 10, 130)
        draw_text(c, font, (255, 255, 255), screen, 10, 150)
        draw_text(d, font, (255, 255, 255), screen, 10, 170)
        draw_text(e, font, (255, 255, 255), screen, 10, 190)
        draw_text(f, font, (255, 255, 255), screen, 10, 210)
        draw_text(w, font, (255, 255, 255), screen, 10, 230)
        draw_text(g, font, (255, 255, 255), screen, 10, 250)
        draw_text(h, font, (255, 255, 255), screen, 10, 270)
        draw_text(w, font, (255, 255, 255), screen, 10, 290)
        draw_text(i, font, (255, 255, 255), screen, 10, 310)
        draw_text(w, font, (255, 255, 255), screen, 10, 330)
        draw_text(j, font, (255, 255, 255), screen, 10, 350)
        draw_text(k, font, (255, 255, 255), screen, 10, 370)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        pygame.display.update()
        mainClock.tick(60)


a = "El juego consiste en despejar todas las casillas de una pantalla "
b = "que no oculten una mina. "
c = "Algunas casillas tienen un número, este número indica las minas "
d = "que son en todas las casillas circundantes. Así, si una casilla "
e = "tiene el número 3, significa que de las ocho casillas que hay alrededor "
f = "(si no es en una esquina o borde) hay 3 con minas y 5 sin minas. "
g = "Si se descubre una casilla sin número indica que ninguna de las casillas "
h = "vecinas tiene mina y estas se descubren automáticamente. "
i = "Si se descubre una casilla con una mina se pierde la partida. "
j = "Se puede poner una marca en las casillas que el jugador piensa que hay "
k = "minas para ayudar a descubrir la que están cerca. "
w = ""

main_menu()


