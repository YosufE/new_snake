from . import viereck
import random


class Essen(viereck.Viereck):
    def __init__(self, farbe=(255, 0, 0)):
        self.farbe = farbe

        self.groesse = 20

        self.moegliche_koordinaten = [i for i in range(0, 600) if i % 20 == 0]
        self.x = random.choice(self.moegliche_koordinaten)
        self.y = random.choice(self.moegliche_koordinaten)

    def neu(self):
        self.x = random.choice(self.moegliche_koordinaten)
        self.y = random.choice(self.moegliche_koordinaten)
