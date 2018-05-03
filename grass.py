import pygame
from block import Block


class Grass(Block):
    def __init__(self):
        super().__init__()
        self.image = './images/clover.jpg'
        self.pos = [0, 0]
        self.setImage(self.image)
        self.setSizeAndPosition(self.pos)

        def setImage(self, image):
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (32, 32))
