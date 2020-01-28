from . import viereck


class Koerper:
    def __init__(self, kopf, farbe):
        self.kopf = kopf
        self.farbe = farbe

        self.laenge = 0

    def zeichne(self, oberflaeche):
        # Zeichne nur so viel wie die laenge des koerpers (die liste hat immer eines extra damit das naechste
        # gezeichnet werden kann)
        for koordinatenset in self.kopf.verlauf_koordinaten[1:]:
            viereck.Viereck(koordinatenset[0], koordinatenset[1], self.kopf.groesse, self.farbe).zeichne(oberflaeche)

    def erweitere(self):
        self.laenge += 1
