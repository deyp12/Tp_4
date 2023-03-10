"""
Polashi Dey
Tp 4
excercice 4

Cette code est pour classer les stastiques du Héro et aussi classer les méthodes d'attaques et défense.
"""

import random



class Hero:

    def __init__(self, nom_hero):
        self.nom_hero = nom_hero
        self.point_vie = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)

    def action_attaque(self):
        return self.force_attaque + random.randint(1, 6)

    def recevoir_dommage(self, dommage):
        self.point_vie -= dommage - self.force_defense

    def est_vivant(self):
        print(f"\nNom: {self.nom_hero}"
              f"\n point de vie: {self.point_vie}"
              f"\n force d'attaque: {self.force_attaque}"
              f"\n force de defense: {self.force_defense}")


Hero = Hero("Roi")
Hero.afficher_tout()
print(f"\nAttaque: {self.force_attaque()}")
Hero.recevoir_dommage(10)
print(f"\nEn vie: {Hero.action_attaque()}")
Hero.afficher_tout()
