import pygame as pg
from config import height, width, tile_size
from block import Block
from resource import Grass


class Player(Block):
    def __init__(self):
        super().__init__()
        self.velocity = 32
        self.health = 100
        self.backpack = {}
        self.backpack_text = ""

        self.image = './images/hero.png'
        self.pos = [96, 96]
        self.move = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]

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

    def harvest(self, harvestable_group, terrain_group):
        harvestable = pg.sprite.spritecollide(self, harvestable_group, True)
        for tile in harvestable:
            tile_pos = tile.pos
            self.addToInventory(tile.drop)
            tile.kill()
            new_tile = Grass(tile_pos)
            new_tile.add(terrain_group)

    def addToInventory(self, item):
        if item not in self.backpack:
            self.backpack[item] = 1
        else:
            self.backpack[item] = self.backpack[item] + 1
        self.printInventory()
    
    def printInventory(self):
        contents = ""
        for item, quantity in self.backpack.items():
            contents += "%s: %d\n" % (item, quantity)
        # print(contents)
        self.backpack_text = contents

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
