from random import randint
from pygame.sprite import spritecollide
from block import Block
from config import tile_size, width, height


class Mob(Block):
    def __init__(self):
        super().__init__()
        self.velocity = tile_size
        images = ['./images/goblin.png',
                  './images/monster.png']
        self.image = images[randint(0, 1)]
        self.pos = [(1, 1), (1, height), (width, 1),
                    (width, height)][randint(0, 3)]
        self.vx = self.velocity
        self.vy = self.velocity

        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

    def get_direction(self, player):
        x_distance = self.rect.x - player.rect.x
        y_distance = self.rect.y - player.rect.y

        if x_distance == 0:
            x_direction = 0
        elif x_distance < 0:
            x_direction = 1
        else:
            x_direction = -1

        if y_distance == 0:
            y_direction = 0
        elif y_distance < 0:
            y_direction = 1
        else:
            y_direction = -1

        return [x_direction, y_direction]

    def move(self, player, house_group):
        direction = self.get_direction(player)

        # Move left or right
        old_x = self.rect.x
        new_x = self.rect.x + (self.vx * direction[0])
        self.rect.x = new_x
        if spritecollide(self, house_group, False):
            self.rect.x = old_x

        # Move up or down
        old_y = self.rect.y
        new_y = self.rect.y + (self.vy * direction[1])
        self.rect.y = new_y
        if spritecollide(self, house_group, False):
            self.rect.y = old_y

        # print("Player: [%d, %d] Mob: [%d, %d]" % (player.rect.x,
        #                                           player.rect.y,
        #                                           self.rect.x, self.rect.y))
