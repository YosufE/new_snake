import pygame


class Viereck:
    def __init__(self, x, y, groesse, farbe=(255, 255, 255)):
        self.x = x
        self.y = y
        self.farbe = farbe
        self.groesse = groesse

    def zeichne(self, oberflaeche):
        pygame.draw.rect(oberflaeche, self.farbe, (self.x, self.y, self.groesse, self.groesse))
