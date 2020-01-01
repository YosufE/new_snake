from modules import fenster, schlange
import pygame

clock = pygame.time.Clock()
fenster = fenster.Fenster(600, 600)
schlange = schlange.Schlange()


laufendes_Spiel = True
while laufendes_Spiel:
    fenster.aktualisiere()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            laufendes_Spiel = False
        if event.type == pygame.KEYDOWN and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            schlange.kopf.aktualisiere_Richtung(event.key)

    schlange.zeichne(fenster.oberflaeche)
    schlange.kopf.bewege()
