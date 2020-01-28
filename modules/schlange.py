from . import kopf, koerper


class Schlange:
    def __init__(self, kopf_farbe=(255, 255, 255), koerper_farbe=(255, 255, 255)):
        self.kopf = kopf.Kopf(kopf_farbe)
        self.koerper = koerper.Koerper(self.kopf, koerper_farbe)

    def zeichne(self, oberflaeche):
        self.kopf.zeichne(oberflaeche)
        self.koerper.zeichne(oberflaeche)

    def bewege(self):
        self.kopf.aktualisiere_verlauf(self.koerper)
        self.kopf.bewege()

    def kollidiert(self, fenster):
        if self.kopf.kollidiert_mit_rand(fenster) or self.kopf.kollidiert_mit_koerper():
            return True
        return False
