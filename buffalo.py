import pygame
import utilities
import entity
import random
import navigate
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
        else:
            self.herd.members.append(self)

    def tick_cycle(self):
        self.age += 1
        self.ticks_without_food += 1
        self.current_hunger_saturation -= 0.01
        self.time_since_last_move += 1

        if self.current_hunger_saturation < self.hunger_threshold:
            self.change_x, self.change_y = self.solve_hunger((self.tile_x, self.tile_y), self.target_object, self.target_coordinates, self.herd.migration_target, self.herd.alpha)
        else:
            self.secondary_behavior()

        if self.time_since_last_move == self.speed:
            self.time_since_last_move = 0
            self.move()
        self.starvation_check()

    def solve_hunger(self, my_position, target_object, target_coordinates, herd_migration_target_coordinates, alpha):
        '''because of what I have in mind, it could end up doing activities that are a bit abstracted from gathering food
        but bottomline is: the end result will be different than if it started from a position of no hunger'''
        self.eat()
        if not self.target_object or not self.target_object.is_valid:
            target_object, target_coordinates = self.choose_target()
        assert target_coordinates
        assert target_coordinates != my_position
        if not self.path or len(self.path.tiles) < 1:
            self.path = navigate.get_path(my_position, self.current_map, target_coordinates, self.incompatible_objects)
        assert self.path
        assert len(self.path.tiles) > 0
        change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
        if utilities.tile_is_valid(self.current_map, my_position[0] + change_x, my_position[1] + change_y, self.incompatible_objects):
            self.path = navigate.get_path(my_position, self.current_map, target_coordinates, self.incompatible_objects)
            change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            return change_x, change_y
        return change_x, change_y

    def secondary_behavior(self):
        if self.within_herd_range(self.tile_x, self.tile_y, self.herd_radius, self.herd.alpha):
            self.idle()
        else:
            self.target_coordinates = (self.herd.alpha.tile_x, self.herd.alpha.tile_y)
            self.path = self.get_path()

    def within_herd_range(self, my_position, herd_radius, alpha):
        distance_from_alpha = navigate.distance(my_position[0], my_position[1], alpha.tile_x, alpha.tile_y)
        if distance_from_alpha < herd_radius:
            return True
        return False

    def choose_target(self):
        nearby_food = self.find_local_food()
        if nearby_food:
            target_object = self.select_closest_target(nearby_food)
            target_coordinates = (target_object.tile_x, target_object.tile_y)
        else:
            target_object = None
            target_coordinates = self.herd.migration_target
        return target_object, target_coordinates

    def eat(self):
        if self.current_tile.entity_group[Wheat]:
            for wheat_object in self.current_tile.entity_group[Wheat]:
                self.current_hunger_saturation += wheat_object.food_value
                self.ticks_without_food = 0
                wheat_object.expire()
                if self.current_hunger_saturation > self.max_hunger_saturation:
                    self.current_hunger_saturation = self.max_hunger_saturation
            self.target_object = None

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
