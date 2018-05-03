import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def setImage(self, image):
        self.image = pygame.image.load(image).convert_alpha()

    def setSizeAndPosition(self, pos):
        self.rect = self.image.get_rect()
        self.rect.center = pos
