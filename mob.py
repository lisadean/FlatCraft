from pygame.sprite import spritecollide
from block import Block
from config import tile_size, width, height
import spritesheet


class Mob(Block):
    def __init__(self):
        super().__init__()
        self.velocity = tile_size
        self.image = './images/goblin.png'
        self.pos = [width, height]

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


class Skeleton(Mob):
    # ### DO NOT USE ###
    # Sprite sheet doesn't work yet
    def __init__(self):
        super().__init__()

        ss = spritesheet.spritesheet('./images/skeleton-front.png')
        images = []
        # Load two images into an array, their transparent bit is
        # (255, 255, 255)
        images = ss.images_at([(0, 0, 32, 32), (33, 0, 32, 32)], colorkey=-1)
        self.image = images[0]
