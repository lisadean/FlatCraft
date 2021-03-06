import pygame as pg
import random
from config import height, width, fps, title, grid_height, grid_width
from config import tile_size, white, time_to_spawn, time_to_move
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
    pg.mixer.music.load('./sounds/music.ogg')
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.5)
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

    house_group = pg.sprite.Group()

    #  Mob timers

    move_event = pg.USEREVENT+1
    pg.time.set_timer(move_event, time_to_move)

    mob_spawn_event = pg.USEREVENT+2
    pg.time.set_timer(mob_spawn_event, time_to_spawn)

    # Game initialization

    stop_game = False
    while not stop_game:

        if player.isDead():
            stop_game = True

        #  Event handling

        for event in pg.event.get():

            if event.type == pg.QUIT:
                stop_game = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q and pg.key.get_mods() & pg.KMOD_META:
                    stop_game = True
                elif event.key == pg.K_SPACE:
                    player.harvest(harvestable_group, terrain_group)
                elif event.key == pg.K_a:
                    player.buildArmor()
                elif event.key == pg.K_h:
                    player.buildHouse([player.rect.x, player.rect.y],
                                      harvestable_group,
                                      mob_group, house_group)
                else:
                    player.move(event.key)

            if event.type == move_event:
                for mob in mob_group.sprites():
                    mob.move(player, house_group)

            if event.type == mob_spawn_event:
                mob_group.add(Mob())

        # Game logic
        mob_contact = pg.sprite.spritecollide(player, mob_group, True)
        if mob_contact:
            player.takeDamage()

        terrain_group.update()
        house_group.update()
        player_group.update()
        mob_group.update()

        # Game display
        terrain_group.draw(screen)
        house_group.draw(screen)
        player_group.draw(screen)
        mob_group.draw(screen)

        display_status(screen, player)

        pg.display.update()

        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
