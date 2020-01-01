from modules import fenster
import pygame

fenster = fenster.Fenster(500, 500)

laufendes_Spiel = True
while laufendes_Spiel:
    fenster.aktualisieren()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            laufendes_Spiel = False
