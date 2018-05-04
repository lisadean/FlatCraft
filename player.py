import pygame
from block import Block


class Player(Block):
    def __init__(self):
        super().__init__()
        velocity = 32

        self.image = './images/hero.png'
        self.pos = [96, 96]
        self.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

        self.vx = velocity
        self.vy = velocity

        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

    def handle_keydown(self, key):
        for i in range(2):
            if key == self.move[i]:
                self.rect.x += self.vx * [-1, 1][i]

        for i in range(2):
            if key == self.move[2:4][i]:
                self.rect.y += self.vy * [-1, 1][i]            
