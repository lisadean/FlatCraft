import pygame
from config import *
from block import Block


class Player(Block):
    def __init__(self):
        super().__init__()
        self.velocity = 32
        self.health = 100
        self.backpack = {}

        self.image = './images/hero.png'
        self.pos = [96, 96]
        self.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

        self.vx = self.velocity
        self.vy = self.velocity

        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

    def handle_keydown(self, key):
        for i in range(2):
            if key == self.move[i]:
                new_x = self.rect.x + self.vx * [-1, 1][i]

                #  Prevent going off screen
                if new_x < 0:
                    new_x = 0
                elif new_x > width - tile_size:
                    new_x = width - tile_size
                else:
                    self.rect.x = new_x

        for i in range(2):
            if key == self.move[2:4][i]:
                new_y = self.rect.y + self.vy * [-1, 1][i]

                #  Prevent going off screen
                if new_y < 0:
                    new_y = 0
                elif new_y > height - tile_size:
                    new_y = height - tile_size
                else:
                    self.rect.y = new_y

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
