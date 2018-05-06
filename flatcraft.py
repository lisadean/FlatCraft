import pygame as pg
import random
from config import height, width, fps, title, grid_height, grid_width
from config import tile_size, white, red
from player import Player
from mob import Mob
from resource import Grass, Ore, Tree


def build_world():
    terrain_group = pg.sprite.Group()
    harvestable_group = pg.sprite.Group()
    grid_y = 0
    for h in range(grid_height):
        grid_x = 0
        for w in range(grid_width):
            roll = random.randint(1, 100)
            # Order in increasing scarcity_percentage order
            if roll in range(Ore.scarcity_percentage):
                ore = Ore([grid_x, grid_y])
                ore.add(terrain_group, harvestable_group)
            elif roll in range(Tree.scarcity_percentage):
                tree = Tree([grid_x, grid_y])
                tree.add(terrain_group, harvestable_group)
            else:
                terrain_group.add(Grass([grid_x, grid_y]))
            grid_x += tile_size
        grid_y += tile_size
    return terrain_group, harvestable_group


def display_status(screen, player):
        font = pg.font.Font(None, 36)
        x = 10
        y = 10
        status = player.status_text + "\n" + player.backpack_text
        for line in status.splitlines():
            line_surface = font.render(line, 1, white)
            line_height = line_surface.get_height()
            screen.blit(line_surface, [x, y])
            y += line_height


def main():

    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption(title)

    #  Build random terrain

    terrain_group, harvestable_group = build_world()

    #  Create characters

    player = Player()
    player_group = pg.sprite.Group()
    player_group.add(player)

    mob_group = pg.sprite.Group()
    mob_group.add(Mob())

    #  Mob timers

    move_event = pg.USEREVENT+1
    time_to_move = 2000  # 2 seconds
    pg.time.set_timer(move_event, time_to_move)

    mob_spawn_event = pg.USEREVENT+2
    time_to_spawn = 20000  # 20 seconds
    pg.time.set_timer(mob_spawn_event, time_to_spawn)

    # Game initialization

    stop_game = False
    while not stop_game:

        if player.isDead():
            stop_game = True

        for event in pg.event.get():

            if event.type == pg.QUIT:
                stop_game = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    stop_game = True
                elif event.key == pg.K_h:
                    player.harvest(harvestable_group, terrain_group)
                else:
                    player.handle_keydown(event.key)

            if event.type == move_event:
                for mob in mob_group.sprites():
                    mob.move(player)

            if event.type == mob_spawn_event:
                mob_group.add(Mob())

        # Game logic
        mob_contact = pg.sprite.spritecollide(player, mob_group, True)
        if mob_contact:
            player.takeDamage()

        player_group.update()
        mob_group.update()

        # Game display
        terrain_group.draw(screen)
        player_group.draw(screen)
        mob_group.draw(screen)

        display_status(screen, player)

        pg.display.update()

        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
