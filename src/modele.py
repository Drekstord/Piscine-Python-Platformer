import pygame
import random

# constantes globals qui permettent le paramètrage de base du jeu
TILE_SIZE = 64
LONGUEUR = 1920
LARGEUR = 1080
FONT = "./font/8bit16.ttf"
GAME_NAME = "L'envolée Educative"


class JeuModel:
    def __init__(self):
        # changer ici si il y a ajout de modèle
        self.LVL_MAX = 2
        self.vivant = False

        self.ecran = 1  # 1 = démarrage, 2 = selection niveaux, 3 = mort, 4 = victoire, 5 = lvl 1, 6 = lvl 2
        self.selected_lvl = 1  # variable de selection de niveau
        self.selected_death_box = 1  # variable qui permet de connaitre la text box selectionné dans la page de mort et de victoire

    # setter and getter
    def get_selected_lvl(self):
        return self.selected_lvl

    def set_selected_lvl(self, value):
        # calcul pour avoir le bouton quitter
        if value > self.LVL_MAX + 1:
            self.selected_lvl = 1
        elif value < 1:
            self.selected_lvl = self.LVL_MAX + 1
        else:
            self.selected_lvl = value

    def get_LVL_MAX(self):
        return self.LVL_MAX

    def get_selected_death_box(self):
        return self.selected_death_box

    def set_selected_death_box(self, value):
        # calcul pour avoir le bouton quitter
        if value > 3:
            self.selected_death_box = 1
        elif value < 1:
            self.selected_death_box = 3
        else:
            self.selected_death_box = value

    def get_ecran(self):
        return self.ecran

    def set_ecran(self, value):
        self.ecran = value

    def get_vivant(self):
        return self.vivant

    def set_vivant(self, value):
        self.vivant = value

    def mise_a_jour(self):
        return
