import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def setImage(self, image):
        self.image = pygame.image.load(image).convert_alpha()

    def setSize(self):
        self.rect = self.image.get_rect()

    def setPosition(self, pos):
        self.rect.topleft = pos
