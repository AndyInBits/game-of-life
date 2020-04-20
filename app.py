# -*- coding: utf-8 -*-
import pygame
import numpy as np
import time
pygame.init()

width, heigth = 1000, 1000
screen = pygame.display.set_mode((heigth, width))
bg = 25, 25, 25, 25
screen.fill(bg)

# Numero de celdas
nxC, nyC = 25, 25

# Dimensiones de la celda
dimCW = width / nxC
dimCH = heigth / nyC

# Estado de las celdas vivas = 1; muertas = 0
gameState = np.zeros((nxC, nyC))

gameState[0, 0] = 1
gameState[0, 1] = 1
gameState[0, 2] = 1
gameState[0, 3] = 1
gameState[1, 0] = 1

while True:

    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    for y in range(0, nxC):
        for x in range(0, nyC):

            # calculamos el numero de vecinos cercanos
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                gameState[(x) % nxC, (y - 1) % nyC] + \
                gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                gameState[(x - 1) % nxC, (y) % nyC] + \
                gameState[(x + 1) % nxC, (y) % nyC] + \
                gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                gameState[(x) % nxC, (y + 1) % nyC] + \
                gameState[(x + 1) % nxC, (y + 1) % nyC]

            # Regla 1 : una celula muerta con exactamente 3 vecinas vivas " revive ".
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # Regla 2 : una celula viva con menos de 2 o ms de 3 vecinos vivos muere.
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # Creamos el poligono de cada celda a dibujar
            poly = [
                ((x) * dimCW, y * dimCH),
                ((x + 1) * dimCW, y * dimCH),
                ((x + 1) * dimCW, (y + 1) * dimCH),
                ((x) * dimCW, (y + 1) * dimCH)
            ]

            # dibujamos la celda para cada par x e y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    # actualiza la pantalla
    pygame.display.flip()
