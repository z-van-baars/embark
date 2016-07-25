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


def distance(a, b, x, y):
    a1 = abs(a - x)
    b1 = abs(b - y)
    c = math.sqrt((a1 * a1) + (b1 * b1))
    return c


def get_vector(self, a, b, x, y):
    distance_to_target = distance(a, b, x, y)
    factor = distance_to_target / self.speed
    x_dist = a - x
    y_dist = b - y
    change_x = x_dist / factor
    change_y = y_dist / factor
    change_x = round(change_x)
    change_y = round(change_y)

    return (change_x, change_y)


def calculate_step(self):
    x_dist = self.tile_x - self.path.tiles[0].column
    y_dist = self.tile_y - self.path.tiles[0].row
    if abs(x_dist) > abs(y_dist):
        if x_dist < 0:
            self.change_x = 1
        elif x_dist > 0:
            self.change_x = -1
    elif abs(x_dist) < abs(y_dist):
        if y_dist < 0:
            self.change_y = 1
        elif y_dist > 0:
            self.change_y = -1
    else:
        if y_dist < 0:
            self.change_y = 1
        elif y_dist > 0:
            self.change_y = -1
        if x_dist < 0:
            self.change_x = 1
        elif x_dist > 0:
            self.change_x = -1


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


def get_path(self):
    if self.target_object:
        target_x = self.target_object.tile_x
        target_y = self.target_object.tile_y
    else:
        target_x = self.target_coordinates[0]
        target_y = self.target_coordinates[1]

    target_tile = self.current_map.game_tile_rows[target_y][target_x]
    start_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
    
    target_distance = distance(start_tile.column, start_tile.row, target_x, target_y)
    tiles_to_process = {start_tile: (0, target_distance, start_tile, start_tile)}
    visited = {start_tile: True}

    tile_neighbors = get_adjacent_tiles(start_tile, self.current_map)
    current_frontier = []
    for each in tile_neighbors:
        current_frontier.append((each, start_tile))
    steps = 0
    while target_tile not in visited:
        next_frontier = []
        steps += 1
        for tile in current_frontier:
            current_tile = tile[0]
            previous_tile = tile[1]
            if current_tile not in visited:
                if self.check_next_tile(current_tile):
                    distance_to_target = distance(current_tile.column, current_tile.row, target_x, target_y)
                    tiles_to_process[current_tile] = (steps, distance_to_target, current_tile, previous_tile)
                    tile_neighbors = get_adjacent_tiles(current_tile, self.current_map)
                    for each in tile_neighbors:
                        entry = (each, current_tile)
                        next_frontier.append(entry)
                visited[current_tile] = True
        current_frontier = next_frontier
    new_path = Path()
    new_path.tiles.append(target_tile)
    new_path.steps.append(tiles_to_process[target_tile][3])

    while start_tile not in new_path.tiles:
        next_tile = new_path.steps[-1]
        if next_tile != start_tile:
            new_path.steps.append(tiles_to_process[next_tile][3])
        new_path.tiles.append(next_tile)
    new_path.tiles.reverse()
    new_path.tiles.pop(0)
    new_path.steps.reverse()
    new_path.steps.pop(0)

    return new_path
