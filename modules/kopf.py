import pygame
from . import viereck


class Kopf(viereck.Viereck):
    def __init__(self, farbe=(255, 255, 255)):
        self.x = 260
        self.y = 260
        self.groesse = 20
        self.farbe = farbe

        self.richtung = None

    def aktualisiere_Richtung(self, taste):
        if taste == pygame.K_LEFT and self.richtung != "Rechts":
            self.richtung = "Links"
        elif taste == pygame.K_RIGHT and self.richtung != "Links":
            self.richtung = "Rechts"
        elif taste == pygame.K_UP and self.richtung != "Unten":
            self.richtung = "Oben"
        elif taste == pygame.K_DOWN and self.richtung != "Oben":
            self.richtung = "Unten"

    def bewege(self):
        if self.richtung == "Links":
            self.x -= self.groesse
        elif self.richtung == "Rechts":
            self.x += self.groesse
        elif self.richtung == "Oben":
            self.y -= self.groesse
        elif self.richtung == "Unten":
            self.y += self.groesse

