import pygame
import math
import random
import pickle

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Embark v 0.3")


class GameState(object):
    def __init__(self, screen_width, screen_height, tile_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clock = pygame.time.Clock()
        self.time = 0
        self.font = pygame.font.SysFont('Calibri', 18, True, False)
        self.debug_status = None
        self.tile_size = tile_size
        self.player = None
        self.maps = {}
        self.active_map = None
        self.reset_surfaces()

    def reset_surfaces(self):
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])


class Colors(object):
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.light_grey = (194, 194, 194)
        self.light_green = (0, 210, 0)
        self.dark_green = (0, 200, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.bright_blue = (8, 248, 252)
        self.blue_grey = (180, 210, 217)
        self.purple = (255, 0, 255)
        self.wheat_gold = (220, 187, 0)
        self.key = (255, 0, 128)
        self.brown = (112, 87, 46)
        self.equipped_item_red = (110, 0, 0)

        self.worthless = (148, 25, 25)
        self.shabby = (148, 82, 25)
        self.acceptable = (216, 168, 21)
        self.ordinary = (80, 161, 32)
        self.fine = (25, 76, 148)
        self.resplendent = (0, 177, 186)
        self.titanic = (148, 25, 146)

colors = Colors()


class Path(object):
    def __init__(self):
        self.tiles = []
        self.steps = []


def on_screen(screen_width, screen_height, x_position, y_position, x_shift, y_shift):
    if 0 <= x_position + x_shift <= screen_width and 0 <= y_position + y_shift <= screen_height - 80:
        return True
    else:
        return False


def any_tile_visible(screen_width, screen_height, x_shift, y_shift, entity):
    initial_x = entity.tile_x
    initial_y = entity.tile_y - (entity.footprint[1] - 1)
    for tile_y in range(initial_y, initial_y + (entity.footprint[1])):
        for tile_x in range(initial_x, initial_x + entity.footprint[0]):
            if on_screen(screen_width, screen_height, tile_x * 20, tile_y * 20, x_shift, y_shift):
                return True
    return False


def get_random_coordinates(x_lower, x_upper, y_lower, y_upper):
        x_position = random.randint(x_lower, x_upper)
        y_position = random.randint(y_lower, y_upper)
        return (x_position, y_position)


def export_game_state(game_state):
    print("Exporting Game State......")
    game_state.clock = None
    pickle.dump(game_state, open("saves/save_1.p", "wb"))
    game_state.clock = pygame.time.Clock()
    print("Done")


def import_game_state():
    print("Importing Game State......")
    imported_game_state = pickle.load(open("saves/save_1.p", "rb"))
    imported_game_state.clock = pygame.time.Clock()
    imported_game_state.reset_surfaces()
    imported_game_state.debug_status.reset_surfaces()
    for each in imported_game_state.maps:
        restore_surfaces(imported_game_state.maps[each])
    print("Done")
    return imported_game_state


def restore_surfaces(imported_map):
    imported_map.map_generation()
    for entity_list in imported_map.entity_group:
        for entity in imported_map.entity_group[entity_list]:
            entity.set_images()
            if hasattr(entity, 'items_list'):
                for each in entity.items_list:
                    each.set_surfaces()
            entity.current_tile = None
            entity.assign_tile()


def any_tile_blocked(tile, active_map, entity):
    initial_x = tile.column
    initial_y = tile.row - (entity.footprint[1] - 1)
    for tile_y in range(initial_y, initial_y + (entity.footprint[1])):
        for tile_x in range(initial_x, initial_x + entity.footprint[0]):
            if within_map(tile_x, tile_y, active_map):
                if active_map.game_tile_rows[tile_y][tile_x].is_occupied():
                    return True
            else:
                return True
    return False


def footprint_visible(screen, active_map, entity):
    initial_x = entity.tile_x
    initial_y = entity.tile_y - (entity.footprint[1] - 1)
    for tile_y in range(initial_y, initial_y + (entity.footprint[1])):
        for tile_x in range(initial_x, initial_x + entity.footprint[0]):
            if active_map.game_tile_rows[tile_y][tile_x].is_occupied():
                return True
    return False


def distance(a, b, x, y):
    a1 = abs(a - x)
    b1 = abs(b - y)
    c = math.sqrt((a1 * a1) + (b1 * b1))
    return c

# function for N repeated rolls of random(S+1), returning a number from 0 to N*S
def roll_dice(number_of_dice, sides):
    # Sum of N dice each of which goes from 0 to sides
    value = 0
    for i in range(number_of_dice):
        value += random.randint(1, sides)
    return value


def get_nearby_tiles(current_map, center, radius):
    nearby_tiles = []
    x = center[0]
    y = center[1]
    for tile_y in range((y - radius), (y + radius)):
        for tile_x in range((x - radius), (x + radius)):
            if within_map(tile_x, tile_y, current_map):
                distance_from_center = distance(tile_x, tile_y, center[0], center[1])
                if distance_from_center <= radius:
                    nearby_tiles.append(current_map.game_tile_rows[tile_y][tile_x])
    return nearby_tiles


def within_map(x, y, current_map):
    return 0 <= x <= len(current_map.game_tile_rows[0]) - 1 and 0 <= y <= len(current_map.game_tile_rows) - 1


def get_adjacent_tiles(tile, current_map):
    initial_x = tile.column - 1
    initial_y = tile.row - 1
    adjacent_tiles = []
    for tile_y in range(initial_y, initial_y + 3):
        for tile_x in range(initial_x, initial_x + 3):
            if within_map(tile_x, tile_y, current_map):
                adjacent_tiles.append(current_map.game_tile_rows[tile_y][tile_x])
    return adjacent_tiles


def get_adjacent_movement_tiles(tile, current_map):
    initial_x = tile.column - 1
    initial_y = tile.row - 1
    adjacent_tiles = []
    for tile_y in range(initial_y, initial_y + 3):
        for tile_x in range(initial_x, initial_x + 3):
            if within_map(tile_x, tile_y, current_map):
                adjacent_tiles.append(current_map.game_tile_rows[tile_y][tile_x])
    return adjacent_tiles


def check_if_inside(x1, x2, y1, y2, pos):
    return x1 < pos[0] < x2 and y1 < pos[1] < y2


def get_vector(self, a, b, x, y):
    distance_to_target = distance(a, b, x, y)
    factor = distance_to_target / self.speed
    x_dist = a - x
    y_dist = b - y
    change_x = x_dist / factor
    change_y = y_dist / factor

    return (change_x, change_y)


