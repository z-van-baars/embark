import pygame
import random
import utilities
from buffalo import Buffalo
from wheat import Wheat
from wall import Wall


animal_types = [Buffalo]
vegetation_types = [Wheat]
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

        self.update_image()

    def update_image(self):
        top = self.entity.tile_y * 10 - self.entity.vertical_sight * 10
        top += self.current_map.y_shift
        left = self.entity.tile_x * 10 - self.entity.horizontal_sight * 10
        left += self.current_map.x_shift
        width = self.entity.horizontal_sight * 20
        height = self.entity.vertical_sight * 20
        self.image = pygame.Rect(left, top, width, height)


def event_processing(current_map, global_variables, event_key):
    if event_key == pygame.K_c:
        if global_variables.debug_status.remove:
            global_variables.debug_status.remove = False
            global_variables.debug_status.current_removal_entity_number = 0
        if global_variables.debug_status.clear:
            global_variables.debug_status.clear = False
        else:
            global_variables.debug_status.clear = True
            global_variables.debug_status.entity_to_place = None
    elif event_key == pygame.K_s:
        if not global_variables.debug_status.draw_search_areas:
            global_variables.debug_status.draw_search_areas = True
        else:
            global_variables.debug_status.draw_search_areas = False
    elif event_key == pygame.K_p:
        if not global_variables.debug_status.draw_paths:
            global_variables.debug_status.draw_paths = True
        else:
            global_variables.debug_status.draw_paths = False

    elif event_key == pygame.K_a and global_variables.debug_status.clear:
        clear_all_animals(current_map, global_variables)
    elif event_key == pygame.K_a and global_variables.debug_status.remove:
        global_variables.debug_status.current_removal_entity_number = 1

    elif event_key == pygame.K_v and global_variables.debug_status.clear:
        clear_all_vegetation(current_map, global_variables)
    elif event_key == pygame.K_v and global_variables.debug_status.remove:
        global_variables.debug_status.current_removal_entity_number = 2

    elif event_key == pygame.K_e and global_variables.debug_status.clear:
        clear_all_entities(current_map, global_variables)
    elif event_key == pygame.K_e and global_variables.debug_status.remove:
        global_variables.debug_status.current_removal_entity_number = 4

    elif event_key == pygame.K_t and global_variables.debug_status.clear:
        clear_all_terrain(current_map, global_variables)
    elif event_key == pygame.K_t and global_variables.debug_status.remove:
        global_variables.debug_status.current_removal_entity_number = 3

    elif event_key == pygame.K_r:
        if global_variables.debug_status.remove:
            global_variables.debug_status.remove = False
            global_variables.debug_status.current_removal_entity_number = 0
        else:
            if global_variables.debug_status.clear:
                global_variables.debug_status.clear = False
            if global_variables.debug_status.entity_to_place:
                global_variables.debug_status.entity_to_place = None
            global_variables.debug_status.remove = True
    elif event_key == pygame.K_b:
        if global_variables.debug_status.clear:
            global_variables.debug_status.clear = False
        if global_variables.debug_status.remove:
            global_variables.debug_status.remove = False
            global_variables.debug_stats.current_removal_entity_number = 0
        global_variables.debug_status.entity_to_place = Buffalo
        global_variables.debug_status.current_placement_entity_number = 2
    elif event_key == pygame.K_w:
        if global_variables.debug_status.clear:
            global_variables.debug_status.clear = False
        if global_variables.debug_status.remove:
            global_variables.debug_status.remove = False
            global_variables.debug_status.current_removal_entity_number = 0
        global_variables.debug_status.entity_to_place = Wheat
        global_variables.debug_status.current_placement_entity_number = 1
    elif event_key == pygame.K_l:
        if global_variables.debug_status.clear:
            global_variables.debug_status.clear = False
        if global_variables.debug_status.remove:
            global_variables.debug_status.remove = False
            global_variables.debug_status.current_removal_entity_number = 0
        global_variables.debug_status.entity_to_place = Wall
        global_variables.debug_status.current_placement_entity_number = 3


