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
            self.is_hungry()
        else:
            self.is_not_hungry()

        if self.time_since_last_move == self.speed:
            self.time_since_last_move = 0
            self.move()
            self.path.tiles.pop(0)
        self.starvation_check()

    def is_hungry(self):
        self.eat()
        distance_from_alpha = utilities.distance(self.tile_x, self.tile_y, self.herd.alpha.tile_x, self.herd.alpha.tile_y)
        if distance_from_alpha <= self.herd_radius:
            if self.path and len(self.path.tiles) > 0:
                self.calculate_step()
                while not self.check_next_tile(None):
                    self.path = self.get_path()
                    self.calculate_step()
            else:
                print("debug a")
                if self.target_object and self.target_object.is_valid:
                    print("debug b")
                    self.path = self.get_path()
                    self.calculate_step()
                else:
                    print("debug c")
                    self.target_object = self.find_local_food()
                    if not self.target_object:
                        print("debug c")
                        if not self.migration_target:
                            print("debug d")
                            if self.herd.migration_target:
                                print("debug e")
                                self.migration_target = self.herd.migration_target
                                self.target_coordinates = self.migration_target
                                self.path = self.get_path()
                                self.calculate_step()
                            else:
                                print("debug f")
                                self.migration_target = self.pick_migration_target()
                                self.target_coordinates = self.migration_target
                                self.path = self.get_path()
                                self.calculate_step()
                        else:
                            print("debug g")
                            print(self.migration_target, self.target_coordinates, (self.tile_x, self.tile_y))
                            if self.target_coordinates == (self.tile_x, self.tile_y):
                                print("debug h")
                                self.migration_target = self.pick_migration_target()
                                self.target_coordinates = self.migration_target
                                self.path = self.get_path()
                                self.calculate_step()
        else:
            print("debug i")
            self.target_coordinates = (self.herd.alpha.tile_x, self.herd.alpha.tile_y)
            self.path = self.get_path()
            self.calculate_step()

    def is_not_hungry(self):
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

    def get_path(self):
        if self.target_object:
            target_x = self.target_object.tile_x
            target_y = self.target_object.tile_y
        else:
            target_x = self.target_coordinates[0]
            target_y = self.target_coordinates[1]

        target_tile = self.current_map.game_tile_rows[target_y][target_x]
        start_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
        target_distance = utilities.distance(start_tile.column, start_tile.row, target_x, target_y)
        tiles_to_process = {start_tile: (0, target_distance, start_tile, start_tile)}
        visited = {start_tile: True}

        tile_neighbors = utilities.get_adjacent_tiles(start_tile, self.current_map)
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
                        distance_to_target = utilities.distance(current_tile.column, current_tile.row, target_x, target_y)
                        tiles_to_process[current_tile] = (steps, distance_to_target, current_tile, previous_tile)
                        tile_neighbors = utilities.get_adjacent_tiles(current_tile, self.current_map)
                        for each in tile_neighbors:
                            entry = (each, current_tile)
                            next_frontier.append(entry)
                    visited[current_tile] = True
            current_frontier = next_frontier
        new_path = utilities.Path()
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

    def starvation_check(self):
        if self.current_hunger_saturation < 1:
            self.expire()

    def pick_migration_target(self):
        target_x = random.randint(0, self.current_map.number_of_columns - 1)
        target_y = random.randint(0, self.current_map.number_of_rows - 1)
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
