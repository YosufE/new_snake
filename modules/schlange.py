from . import viereck, kopf


class Schlange(viereck.Viereck):
    def __init__(self, farbe=(255, 255, 255)):
        self.farbe = farbe

        self.kopf = kopf.Kopf()

    def zeichne(self, oberflaeche):
        self.kopf.zeichne(oberflaeche)
