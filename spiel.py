from modules import fenster, schlange, essen
import pygame

clock = pygame.time.Clock()
fenster = fenster.Fenster()
schlange = schlange.Schlange()
essen = essen.Essen()


laufendes_Spiel = True
while laufendes_Spiel:
    fenster.aktualisiere()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            laufendes_Spiel = False
        if event.type == pygame.KEYDOWN and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            schlange.kopf.aktualisiere_Richtung(event.key)
            break  # um zu verhindern das man mehrere Tasten aufeinmal drueckt

    schlange.bewege()

    schlange.zeichne(fenster.oberflaeche)
    essen.zeichne(fenster.oberflaeche)

    if schlange.kollidiert(fenster):
        laufendes_Spiel = False
    if schlange.kopf.kollidiert_mit_essen(essen):
        schlange.koerper.erweitere()
        essen.neu(schlange)
