import pygame as pg
from math import floor
from config import height, width, tile_size, grid_height, grid_width
from block import Block
from resource import Grass
from house import House


class Player(Block):
    def __init__(self):
        super().__init__()
        self.velocity = 32
        self.health = 2
        self.armor = 0
        self.backpack = {}
        self.backpack_text = ""
        self.status_text = ""

        self.image = './images/hero.png'
        self.hit_sound = './sounds/hit.ogg'
        # self.pos = [96, 0]
        self.pos = [floor(grid_width/2) * tile_size,
                    floor(grid_height/2) * tile_size]
        self.movements = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]

        self.vx = self.velocity
        self.vy = self.velocity

        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

    def move(self, key):
        for i in range(2):
            if key == self.movements[i]:
                new_x = self.rect.x + self.vx * [-1, 1][i]

                #  Prevent going off screen
                if new_x < 0:
                    new_x = 0
                elif new_x > width - tile_size:
                    new_x = width - tile_size
                else:
                    self.rect.x = new_x

        for i in range(2):
            if key == self.movements[2:4][i]:
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
            self.addToInventory(tile.drop, 1)
            pg.mixer.Sound(tile.harvest_sound).play()
            tile.kill()
            new_tile = Grass(tile_pos)
            new_tile.add(terrain_group)

    def addToInventory(self, item, quantity):
        if item not in self.backpack:
            self.backpack[item] = quantity
        else:
            self.backpack[item] = self.backpack[item] + quantity
        self.printInventory()

    def removeFromInventory(self, item, quantity):
        if item in self.backpack:
            if self.backpack[item] >= quantity:
                self.backpack[item] -= quantity
                self.printInventory()
                return True
            return False

    def buildArmor(self):
        if self.removeFromInventory('Metal', 2):
            self.armor += 1
        else:
            print("Not enough metal")

    def buildHouse(self, pos, harvestable_group, mob_group,
                   house_group):
        if self.removeFromInventory('Wood', 4):
            house = House(pos, harvestable_group, mob_group,
                          house_group)
            if house not in house_group:
                self.addToInventory('Wood', 4)
                print("Can't place house")
        else:
            print("Not enough wood")

    def printInventory(self):
        contents = ""
        for item, quantity in self.backpack.items():
            contents += "%s: %d\n" % (item, quantity)
        self.backpack_text = contents

    def takeDamage(self):
        pg.mixer.Sound(self.hit_sound).play()
        if self.armor > 0:
            self.armor -= 1
        else:
            self.health -= 1

    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def update(self):
        status = "Health: %d\n" % self.health
        status += "Armor: %d\n" % self.armor
        status += "\n"
        self.status_text = status
