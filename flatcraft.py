import pygame as pg
import random
from config import *
from player import Player
from mob import Mob
# from grass import Grass
# from tree import Tree
# from ore import Ore
from resource import Grass, Ore, Tree


def main():

    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption(game_name)

    #  Build world

    terrain_group = pg.sprite.Group()
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
    player_group = pg.sprite.Group()
    player_group.add(player)

    mob = Mob()
    mob_group = pg.sprite.Group()
    mob_group.add(mob)

    # Game initialization

    stop_game = False
    while not stop_game:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop_game = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    stop_game = True
                else:
                    player.handle_keydown(event.key)

        # Game logic
        hit = pg.sprite.spritecollide(player, mob_group, True)
        if hit:
            player.image.fill((255, 255, 255))

        # Game display
        terrain_group.draw(screen)
        player_group.draw(screen)
        mob_group.draw(screen)

        pg.display.update()

        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
