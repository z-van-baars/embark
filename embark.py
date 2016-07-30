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
import debug


def select_world_size(world_size_candidates):
    world_size_not_selected = True
    while world_size_not_selected:
        while True:
            try:
                print("World Size? 1 - 2 - 3 - 4")
                size_selected = int(input("? "))
                size_selected -= 1
                break
            except ValueError:
                print("Invalid world size")
                pass
        if size_selected in range(0, len(world_size_candidates)):
            world_dimensions = world_size_candidates[size_selected]
            return world_dimensions
        else:
            print("Invalid world size, try again")


def main(global_variables, map_dimensions):
    new_map = Map(world_dimensions)
    new_map.map_generation()
    done = False
    super_scroll = 1
    debug_stats = debug.DebugStatus(new_map, global_variables)
    debug_stats.tile_selector_graphic = debug.TileSelectorGraphic(0, 0, new_map)
    global_variables.debug_status = debug_stats
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

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    super_scroll = 1
                elif event.key == pygame.K_LCTRL:
                    control_on = False

        for tile in new_map.display_tiles:
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, tile.rect.x, tile.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(tile.image, [(tile.rect.x + new_map.x_shift), (tile.rect.y + new_map.y_shift)])
        for terrain in new_map.entity_group[Wall]:
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, terrain.rect.x, terrain.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(terrain.image, [(terrain.rect.x + new_map.x_shift), (terrain.rect.y + new_map.y_shift)])

        for wheat in new_map.entity_group[Wheat]:
            wheat.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, wheat.rect.x, wheat.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(
                    wheat.image,
                    [(wheat.rect.x + new_map.x_shift),
                        (wheat.rect.y + new_map.y_shift)])
        for herd in new_map.herds:
            herd.check_food_supply()

        for animal in new_map.entity_group[Buffalo]:
            animal.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, animal.rect.x, animal.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(animal.image, [(animal.rect.x + new_map.x_shift), (animal.rect.y + new_map.y_shift)])

        for tree in new_map.entity_group[Tree]:
            tree.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, tree.rect.x, tree.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(
                    tree.image,
                    [(tree.rect.x + new_map.x_shift),
                        (tree.rect.y + new_map.y_shift)])

        if debug_stats.debug:
            for each in new_map.entity_group[Buffalo]:
                each.search_area_graphic = debug.FoodSearchRadius(new_map, each)
            debug_stats.tile_selector_graphic.update_image(mouse_pos)
            debug_stats.print_to_screen()
            if debug_stats.remove or debug_stats.entity_to_place:
                pygame.draw.rect(global_variables.screen, (255, 255, 255), debug_stats.tile_selector_graphic.image, 1)

        pygame.display.flip()
        global_variables.clock.tick(60)
        global_variables.time += 1

global_variables = GlobalVariables(700, 700)

world_dimensions = (70, 70)

main(global_variables, world_dimensions)

