import pygame
import utilities
import entity
import random
from wheat import Wheat
from herd import Herd
from wall import Wall


class Buffalo(entity.Entity):
    def __init__(self, x, y, current_map, herd=None):
        super().__init__(x, y, utilities.colors.red, 6, 6, current_map, Wheat)
        self.speed = 20
        self.time_since_last_move = 0
        self.age = 0
        self.ticks_without_food = 0
        self.change_x = 0
        self.change_y = 0
        self.current_hunger_saturation = 200
        self.hunger_threshold = 400
        self.max_hunger_saturation = 400
        self.horizontal_sight = 5
        self.vertical_sight = 5
        self.migration_target = None
        self.local_food_supply = []
        self.herd_radius = 5
        self.herd = herd
        self.is_alpha = False
        self.alpha_color = (215, 0, 0)

        self.target_coordinates = None
        self.target_object = None
        self.path = None

        self.search_area_graphic = None

        self.min_initial_herd_size = 5
        self.max_initial_herd_size = 10

        self.incompatible_objects = [Buffalo, Wall]

        if not self.herd:
            self.herd = Herd(self.current_map)
            self.herd.members.append(self)
            self.herd.choose_new_alpha()
            self.current_map.herds.append(self.herd)

        self.herd.members.append(self)

    def tick_cycle(self):
        self.age += 1
        self.ticks_without_food += 1
        self.current_hunger_saturation -= 0.01
        self.time_since_last_move += 1

        if self.current_hunger_saturation < self.hunger_threshold:
            self.solve_hunger((self.tile_x, self.tile_y), self.target_object, self.migration_target, self.target_coordinates, self.herd.migration_target, self.herd.alpha)
        else:
            self.secondary_behavior()

        if self.time_since_last_move == self.speed:
            self.time_since_last_move = 0
            if not self.check_next_tile(None):
                print("whoops, got blocked")
                self.get_path(self.current_map, self.target_coordinates)
            self.move()
        self.starvation_check()

    def solve_hunger(self, my_position, target_object, migration_target_coordinates, target_coordinates, herd_migration_target_coordinates, alpha):
        '''because of what I have in mind, it could end up doing activities that are a bit abstracted from gathering food
        but bottomline is: the end result will be different than if it started from a position of no hunger'''
        self.eat()
        distance_from_alpha = utilities.distance(my_position[0], my_position[1], alpha.tile_x, alpha.tile_y)
        print("Debug A")
        if not target_object or not target_object.is_valid:
            print("Debug B")
            self.target_object = self.find_local_food()
            if not target_object:
                print("Debug C")
                if not migration_target_coordinates:
                    print("Debug D")
                    if herd_migration_target_coordinates:
                        print("Debug E")
                        self.migration_target = herd_migration_target_coordinates
                        self.target_coordinates = herd_migration_target_coordinates
                    else:
                        print("Debug F")
                        self.migration_target = self.pick_migration_target(self.current_map, my_position)
                        self.target_coordinates = self.migration_target
                else:
                    print("Debug G")
                    if my_position == target_coordinates:
                        print("Debug H")
                        self.migration_target = self.pick_migration_target(self.current_map, my_position)
                        self.target_coordinates = self.migration_target
            elif self.target_object:
                print("Debug I")
                self.migration_target = None
                self.target_coordinates = (self.target_object.tile_x, self.target_object.tile_y)
        if distance_from_alpha > self.herd_radius:
            print("Debug J")
            self.target_coordinates = (self.herd.alpha.tile_x, self.herd.alpha.tile_y)
        if not self.path or len(self.path.tiles) < 1:
            self.path = self.get_path(self.current_map, self.target_coordinates)
        print(my_position, self.target_coordinates)
        print(len(self.path.tiles))
        self.calculate_step()

    def secondary_behavior(self):
        distance_from_alpha = utilities.distance(self.tile_x, self.tile_y, self.herd.alpha.tile_x, self.herd.alpha.tile_y)
        if distance_from_alpha < self.herd_radius:
            self.idle()
        else:
            self.target_coordinates = (self.herd.alpha.tile_x, self.herd.alpha.tile_y)
            self.path = self.get_path()

    def eat(self):
        if self.current_tile.entity_group[Wheat]:
            for wheat_object in self.current_tile.entity_group[Wheat]:
                self.current_hunger_saturation += wheat_object.food_value
                self.ticks_without_food = 0
                wheat_object.expire()
                if self.current_hunger_saturation > self.max_hunger_saturation:
                    self.current_hunger_saturation = self.max_hunger_saturation
            self.target_object = None

    def get_path(self, game_map, target_coordinates):

        target_tile = game_map.game_tile_rows[target_coordinates[1]][target_coordinates[0]]
        start_tile = game_map.game_tile_rows[self.tile_y][self.tile_x]
        target_distance = utilities.distance(start_tile.column, start_tile.row, target_coordinates[0], target_coordinates[1])
        tiles_to_process = {start_tile: (0, target_distance, start_tile, start_tile)}
        visited = {start_tile: True}

        tile_neighbors = utilities.get_adjacent_tiles(start_tile, game_map)
        current_frontier = []
        for each in tile_neighbors:
            current_frontier.append((each, start_tile))

        visited, tiles_to_process = self.explore_frontier_to_target(visited, target_tile, current_frontier, tiles_to_process)

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

    def explore_frontier_to_target(self, visited, target_tile, current_frontier, tiles_to_process):
        steps = 0
        while target_tile not in visited:
            next_frontier = []
            steps += 1
            for tile in current_frontier:
                current_tile = tile[0]
                previous_tile = tile[1]
                if current_tile not in visited:
                    if self.check_next_tile(current_tile):
                        distance_to_target = utilities.distance(current_tile.column, current_tile.row, target_tile.column, target_tile.row)
                        tiles_to_process[current_tile] = (steps, distance_to_target, current_tile, previous_tile)
                        tile_neighbors = utilities.get_adjacent_tiles(current_tile, self.current_map)
                        for each in tile_neighbors:
                            entry = (each, current_tile)
                            next_frontier.append(entry)
                    visited[current_tile] = True
            current_frontier = next_frontier
        return visited, tiles_to_process

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

    def move(self):
        self.tile_x += self.change_x
        if self.tile_x < 0:
            self.tile_x = 0
        elif self.tile_x >= self.current_map.number_of_columns:
            self.tile_x = self.current_map.number_of_columns - 1
        self.tile_y += self.change_y
        if self.tile_y < 0:
            self.tile_y = 0
        elif self.tile_y >= self.current_map.number_of_rows:
            self.tile_y = self.current_map.number_of_rows - 1

        self.assign_tile()
        self.rect.x = self.tile_x * 10 + ((10 - self.width) / 2)
        self.rect.y = self.tile_y * 10 + ((10 - self.height) / 2)
        self.change_x = 0
        self.change_y = 0
        self.path.tiles.pop(0)

    def starvation_check(self):
        if self.current_hunger_saturation < 1:
            self.expire()

    def pick_migration_target(self, game_map, my_coordinates):
        target_x = random.randint(0, game_map.number_of_columns - 1)
        target_y = random.randint(0, game_map.number_of_rows - 1)
        return (target_x, target_y)

    def idle(self):
        action = random.randint(0, 900)
        if action <= 10:
            self.change_x = 1
        elif 10 < action <= 20:
            self.change_x = -1
        elif 20 < action <= 30:
            self.change_y = 1
        elif 30 < action <= 40:
            self.change_y = -1
        elif action > 750:
            self.change_x = 0
            self.change_y = 0
