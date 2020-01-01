import pygame


class Viereck:
    def __init__(self, oberflaeche, x, y, breite, hoehe, farbe=(255, 255, 255)):
        self.oberflaeche = oberflaeche
        self.x = x
        self.y = y
        self.breite = breite
        self.hoehe = hoehe
        self.farbe = farbe

    def zeichne(self):
        pygame.draw.rect(self.oberflaeche, self.farbe, (self.x, self.y, self.breite, self.hoehe))
