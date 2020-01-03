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
        self.koerper.aktualisiere_liste()
