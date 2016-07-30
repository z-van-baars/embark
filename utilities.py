import pygame
import math

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Embark v 0.21")


class GlobalVariables(object):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.clock = pygame.time.Clock()
        self.time = 0
        self.font = pygame.font.SysFont('Calibri', 18, True, False)
        self.debug_status = None


class Colors(object):
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.light_green = (0, 210, 0)
        self.dark_green = (0, 200, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.blue_grey = (180, 210, 217)
        self.purple = (255, 0, 255)
        self.wheat_gold = (220, 187, 0)
        self.key = (255, 0, 128)
        self.brown = (112, 87, 46)

colors = Colors()


class Path(object):
    def __init__(self):
        self.tiles = []
        self.steps = []


def on_screen(screen_width, screen_height, x_position, y_position, x_shift, y_shift):
    if 0 <= x_position + x_shift <= screen_width and 0 <= y_position + y_shift <= screen_height:
        return True
    else:
        return False

def distance(a, b, x, y):
    a1 = abs(a - x)
    b1 = abs(b - y)
    c = math.sqrt((a1 * a1) + (b1 * b1))
    return c


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


def tile_is_valid(game_map, next_tile_x, next_tile_y, incompatible_objects):
    tile = game_map.game_tile_rows[next_tile_y][next_tile_x]
    for object_type in incompatible_objects:
        if len(tile.entity_group[object_type]) > 0:
            return False
    return True
