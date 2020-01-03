import pygame


class Fenster:
    def __init__(self, breite=600, hoehe=600, farbe=(0, 0, 0)):
        self.breite = breite
        self.hoehe = hoehe
        self.farbe = farbe

        # Nimmt nur eine Liste mit Breite und Höhe an
        self.oberflaeche = pygame.display.set_mode((breite, hoehe))

    def aktualisiere(self):
        pygame.display.flip()
        self.oberflaeche.fill(self.farbe)
