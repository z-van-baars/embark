import pygame
import random
import utilities
from utilities import GlobalVariables
from tile import Tile
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
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_map.world_scroll(0, 10, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_DOWN:
                    new_map.world_scroll(0, -10, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_LEFT:
                    new_map.world_scroll(10, 0, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_RIGHT:
                    new_map.world_scroll(-10, 0, global_variables.screen_width, global_variables.screen_height)

        for tile in new_map.tiles:
            global_variables.screen.blit(tile.image, [(tile.rect.x + new_map.x_shift), (tile.rect.y + new_map.y_shift)])
        for vegetation in new_map.vegetation_group:
            global_variables.screen.blit(vegetation.image, [(vegetation.rect.x + new_map.x_shift), (vegetation.rect.y + new_map.y_shift)])
        for animal in new_map.animals_group:
            animal.do_thing()
            global_variables.screen.blit(animal.image, [(animal.rect.x + new_map.x_shift), (animal.rect.y + new_map.y_shift)])

        pygame.display.flip()
        global_variables.clock.tick(60)
        global_variables.time += 1

world_sizes = [(20, 20), (50, 50), (100, 100), (1000, 1000)]
global_variables = GlobalVariables(600, 600)

grass_1 = ("Grass 1", (utilities.colors.light_green))
grass_2 = ("Grass 2", (utilities.colors.dark_green))

terrain_types = [grass_1, grass_2]


world_dimensions = (100, 100)

main(global_variables, world_dimensions)

