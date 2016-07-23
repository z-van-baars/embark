import pygame
import random
import utilities
from utilities import GlobalVariables
from tile import DisplayTile
from buffalo import Buffalo
from wheat import Wheat
from game_map import Map


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
    while not done:
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

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    super_scroll = 1

        for tile in new_map.display_tiles:
            global_variables.screen.blit(tile.image, [(tile.rect.x + new_map.x_shift), (tile.rect.y + new_map.y_shift)])
        for vegetation in new_map.entity_group[Wheat]:
            vegetation.tick_cycle()
            global_variables.screen.blit(
                vegetation.image,
                [(vegetation.rect.x + new_map.x_shift),
                    (vegetation.rect.y + new_map.y_shift)])
        for herd in new_map.herds:
            herd.check_food_supply()

        for animal in new_map.entity_group[Buffalo]:
            animal.tick_cycle()
            global_variables.screen.blit(animal.image, [(animal.rect.x + new_map.x_shift), (animal.rect.y + new_map.y_shift)])

        pygame.display.flip()
        global_variables.clock.tick(60)
        global_variables.time += 1

global_variables = GlobalVariables(700, 700)

world_dimensions = (70, 70)

main(global_variables, world_dimensions)

