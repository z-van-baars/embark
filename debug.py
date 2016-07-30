import pygame
import random
import utilities
from buffalo import Buffalo
from wheat import Wheat
from wall import Wall
from tree import Tree


animal_types = [Buffalo]
vegetation_types = [Wheat, Tree]
terrain_types = [Wall]


class TileSelectorGraphic(pygame.sprite.Sprite):
    def __init__(self, x, y, current_map):
        super().__init__()
        self.tile_x = x
        self.tile_y = y
        self.current_map = current_map

        self.update_image((0, 0))

    def update_image(self, mouse_pos):
        self.tile_x = int(mouse_pos[0] + self.current_map.x_shift) / 10
        self.tile_y = int(mouse_pos[1] + self.current_map.y_shift) / 10
        self.image = pygame.Rect((int(mouse_pos[0] / 10) * 10), (int(mouse_pos[1] / 10) * 10), 10, 10)


class TileMarker(pygame.sprite.Sprite):
    def __init__(self, x, y, current_map):
        super().__init__()
        self.tile_x = x
        self.tile_y = y
        self.current_map = current_map

        self.update_image()

    def update_image(self):

        top = int(self.tile_y * 10) + self.current_map.y_shift
        left = int(self.tile_x * 10) + self.current_map.x_shift
        self.image = pygame.Rect(left, top, 10, 10)


class FoodSearchRadius(pygame.sprite.Sprite):
    def __init__(self, current_map, entity):
        super().__init__()
        self.current_map = current_map
        self.entity = entity
        self.center = (entity.rect.x, entity.rect.y)
        self.radius = (self.entity.sight_range * 10)

        self.update_stats()

    def update_stats(self):
        self.center = (self.entity.rect.x + 5 + self.current_map.x_shift, self.entity.rect.y + 5 + self.current_map.y_shift)
        self.radius = (self.entity.sight_range * 10)


def event_processing(current_map, debug_status, event_key):
    if event_key == pygame.K_c:
        if debug_status.remove:
            debug_status.remove = False
            debug_status.current_removal_entity_number = 0
        if debug_status.clear:
            debug_status.clear = False
        else:
            debug_status.clear = True
            debug_status.entity_to_place = None
    elif event_key == pygame.K_s:
        if not debug_status.draw_search_areas:
            debug_status.draw_search_areas = True
        else:
            debug_status.draw_search_areas = False
    elif event_key == pygame.K_p:
        if not debug_status.draw_paths:
            debug_status.draw_paths = True
        else:
            debug_status.draw_paths = False

    elif event_key == pygame.K_a and debug_status.clear:
        clear_all_animals(current_map)
    elif event_key == pygame.K_a and debug_status.remove:
        debug_status.current_removal_entity_number = 1

    elif event_key == pygame.K_v and debug_status.clear:
        clear_all_vegetation(current_map)
    elif event_key == pygame.K_v and debug_status.remove:
        debug_status.current_removal_entity_number = 2

    elif event_key == pygame.K_e and debug_status.clear:
        clear_all_entities(current_map)
    elif event_key == pygame.K_e and debug_status.remove:
        debug_status.current_removal_entity_number = 4

    elif event_key == pygame.K_t and debug_status.clear:
        clear_all_terrain(current_map)
    elif event_key == pygame.K_t and debug_status.remove:
        debug_status.current_removal_entity_number = 3

    elif event_key == pygame.K_r:
        if debug_status.remove:
            debug_status.remove = False
            debug_status.current_removal_entity_number = 0
        else:
            if debug_status.clear:
                debug_status.clear = False
            if debug_status.entity_to_place:
                debug_status.entity_to_place = None
            debug_status.remove = True
    elif event_key == pygame.K_b:
        if debug_status.clear:
            debug_status.clear = False
        if debug_status.remove:
            debug_status.remove = False
            debug_status.current_removal_entity_number = 0
        debug_status.entity_to_place = Buffalo
        debug_status.current_placement_entity_number = 2
    elif event_key == pygame.K_w:
        if debug_status.clear:
            debug_status.clear = False
        if debug_status.remove:
            debug_status.remove = False
            debug_status.current_removal_entity_number = 0
        debug_status.entity_to_place = Wheat
        debug_status.current_placement_entity_number = 1
    elif event_key == pygame.K_l:
        if debug_status.clear:
            debug_status.clear = False
        if debug_status.remove:
            debug_status.remove = False
            debug_status.current_removal_entity_number = 0
        debug_status.entity_to_place = Wall
        debug_status.current_placement_entity_number = 3
    elif event_key == pygame.K_n:
        if debug_status.clear:
            debug_status.clear = False
        if debug_status.remove:
            debug_status.remove = False
            debug_status.current_removal_entity_number = 0
        debug_status.entity_to_place = Tree
        debug_status.current_placement_entity_number = 4


def mouse_processing(current_map, debug_status, mouse_pos, event):
    tile_x = int((mouse_pos[0] + current_map.x_shift) / 10)
    tile_y = int((mouse_pos[1] + current_map.y_shift) / 10)
    selected_tile = current_map.game_tile_rows[tile_y][tile_x]
    if debug_status.entity_to_place:
        if event.type == pygame.MOUSEBUTTONDOWN:
            debug_status.entity_to_place(selected_tile.column, selected_tile.row, current_map)
            # if not utilities.tile_is_valid(current_map, selected_tile.column, selected_tile.row, new_entity.incompatible_objects):
                # new_entity.expire()
    if debug_status.current_removal_entity_number != 0:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if debug_status.current_removal_entity_number == 1:
                remove_animals_at_tile(current_map, selected_tile)
            elif debug_status.current_removal_entity_number == 2:
                remove_vegetation_at_tile(current_map, selected_tile)
            elif debug_status.current_removal_entity_number == 4:
                remove_animals_at_tile(current_map, selected_tile)
                remove_vegetation_at_tile(current_map, selected_tile)
            elif debug_status.current_removal_entity_number == 3:
                remove_terrain_at_tile(current_map, selected_tile)


