import pygame
from os import walk


def import_folder(path):
    surface_list = []

    # Parcours du dossier spécifié et chargement de toutes les images du joueur
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    # retourne les images de l'animation du joueur
    return surface_list


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        # Initialisation des paramètres d'animation et de position
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["stop"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        # Paramètres de mouvement du personnage
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # Statut initial du personnage
        self.status = "stop"

        # Variable pour tester le vol (à des fins de développement)
        self.fly = False

    # Méthode pour importer les ressources graphiques du personnage
    def import_character_assets(self):
        character_path = ".\\sprites\\skin\\"
        self.animations = {"run": [], "stop": []}

        # Chargement des images pour chaque type d'animation
        for animation in self.animations.keys():
            full_path = character_path + animation
            loaded_images = import_folder(full_path)
            scaled_images = [
                pygame.transform.scale(img, (64, 64)) for img in loaded_images
            ]
            self.animations[animation] = scaled_images

    # Méthode pour animer le personnage
    def animate(self):
        animation = self.animations[self.status]

        # Logique pour boucler à travers les frames d'animation
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    # Méthode pour gérer les entrées clavier
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # Gestion du saut
        if keys[pygame.K_SPACE]:
            self.jump()

        # Activation du mode "vol" (test)
        if keys[pygame.K_f] and self.fly:
            self.fly = False
        elif keys[pygame.K_f] and not self.fly:
            self.fly = True

    # Méthode pour mettre à jour le statut du personnage
    def get_status(self):
        if self.direction.x != 0:
            self.status = "run"
        else:
            self.status = "stop"

    # Méthode pour appliquer la gravité
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    # Méthode pour gérer le saut
    def jump(self):
        if self.direction.y == 0 or self.fly:
            self.direction.y = self.jump_speed

    # Méthode update pour mettre à jour l'état du personnage
    def update(self):
        self.get_input()
        self.get_status()
        self.animate()

        # vérif de la direction pour rotationner le sprite
        if self.direction.x < 0:  # déplace vers la gauche --> flip gauche
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction.x > 0:  # déplace vers la droite --> aucun flip
            self.image = pygame.transform.flip(self.image, False, False)
