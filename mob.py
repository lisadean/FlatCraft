from block import Block
import spritesheet


class Mob(Block):
    def __init__(self):
        super().__init__()
        self.velocity = 32
        self.image = './images/goblin.png'
        self.pos = [0, 0]

        self.vx = self.velocity
        self.vy = self.velocity

        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

    def move(self, player):
        player_x = player.rect.x
        player_y = player.rect.y

        x_distance = self.rect.x - player_x
        y_distance = self.rect.y - player_y

        if x_distance != 0:
            x_direction = int(x_distance / abs(x_distance))
        else:
            x_direction = 0

        if y_distance != 0:
            y_direction = int(y_distance / abs(y_distance))
        else:
            y_direction = 0

        if x_direction != 0:
            if x_direction == -1:
                self.rect.x = self.rect.x + self.vx  # Move right
            if x_direction == 1:
                self.rect.x = self.rect.x - self.vx  # Move left
        if y_direction != 0:
            if y_direction == -1:
                self.rect.y = self.rect.y + self.vy  # Move down
            if y_direction == 1:
                self.rect.y = self.rect.y - self.vy  # Move up

        print("Player: [%d, %d] Mob: [%d, %d]" % (player_x, player_y,
                                                  self.rect.x, self.rect.y))


class Skeleton(Mob):
    # ### DO NOT USE ###
    # Sprite sheet doesn't work yet
    def __init__(self):
        super().__init__()

        ss = spritesheet.spritesheet('./images/skeleton-front.png')
        images = []
        # Load two images into an array, their transparent bit is (255, 255, 255)
        images = ss.images_at([(0, 0, 32, 32), (33, 0, 32, 32)], colorkey=-1)
        self.image = images[0]
