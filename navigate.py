import random
import math
import utilities


def distance(a, b, x, y):
    a1 = abs(a - x)
    b1 = abs(b - y)
    c = math.sqrt((a1 * a1) + (b1 * b1))
    return c


def calculate_step(my_position, next_tile):
    x_dist = my_position[0] - next_tile.column
    y_dist = my_position[1] - next_tile.row
    if abs(x_dist) > abs(y_dist):
        if x_dist < 0:
            change_x = 1
        elif x_dist > 0:
            change_x = -1
    elif abs(x_dist) < abs(y_dist):
        if y_dist < 0:
            change_y = 1
        elif y_dist > 0:
            change_y = -1
    else:
        if y_dist < 0:
            change_y = 1
        elif y_dist > 0:
            change_y = -1
        if x_dist < 0:
            change_x = 1
        elif x_dist > 0:
            change_x = -1
    return change_x, change_y


def explore_frontier_to_target(game_map, visited, target_tile, current_frontier, tiles_to_process, incompatible_objects):
    steps = 0
    while target_tile not in visited:
        next_frontier = []
        steps += 1
        for tile in current_frontier:
            current_tile = tile[0]
            previous_tile = tile[1]
            if current_tile not in visited:
                if utilities.tile_is_valid(game_map, current_tile.column, current_tile.row, incompatible_objects):
                    distance_to_target = distance(current_tile.column, current_tile.row, target_tile.column, target_tile.row)
                    tiles_to_process[current_tile] = (steps, distance_to_target, current_tile, previous_tile)
                    tile_neighbors = utilities.get_adjacent_tiles(current_tile, game_map)
                    for each in tile_neighbors:
                        entry = (each, current_tile)
                        next_frontier.append(entry)
                    visited[current_tile] = True
        current_frontier = next_frontier
    return visited, tiles_to_process


def get_path(my_position, game_map, target_coordinates, incompatible_objects):

        target_tile = game_map.game_tile_rows[target_coordinates[1]][target_coordinates[0]]
        start_tile = game_map.game_tile_rows[my_position[1]][my_position[0]]
        target_distance = distance(start_tile.column, start_tile.row, target_coordinates[0], target_coordinates[1])
        tiles_to_process = {start_tile: (0, target_distance, start_tile, start_tile)}
        visited = {start_tile: True}

        tile_neighbors = utilities.get_adjacent_tiles(start_tile, game_map)
        current_frontier = []
        for each in tile_neighbors:
            current_frontier.append((each, start_tile))

        visited, tiles_to_process = explore_frontier_to_target(game_map, visited, target_tile, current_frontier, tiles_to_process, incompatible_objects)

        new_path = utilities.Path()
        new_path.tiles.append(target_tile)
        new_path.steps.append(tiles_to_process[target_tile][3])

        while start_tile not in new_path.tiles:
            next_tile = new_path.steps[-1]
            if next_tile != start_tile:
                new_path.steps.append(tiles_to_process[next_tile][3])
            new_path.tiles.append(next_tile)
        new_path.tiles.reverse()
        # removes the start tile from the tiles list and the steps list in the path object
        new_path.tiles.pop(0)
        new_path.steps.reverse()
        new_path.steps.pop(0)

        return new_path

