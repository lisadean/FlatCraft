import pygame
import random
from player import Player
from mob import Mob
from grass import Grass
from tree import Tree
from ore import Ore


def main():
    game_name = "FlatCraft"
    fps = 50
    width = int(2560 / 2)
    height = int(1600 / 2)

    tile_size = 32
    grid_width = int(width / tile_size)
    grid_height = int(height / tile_size)
    print("grid height: %d width: %d" % (grid_height, grid_width))

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(game_name)

    #  Doesn't seem to do shit
    # pygame.key.set_repeat()

    #  Build world

    terrain_group = pygame.sprite.Group()
    grid_y = 0
    for h in range(grid_height):
        grid_x = 0
        for w in range(grid_width):
            roll = random.randint(1, 100)
            # Order in increasing scarcity_percentage order
            if roll in range(Ore.scarcity_percentage):
                terrain_group.add(Ore([grid_x, grid_y]))
            elif roll in range(Tree.scarcity_percentage):
                terrain_group.add(Tree([grid_x, grid_y]))
            else:
                terrain_group.add(Grass([grid_x, grid_y]))
            grid_x += tile_size
        grid_y += tile_size

    #  Create characters

    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    mob = Mob()
    mob_group = pygame.sprite.Group()
    mob_group.add(mob)

    # Game initialization

    stop_game = False
    while not stop_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    stop_game = True
                else:
                    player.handle_keydown(event.key)

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
