import pygame
from modele import JeuModel
from vue import JeuVue
from controleur import JeuControleur


def main():
    # Création des instances du modèle, de la vue, et du controleur
    MODELE = JeuModel()
    VUE = JeuVue()
    CONTROLEUR = JeuControleur(MODELE, VUE)

    # Lancement du jeu à travers le controleur
    CONTROLEUR.jouer()

    # Fermeture pygame à la fin du jeu
    pygame.quit()


# Vérification pour exécuter le jeu uniquement si ce script est le point d'entrée principal
if __name__ == "__main__":
    main()
