"""
Tp 4
Polashi Dey
Excercice 3

Cette code est pour afficher le circonference et l'aire d'une classe qui s'appelle cercle.
"""

from math import pi


class Cercle:

    def _init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return pi * self.rayon * 2

    def calcul_circonference(self):
        return pi * self.rayon * 2

    def afficher_infos(self):
        print(f" le cercle a un aire de {self.calcul_aire()})",
              f" le cercle a un circonference de {self.calcul_circonference()}")









