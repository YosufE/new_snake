from . import viereck, kopf, koerper


class Schlange(viereck.Viereck):
    def __init__(self, farbe=(255, 255, 255)):
        self.farbe = farbe

        self.kopf = kopf.Kopf()
        self.koerper = koerper.Koerper(self.kopf)

    def zeichne(self, oberflaeche):
        self.kopf.zeichne(oberflaeche)
        self.koerper.zeichne(oberflaeche)
    
    def bewege(self):
        self.kopf.bewege()
        self.kopf.aktualisiere_verlauf(self.koerper)

    def kollidiert(self, fenster):
        if self.kopf.kollidiert_mit_rand(fenster) or self.kopf.kollidiert_mit_koerper():
            return True
        return False