def mouse_processing(current_map, global_variables, mouse_pos, event):
    tile_x = int((mouse_pos[0] + current_map.x_shift) / 10)
    tile_y = int((mouse_pos[1] + current_map.y_shift) / 10)
    selected_tile = current_map.game_tile_rows[tile_y][tile_x]
    if global_variables.debug_status.entity_to_place:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(selected_tile.entity_group[global_variables.debug_status.entity_to_place]) == 0:
                new_entity = global_variables.debug_status.entity_to_place(selected_tile.column, selected_tile.row, current_map)
                current_map.entity_group[global_variables.debug_status.entity_to_place].add(new_entity)
    if global_variables.debug_status.current_removal_entity_number != 0:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if global_variables.debug_status.current_removal_entity_number == 1:
                remove_animals_at_tile(current_map, global_variables, selected_tile)
            elif global_variables.debug_status.current_removal_entity_number == 2:
                remove_vegetation_at_tile(current_map, global_variables, selected_tile)
            elif global_variables.debug_status.current_removal_entity_number == 4:
                remove_animals_at_tile(current_map, global_variables, selected_tile)
                remove_vegetation_at_tile(current_map, global_variables, selected_tile)
            elif global_variables.debug_status.current_removal_entity_number == 3:
                remove_terrain_at_tile(current_map, global_variables, selected_tile)


def clear_all_entities(current_map, global_variables):
    clear_all_animals(current_map, global_variables)
    clear_all_vegetation(current_map, global_variables)


def clear_all_animals(current_map, global_variables):
    for animal in animal_types:
        for each in current_map.entity_group[animal]:
            each.current_tile.entity_group[animal].remove(each)
        current_map.entity_group[animal] = pygame.sprite.Group()
    current_map.herds = []


def clear_all_terrain(current_map, global_variables):
    for terrain in terrain_types:
        for each in current_map.entity_group[terrain]:
            each.current_tile.entity_group[terrain].remove(each)
        current_map.entity_group[terrain] = pygame.sprite.Group()


def clear_all_vegetation(current_map, global_variables):
    for vegetation in vegetation_types:
        for each in current_map.entity_group[vegetation]:
            each.current_tile.entity_group[vegetation].remove(each)
        current_map.entity_group[vegetation] = pygame.sprite.Group()


def remove_vegetation_at_tile(current_map, global_variables, current_tile):
    for vegetation in vegetation_types:
        for each in current_tile.entity_group[vegetation]:
            current_tile.entity_group[vegetation].remove(each)
            current_map.entity_group[vegetation].remove(each)


def remove_terrain_at_tile(current_map, global_variables, current_tile):
    for terrain in terrain_types:
        for each in current_tile.entity_group[terrain]:
            current_tile.entity_group[terrain].remove(each)
            current_map.entity_group[terrain].remove(each)


def remove_animals_at_tile(current_map, global_variables, current_tile):
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
        self.entity_strings = ["None", "Wheat", "Buffalo", "Wall"]
        self.current_placement_entity_number = 0
        self.path_stamp = self.font.render("Drawing Paths", True, utilities.colors.black)

        self.entity_type_strings = ["None", "Animals", "Vegetation", "Terrain", "All"]
        self.current_removal_entity_number = 0

        debug = self.font.render("Debug Mode", True, utilities.colors.black)
        item_to_place = self.font.render("Placing Item: ", True, utilities.colors.black)
        clear_stamp = self.font.render("Clear Items: All [E]ntities / All [A]nimals / All [V]egetation", True, utilities.colors.black)
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
                pygame.draw.rect(self.global_variables.screen, (0, 0, 0), each.search_area_graphic.image, 1)
        if self.global_variables.debug_status.draw_paths:
            self.global_variables.screen.blit(self.path_stamp, [10, 40])
            for each in self.current_map.entity_group[Buffalo]:
                for tile in each.path.tiles:
                    marker = TileMarker(tile.column, tile.row, self.current_map)
                    marker.update_image()
                    pygame.draw.rect(self.global_variables.screen, (255, 0, 255), marker.image, 1)



