import pygame
from . import viereck


class Kopf(viereck.Viereck):
    def __init__(self, farbe):
        super().__init__(260, 260, 20, farbe)

        self.richtung = None
        self.verlauf_koordinaten = []

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

    def aktualisiere_verlauf(self, koerper):
        if self.richtung != None:
            self.verlauf_koordinaten.append((self.x, self.y))
            # Behalte die Liste auf die Länge des Körpers + 1 um zu wissen wo nächstes viereck gezeichnet wird
            self.verlauf_koordinaten = self.verlauf_koordinaten[-koerper.laenge-1:]

    def kollidiert_mit_rand(self, fenster):
        if (self.x >= fenster.breite) or (self.x < 0) or (self.y >= fenster.hoehe) or (self.y < 0):
            return True
        return False

    def kollidiert_mit_koerper(self):
        if (self.x, self.y) in self.verlauf_koordinaten[1:]:
            return True
        return False

    def kollidiert_mit_essen(self, essen):
        if (self.x, self.y) == (essen.x, essen.y):
            return True
        return False

