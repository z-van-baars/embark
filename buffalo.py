import pygame
import utilities
import entity
import random
from wheat import Wheat
from herd import Herd


class Buffalo(entity.Entity):
    def __init__(self, x, y, current_map, herd):
        super().__init__(x, y, utilities.colors.red, 6, 6, current_map, Wheat)
        self.speed = 2
        self.time_since_last_move = 0
        self.age = 0
        self.ticks_without_food = 0
        self.change_x = 0
        self.change_y = 0
        self.current_hunger_saturation = 200
        self.hunger_threshold = 400
        self.max_hunger_saturation = 400
        self.target_food = None
        self.horizontal_sight = 20
        self.vertical_sight = 20
        self.migration_target = None
        self.local_food_supply = []
        self.herd_radius = 40
        self.herd = herd
        self.is_alpha = False
        self.alpha_color = (215, 0, 0)

        self.min_initial_herd_size = 6
        self.max_initial_herd_size = 20

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
        self.starvation_check()

    def is_hungry(self):
        self.eat()
        distance_from_alpha = utilities.distance(self.tile_x, self.tile_y, self.herd.alpha.tile_x, self.herd.alpha.tile_y)
        if distance_from_alpha <= self.herd_radius:
            if self.target_food and self.target_food.is_valid:
                if self.target_food:
                    self.migration_target = None
                    self.calculate_step()
            else:
                self.target_food = None
                self.target_food = self.find_local_food()
                if not self.target_food:
                    if self.herd.migration_target:
                        self.migration_target = self.herd.migration_target
                    else:
                        self.migration_target = self.pick_migration_target()
                    self.calculate_step()
        else:
            self.migration_target = (self.herd.alpha.tile_x, self.herd.alpha.tile_y)
            self.calculate_step()

    def is_not_hungry(self):
        distance_from_alpha = utilities.distance(self.tile_x, self.tile_y, self.herd.alpha.tile_x, self.herd.alpha.tile_y)
        if distance_from_alpha < self.herd_radius:
            self.idle()
        else:
            self.migration_target = (self.herd.alpha.tile_x, self.herd.alpha.tile_y)

    def eat(self):
        if self.current_tile.entity_group[Wheat]:
            for wheat_object in self.current_tile.entity_group[Wheat]:
                self.current_hunger_saturation += wheat_object.food_value
                self.ticks_without_food = 0
                wheat_object.expire()
                if self.current_hunger_saturation > self.max_hunger_saturation:
                    self.current_hunger_saturation = self.max_hunger_saturation
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
