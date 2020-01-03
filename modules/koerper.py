from . import viereck


class Koerper(viereck.Viereck):
    def __init__(self, kopf, farbe=(255, 255, 255)):
        self.kopf = kopf
        self.farbe = farbe

        self.laenge = 0
        self.verlauf_koordinaten = [(self.kopf.x, self.kopf.y)]

    def zeichne(self, oberflaeche):
        # Zeichne nur so viel wie die laenge des koerpers (die liste hat immer eines extra damit das naechste
        # gezeichnet werden kann)
        for koordinatenset in self.verlauf_koordinaten[:-1]:
            viereck.Viereck(koordinatenset[0], koordinatenset[1], self.kopf.groesse-1).zeichne(oberflaeche)

    def aktualisiere_liste(self):
        # Um zu verhindern, dass mehr als ein mal die gleichen Koordinaten folgen
        if self.verlauf_koordinaten[-1] != (self.kopf.x, self.kopf.y):
            self.verlauf_koordinaten.append((self.kopf.x, self.kopf.y))
        # Behalte die Liste auf die Länge des Körpers + 1
        self.verlauf_koordinaten = self.verlauf_koordinaten[-self.laenge - 1:]

    def erweitere(self):
        self.laenge += 1
