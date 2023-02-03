"""
Polashi Dey
Tp 4
excercice 6

Cette code est pour faire une classe de héro comme l'excercice 4 mais en ajoutant un database de l'excercice 5.
"""

import random


class Hero:
    def __init__(self, nom_hero):
        self.nom_hero = nom_hero
        self.point_vie = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)
        self.force_charisme = random.randint(1, 20)

    def action_attaque(self):
        return self.force_attaque + random.randint(1, 10)

    def recevoir_dommage(self, dommage):
        self.point_vie -= dommage - self.force_defense

    def est_vivant(self):
        return.point_vie > 0

    def afficher_tout(self):
        print(f"\nNom: {self.nom_hero}"
              f"\n point de vie: {self.point_vie}"
              f"\n force d'attaque: {self.force_attaque}"
              f"\n force de defense: {self.force_defense}"
              f"\n charisme: {self.force_charisme}")


Hero = Hero("Roi")
Hero.afficher_tout()
