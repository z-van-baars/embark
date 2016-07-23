import pygame
import utilities
import entity
import random
from wheat import Wheat


class Buffalo(entity.Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, utilities.colors.red, 6, 6, current_map)
        self.speed = 1
        self.time_since_last_move = 0
        self.age = 0
        self.ticks_without_food = 0
        self.change_x = 0
        self.change_y = 0
        self.hunger_saturation = 50
        self.max_hunger_saturation = 400
        self.target_food = None
        self.horizontal_sight = 20
        self.vertical_sight = 20
        self.migration_target = None

    def do_thing(self):
        self.age += 1
        self.ticks_without_food += 1
        self.hunger_saturation -= 0.1
        self.time_since_last_move += 1
        if self.hunger_saturation < self.max_hunger_saturation:
            if self.target_food and self.target_food.is_valid:
                self.eat()
                if self.target_food:
                    self.calculate_step()
            else:
                self.target_food = self.find_local_food()
                if not self.target_food:
                    if not self.migration_target:
                        self.pick_migration_target()
                    elif self.migration_target:
                        if self.tile_x == self.migration_target[0] and self.tile_y == self.migration_target[1]:
                            self.migration_target = None
                            self.pick_migration_target()
                    self.calculate_step()
        else:
            self.idle()

        if self.time_since_last_move == self.speed:
            self.time_since_last_move = 0
            self.move()
        self.starvation_check()

    def eat(self):
        if self.current_tile.entity_group[Wheat]:
            for wheat_object in self.current_tile.entity_group[Wheat]:
                self.hunger_saturation += wheat_object.food_value
                self.ticks_without_food = 0
                wheat_object.expire()
                if self.hunger_saturation > self.max_hunger_saturation:
                    self.hunger_saturation = self.max_hunger_saturation
            self.target_food = None

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

    def calculate_step(self):
        if self.target_food:
            x_dist = self.tile_x - self.target_food.tile_x
            y_dist = self.tile_y - self.target_food.tile_y
        else:
            x_dist = self.tile_x - self.migration_target[0]
            y_dist = self.tile_y - self.migration_target[1]
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

    def starvation_check(self):
        if self.ticks_without_food > 50000:
            self.expire()
        if self.hunger_saturation < 1:
            self.expire()

    def pick_migration_target(self):
        target_x = random.randint(0, self.current_map.number_of_columns - 1)
        target_y = random.randint(0, self.current_map.number_of_rows - 1)
        self.migration_target = (target_x, target_y)

    def find_local_food(self):
        nearby_wheat_list = []
        tile_x = self.tile_x - (self.horizontal_sight)
        tile_y = self.tile_y - (self.vertical_sight)
        for map_tile_row in range(self.vertical_sight * 2 + 1):
            for map_tile in range(self.horizontal_sight * 2 + 1):
                if utilities.within_map(tile_x, tile_y, self.current_map):
                    wheat_at_this_tile = self.current_map.game_tile_rows[tile_y][tile_x].entity_group[Wheat]
                    nearby_wheat_list.extend(wheat_at_this_tile)
                tile_x += 1
            tile_x = self.tile_x - (self.horizontal_sight)
            tile_y += 1

        targets_to_sort = []
        for target in nearby_wheat_list:
            dist = utilities.distance(target.tile_x, target.tile_y, self.tile_x, self.tile_y)
            targets_to_sort.append((dist, target))

        possible_targets = sorted(targets_to_sort)
        if possible_targets:
            return possible_targets[0][1]
        else:
            return None

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
