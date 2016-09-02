import pygame
import random
import utilities
from utilities import GlobalVariables
from tile import DisplayTile
from buffalo import Buffalo
from wheat import Wheat
from game_map import Map
from tree import Tree
from wall import Wall
from avatar import Avatar
import debug

pygame.init()
pygame.display.set_mode([0, 0])

lower_left = pygame.image.load("art/ui_elements/lower_left.png").convert()
bag = pygame.image.load("art/ui_elements/bag.png").convert()
bag_selected = pygame.image.load("art/ui_elements/bag_highlight.png").convert()


def set_bottom_pane_stamp(current_map, mouse_pos):
    font = pygame.font.SysFont('Calibri', 18, True, False)
    tile_x = int((mouse_pos[0] + current_map.x_shift) / 10)
    tile_y = int((mouse_pos[1] + current_map.y_shift) / 10)

    if utilities.within_map(tile_x, tile_y, current_map):
        selected_tile = current_map.game_tile_rows[tile_y][tile_x]
        if selected_tile.is_occupied():
            for entity_type in selected_tile.entity_group:
                if entity_type.occupies_tile:
                    if selected_tile.entity_group[entity_type]:
                        entity = selected_tile.entity_group[entity_type][0]
                        stamp = font.render(entity.display_name, True, utilities.colors.black)
            return stamp
    else:
        return None


def main(global_variables, map_dimensions):
    new_map = Map(map_dimensions)
    new_map.map_generation()
    done = False
    super_scroll = 1
    debug_stats = debug.DebugStatus(new_map, global_variables)
    debug_stats.tile_selector_graphic = debug.TileSelectorGraphic(0, 0, new_map)
    global_variables.debug_status = debug_stats
    bottom_pane = pygame.sprite.Sprite()
    bottom_pane.image = pygame.Surface([global_variables.screen_width - 280, 80])
    bottom_pane.image.fill((171, 171, 171))
    control_on = False
    while not done:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_map.world_scroll(0, (10 * super_scroll), global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_DOWN:
                    new_map.world_scroll(0, (-10 * super_scroll), global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_LEFT:
                    new_map.world_scroll((10 * super_scroll), 0, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_RIGHT:
                    new_map.world_scroll((-10 * super_scroll), 0, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_LSHIFT:
                    super_scroll = 10
                elif event.key == pygame.K_LCTRL:
                    control_on = True

                elif event.key == pygame.K_SPACE:
                    paused = True
                    while paused:
                        for new_event in pygame.event.get():
                            if new_event.type == pygame.QUIT:
                                paused = False
                                done = True
                            elif new_event.type == pygame.KEYDOWN:
                                if new_event.key == pygame.K_SPACE:
                                    paused = False
                elif event.key == pygame.K_d and control_on:
                    if not debug_stats.debug:
                        debug_stats.debug = True
                    else:
                        debug_stats.debug = False
                        debug_stats.entity_to_place = None
                        debug_stats.current_placement_entity_number = 0
                        debug_stats.clear = False
                        debug_stats.remove = False
                        debug_stats.current_removal_entity_number = 0

                if debug_stats.debug:
                    debug.event_processing(new_map, global_variables.debug_status, event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if debug_stats.debug:
                    debug.mouse_processing(new_map, global_variables.debug_status, mouse_pos, event)
                else:
                    new_map.entity_group[Avatar][0].assign_target(new_map, mouse_pos)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    super_scroll = 1
                elif event.key == pygame.K_LCTRL:
                    control_on = False

        bottom_pane_stamp = set_bottom_pane_stamp(new_map, mouse_pos)

        for tile in new_map.display_tiles:
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, tile.rect.x, tile.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(tile.image, [(tile.rect.x + new_map.x_shift), (tile.rect.y + new_map.y_shift)])
        for terrain in new_map.entity_group[Wall]:
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, terrain.sprite.rect.x, terrain.sprite.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(terrain.sprite.image, [(terrain.sprite.rect.x + new_map.x_shift), (terrain.sprite.rect.y + new_map.y_shift)])
        for wheat in new_map.entity_group[Wheat]:
            wheat.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, wheat.sprite.rect.x, wheat.sprite.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(
                    wheat.sprite.image,
                    [(wheat.sprite.rect.x + new_map.x_shift),
                        (wheat.sprite.rect.y + new_map.y_shift)])

        for animal in new_map.entity_group[Buffalo]:
            animal.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, animal.sprite.rect.x, animal.sprite.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(animal.sprite.image, [(animal.sprite.rect.x + new_map.x_shift), (animal.sprite.rect.y + new_map.y_shift)])

        for avatar in new_map.entity_group[Avatar]:
            avatar.tick_cycle()
            global_variables.screen.blit(avatar.sprite.image, [(avatar.sprite.rect.x + new_map.x_shift), (avatar.sprite.rect.y + new_map.y_shift)])

        for tree in new_map.entity_group[Tree]:
            tree.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, tree.sprite.rect.x, tree.sprite.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(
                    tree.sprite.image,
                    [(tree.sprite.rect.x + new_map.x_shift),
                        (tree.sprite.rect.y + new_map.y_shift)])

        global_variables.screen.blit(lower_left, [0, global_variables.screen_height - 80])
        global_variables.screen.blit(bottom_pane.image, [200, global_variables.screen_height - 79])

        if mouse_pos[0] > global_variables.screen_width - 80 and mouse_pos[1] > global_variables.screen_height - 80:
            bag_image = bag_selected
        else:
            bag_image = bag
        global_variables.screen.blit(bag_image, [global_variables.screen_width - 80, global_variables.screen_height - 80])

        if bottom_pane_stamp and not debug_stats.debug:
            global_variables.screen.blit(bottom_pane_stamp, [210, global_variables.screen_height - 60])

        if debug_stats.debug:
            for each in new_map.entity_group[Buffalo]:
                each.search_area_graphic = debug.FoodSearchRadius(new_map, each)
            debug_stats.tile_selector_graphic.update_image(mouse_pos)
            debug_stats.print_to_screen(global_variables.screen)
            if debug_stats.remove or debug_stats.entity_to_place:
                pygame.draw.rect(global_variables.screen, (255, 255, 255), debug_stats.tile_selector_graphic.image, 1)

        pygame.display.flip()
        global_variables.clock.tick(60)
        global_variables.time += 1

global_variables = GlobalVariables(1000, 700 + 80)

world_dimensions = (100, 70)

main(global_variables, world_dimensions)

