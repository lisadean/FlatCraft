import pygame
# from block import Block
from player import Player
from mob import Mob
from grass import Grass


def main():
    fps = 50
    width = int(2560 / 2)
    height = int(1600 / 2)

    tile_size = 32
    grid_width = int(width / tile_size)
    grid_height = int(height / tile_size)
    print("grid height: %d width: %d" % (grid_height, grid_width))
    # blue_color = (97, 159, 182)
    # grass = (86, 104, 57)
    # bg = grass

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('FlatCraft')
    clock = pygame.time.Clock()

    terrain_group = pygame.sprite.Group()

    grid_y = 0
    for h in range(grid_height):
        grid_x = 0
        for w in range(grid_width):
            print("%d, %d" % (grid_x, grid_y))
            terrain_group.add(Grass([grid_x, grid_y]))
            grid_x += tile_size
        grid_y += tile_size

    # block1 = Grass([0, 0])
    # block2 = Grass([32, 0])
    # block3 = Grass([64, 0])
    # block4 = Grass([96, 0])

    # terrain_group.add(block1)
    # terrain_group.add(block2)
    # terrain_group.add(block3)
    # terrain_group.add(block4)

    # player = Block([40, 50], './images/hero.png')
    player = Player()
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5

    player_group = pygame.sprite.Group()
    player_group.add(player)

    # mob = Block([100, 60], './images/goblin.png')
    mob = Mob()

    mob_group = pygame.sprite.Group()
    mob_group.add(mob)

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]

        # Draw background
        # screen.fill(bg)

        # Game logic
        hit = pygame.sprite.spritecollide(player, mob_group, True)
        if hit:
            player.image.fill((255, 255, 255))

        # Game display
        terrain_group.draw(screen)
        player_group.draw(screen)
        mob_group.draw(screen)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
