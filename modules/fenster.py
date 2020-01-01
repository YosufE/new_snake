import pygame


class Fenster:
    def __init__(self, breite, hoehe, farbe=(0, 0, 0)):
        self.breite = breite
        self.hoehe = hoehe
        self.farbe = farbe

        # nimmt nur eine liste mit breite und höhe an
        self.fenster = pygame.display.set_mode((breite, hoehe))

    def aktualisieren(self):
        pygame.display.flip()
