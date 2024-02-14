import pygame
from tiles import Tuile
from endPoint import End_Point
from modele import TILE_SIZE, LONGUEUR
from perso import Player


class Niveau:
    def __init__(self, level_data, surface):
        # Setup du niveau
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.player_life = True
        self.victory = False

    def get_player_life(self):
        return self.player_life

    def set_player_life(self, value):
        self.player_life = value

    def get_victory(self):
        return self.victory

    def set_victory(self, value):
        self.victory = value

    # Configuration du niveau basée sur les données fournies
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()  # Groupe de tuiles pour les obstacles
        self.end = pygame.sprite.Group()  # Groupe pour le point de fin
        self.player = pygame.sprite.GroupSingle()  # Groupe pour le joueur

        # Création des tuiles, du joueur et du point de fin basé sur le layout
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                # Création des différents éléments selon le caractère dans le layout
                if cell == "X":
                    tile = Tuile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "E":
                    end_point = End_Point((x, y), TILE_SIZE)
                    self.end.add(end_point)

    # Gestion du défilement horizontal du niveau
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        # Conditions pour déplacer le monde (et non le joueur)
        if player_x < LONGUEUR / 4 and direction_x < 0:
            self.world_shift = 8  # Déplace le monde vers la droite
            player.speed = 0
        elif player_x > LONGUEUR / 2.2 and direction_x > 0:
            self.world_shift = -8  # Déplace le monde vers la gauche
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8  # Vitesse normale du joueur

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        # Vérification des collisions avec les tuiles
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # Collision à gauche
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:  # Collision à droite
                    player.rect.right = sprite.rect.left
        # Vérification des collisions avec le point de fin
        for sprite in self.end.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    self.victory = True
                elif player.direction.x > 0:
                    self.victory = True

    # Gestion des collisions lors des mouvements verticaux
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        # Vérification des collisions avec les tuiles
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:  # Collision en tombant
                    player.direction.y = 0
                    player.rect.bottom = sprite.rect.top
                elif player.direction.y < 0:  # Collision en sautant
                    player.direction.y = 0
                    player.rect.top = sprite.rect.bottom
        # Vérification des collisions avec le point de fin
        for sprite in self.end.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    self.victory = True
                elif player.direction.y < 0:
                    self.victory = True

    # Gestion de la mort du joueur en cas de chute
    def mort_chutte(self):
        player = self.player.sprite
        player_y = player.rect.centery  # Position Y du joueur
        if player_y > 1088:  # Si le joueur tombe en dessous d'un certain seuil
            self.player_life = False  # Le joueur meurt

    # Méthode run pour exécuter la logique du niveau
    def run(self):
        # Mise à jour et affichage des tuiles et du point de fin
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.end.update(self.world_shift)
        self.end.draw(self.display_surface)
        self.scroll_x()

        # Player
        self.player.update()
        self.mort_chutte()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
