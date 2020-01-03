from . import viereck


class Koerper(viereck.Viereck):
    def __init__(self, kopf, farbe=(255, 255, 255)):
        self.kopf = kopf
        self.farbe = farbe

        self.laenge = 0

    def zeichne(self, oberflaeche):
        # Zeichne nur so viel wie die laenge des koerpers (die liste hat immer eines extra damit das naechste
        # gezeichnet werden kann)
        for koordinatenset in self.kopf.verlauf_koordinaten[:-1]:
            viereck.Viereck(koordinatenset[0], koordinatenset[1], self.kopf.groesse).zeichne(oberflaeche)

    def erweitere(self):
        self.laenge += 1
