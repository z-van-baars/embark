import pygame
import utilities
import random
import navigate
import animal
from wheat import Wheat
from herd import Herd
from wall import Wall
from tree import Tree

pygame.init()
pygame.display.set_mode([0, 0])

buffalo_image_1 = pygame.image.load("art/buffalo/buffalo_1.png").convert()
buffalo_image_1.set_colorkey(utilities.colors.key)


class Buffalo(animal.Animal):
    occupies_tile = True

    def __init__(self, x, y, current_map, herd=None):
        super().__init__(x, y, current_map, Wheat)
        self.speed = 100
        self.current_hunger_saturation = 20000
        self.hunger_threshold = 35000
        self.max_hunger_saturation = 40000
        self.horizontal_sight = 6
        self.vertical_sight = 6
        self.sight_range = 10
        self.herd_radius = 5
        self.herd = herd
        self.bite_size = 5
        self.ticks_without_eating = 0
        self.time_since_last_move = 0
        self.min_initial_herd_size = 5
        self.max_initial_herd_size = 10

        if not self.herd:
            self.herd = Herd(self.current_map)
            self.herd.members.append(self)
            self.herd.choose_new_alpha()
            self.current_map.herds.append(self.herd)
        else:
            self.herd.members.append(self)

        self.sprite.image = buffalo_image_1
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 10
        self.sprite.rect.y = self.tile_y * 10

    def tick_cycle(self):
        self.age += 1
        self.current_hunger_saturation -= 1
        self.time_since_last_move += 1

        if self.current_hunger_saturation < self.hunger_threshold:
            self.change_x, self.change_y = self.solve_hunger((self.tile_x, self.tile_y), self.target_object, self.target_coordinates, self.herd.migration_target, self.herd.alpha)
        else:
            self.secondary_behavior()

        if not self.eating:
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.move()
        self.starvation_check()

    def solve_hunger(self, my_position, target_object, target_coordinates, herd_migration_target_coordinates, alpha):
        '''because of what I have in mind, it could end up doing activities that are a bit abstracted from gathering food
        but bottomline is: the end result will be different than if it started from a position of no hunger'''
        self.eating = False
        self.ticks_without_eating += 1
        if self.current_tile.entity_group[Wheat] and self.ticks_without_eating > 30:
            self.eat()
            return 0, 0
        else:
            if not self.target_object or not self.target_object.is_valid:
                target_object, target_coordinates = self.choose_target(self.current_map, my_position)

            if not self.path or len(self.path.tiles) < 1:
                self.path, target_coordinates = navigate.get_path(my_position, self.current_map, target_coordinates, self.incompatible_objects)
                if len(self.path.tiles) < 1:
                    self.path, target_coordinates = navigate.get_path(my_position, self.current_map, target_coordinates, self.incompatible_objects)

            change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            if self.path.tiles[0].is_occupied():
                self.path, target_coordinates = navigate.get_path(my_position, self.current_map, target_coordinates, self.incompatible_objects)
                change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            return change_x, change_y

    def secondary_behavior(self):
        if self.within_herd_range((self.tile_x, self.tile_y), self.herd_radius, self.herd.alpha):
            self.idle()
        else:
            self.target_coordinates = (self.herd.alpha.tile_x, self.herd.alpha.tile_y)
            self.path = self.get_path()

    def within_herd_range(self, my_position, herd_radius, alpha):
        distance_from_alpha = navigate.distance(my_position[0], my_position[1], alpha.tile_x, alpha.tile_y)
        if distance_from_alpha < herd_radius:
            return True
        return False

    def choose_target(self, current_map, my_position):
        nearby_food = self.find_local_food(current_map)
        if nearby_food:
            target_object = random.choice(nearby_food)
            target_coordinates = (target_object.tile_x, target_object.tile_y)
        else:
            target_object = None
            target_coordinates = my_position
            while target_coordinates == my_position:
                acceptable_targets = utilities.get_nearby_tiles(self.current_map, self.herd.migration_target, self.herd_radius)
                target_tile = random.choice(acceptable_targets)
                target_coordinates = (target_tile.column, target_tile.row)
        assert my_position != target_coordinates
        return target_object, target_coordinates

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
