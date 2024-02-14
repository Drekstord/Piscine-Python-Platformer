import pygame


class End_Point(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # Création de l'image du point de fin
        self.image = pygame.Surface((size, size))
        self.image.blit(
            pygame.transform.scale(
                pygame.image.load("./sprites/block/win.png"),
                (size, size),
            ),
            (0, 0),
        )
        # Création du rectangle pour la position et les collisions
        self.rect = self.image.get_rect(topleft=pos)

    # Méthode pour mettre à jour la position du point de fin
    def update(self, x_shift):
        self.rect.x += x_shift
