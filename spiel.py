from modules import fenster, viereck
import pygame

fenster = fenster.Fenster(500, 500)
viereck = viereck.Viereck(fenster.oberflaeche, 50, 50, 50, 50)

laufendes_Spiel = True
while laufendes_Spiel:
    fenster.aktualisiere()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            laufendes_Spiel = False

    viereck.zeichne()