def clear_all_entities(current_map):
    clear_all_animals(current_map)
    clear_all_vegetation(current_map)


def clear_all_animals(current_map):
    for animal in animal_types:
        for each in current_map.entity_group[animal]:
            each.current_tile.entity_group[animal].remove(each)
        current_map.entity_group[animal] = pygame.sprite.Group()
    current_map.herds = []


def clear_all_terrain(current_map):
    for terrain in terrain_types:
        for each in current_map.entity_group[terrain]:
            each.current_tile.entity_group[terrain].remove(each)
        current_map.entity_group[terrain] = pygame.sprite.Group()


def clear_all_vegetation(current_map):
    for vegetation in vegetation_types:
        for each in current_map.entity_group[vegetation]:
            each.current_tile.entity_group[vegetation].remove(each)
        current_map.entity_group[vegetation] = pygame.sprite.Group()


def remove_vegetation_at_tile(current_map, current_tile):
    for vegetation in vegetation_types:
        for each in current_tile.entity_group[vegetation]:
            current_tile.entity_group[vegetation].remove(each)
            current_map.entity_group[vegetation].remove(each)


def remove_terrain_at_tile(current_map, current_tile):
    for terrain in terrain_types:
        for each in current_tile.entity_group[terrain]:
            current_tile.entity_group[terrain].remove(each)
            current_map.entity_group[terrain].remove(each)


def remove_animals_at_tile(current_map, current_tile):
    for animal in animal_types:
        for each in current_tile.entity_group[animal]:
            current_tile.entity_group[animal].remove(each)
            current_map.entity_group[animal].remove(each)


class DebugStatus(object):
    def __init__(self, current_map, global_variables):
        self.font = pygame.font.SysFont('Calibri', 18, True, False)
        self.current_map = current_map
        self.global_variables = global_variables
        self.debug = False
        self.clear = False
        self.remove = False
        self.entity_to_place = None
        self.draw_search_areas = False
        self.draw_paths = False
        self.entity_strings = ["None", "Wheat", "Buffalo", "Wall", "Tree"]
        self.current_placement_entity_number = 0
        self.path_stamp = self.font.render("Drawing Paths", True, utilities.colors.black)

        self.entity_type_strings = ["None", "Animals", "Vegetation", "Terrain", "All"]
        self.current_removal_entity_number = 0

        debug = self.font.render("Debug Mode", True, utilities.colors.black)
        item_to_place = self.font.render("Placing Item: ", True, utilities.colors.black)
        clear_stamp = self.font.render("Clear Items: All [E]ntities / All [A]nimals / All [V]egetation / All [T]errain", True, utilities.colors.black)
        removal_stamp = self.font.render("Click to remove from tile at cursor: ", True, utilities.colors.black)
        removal_types_stamp = self.font.render("[A]nimals / [V]egetation / All [E]ntities", True, utilities.colors.black)
        self.stamps = [
                        ((10, 10), debug),
                        ((10, 25), item_to_place),
                        ((10, 25), clear_stamp),
                        ((10, 25), removal_stamp),
                        ((280, 25), removal_types_stamp)
                    ]
        self.update_entity_stamp()

    def update_entity_stamp(self):
        self.entity_stamp = self.font.render(self.entity_strings[self.current_placement_entity_number], True, utilities.colors.black)

    def update_item_removal_stamp(self):
        self.item_removal_stamp = self.font.render(self.entity_type_strings[self.current_removal_entity_number], True, utilities.colors.black)

    def print_to_screen(self):
        self.global_variables.screen.blit(self.stamps[0][1], self.stamps[0][0])
        if self.clear:
            self.global_variables.screen.blit(self.stamps[2][1], self.stamps[2][0])
        if self.entity_to_place:
            self.update_entity_stamp()
            self.global_variables.screen.blit(self.stamps[1][1], self.stamps[1][0])
            self.global_variables.screen.blit(self.entity_stamp, [115, 25])
        if self.remove:
            self.update_item_removal_stamp()
            self.global_variables.screen.blit(self.stamps[3][1], self.stamps[3][0])
            if self.current_removal_entity_number != 0:
                self.global_variables.screen.blit(self.item_removal_stamp, [280, 25])
            else:
                self.global_variables.screen.blit(self.stamps[4][1], self.stamps[4][0])
        if self.global_variables.debug_status.draw_search_areas:
            for each in self.current_map.entity_group[Buffalo]:
                new_search_area_graphic = FoodSearchRadius(self.current_map, each)
                new_search_area_graphic.update_stats()
                pygame.draw.circle(self.global_variables.screen, (0, 0, 0), new_search_area_graphic.center, new_search_area_graphic.radius, 1)
        if self.global_variables.debug_status.draw_paths:
            self.global_variables.screen.blit(self.path_stamp, [10, 40])
            for each in self.current_map.entity_group[Buffalo]:
                if each.path:
                    for tile in each.path.tiles:
                        marker = TileMarker(tile.column, tile.row, self.current_map)
                        marker.update_image()
                        pygame.draw.rect(self.global_variables.screen, (255, 0, 255), marker.image, 1)



