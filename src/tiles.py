import pygame


class Tuile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # Création de l'image de la tuile
        self.image = pygame.Surface((size, size))
        self.image.blit(
            pygame.transform.scale(
                pygame.image.load("./sprites/block/block.png"),
                (size, size),
            ),
            (0, 0),
        )
        # Création du rectangle pour la position et les collisions
        self.rect = self.image.get_rect(topleft=pos)

    # Méthode pour mettre à jour la position de la tuile
    def update(self, x_shift):
        self.rect.x += x_shift
