import pygame
import utilities
import entity
import random
from wheat import Wheat


class Buffalo(entity.Entity):
    def __init__(self, x, y, current_map, current_tile):
        super().__init__((x + 2), (y + 2), utilities.colors.red, 6, 6, current_map)
        self.speed = 60
        self.time_since_last_move = 0
        self.age = 0
        self.ticks_without_food = 0
        self.change_x = 0
        self.change_y = 0
        self.hunger_saturation = 50
        self.max_hunger_saturation = 200
        self.target_food = None
        self.current_tile = current_tile

    def do_thing(self):
        self.age += 1
        self.ticks_without_food += 1
        self.hunger_saturation -= 0.1
        self.time_since_last_move += 1
        self.starvation_check()
        if self.target_food:
            self.eat()
            if self.target_food:
                self.calculate_step()
        else:
            if self.hunger_saturation < 200:
                self.target_food = self.find_local_food()
            else:
                self.idle()
        if self.time_since_last_move == self.speed:
            self.time_since_last_move = 0
            self.move()

    def eat(self):
        wheat_collision = pygame.sprite.spritecollide(self, self.current_map.entity_group[Wheat], True)
        if wheat_collision:
            for wheat_object in wheat_collision:
                self.hunger_saturation += wheat_object.food_value
                self.current_map.entity_group[Wheat].remove(wheat_object)
                if self.hunger_saturation > self.max_hunger_saturation:
                    self.hunger_saturation = self.max_hunger_saturation
                self.ticks_without_food = 0
            self.target_food = None

    def move(self):
        if 0 <= (self.rect.x + self.change_x) <= self.current_map.width:
            self.rect.x += self.change_x
        if 0 <= (self.rect.y + self.change_y) <= self.current_map.height:
            self.rect.y += self.change_y
        self.change_x = 0
        self.change_y = 0

    def calculate_step(self):
        x_dist = self.rect.x - self.target_food.rect.x
        y_dist = self.rect.y - self.target_food.rect.y
        if abs(x_dist) > abs(y_dist):
            if x_dist < 0:
                self.change_x = -10
            else:
                self.change_x = 10
        elif abs(x_dist) < abs(y_dist):
            if y_dist < 0:
                self.change_y = -10
            else:
                self.change_y = 10
        else:
            if y_dist < 0:
                self.change_y = -10
            else:
                self.change_y = 10
            if x_dist < 0:
                self.change_x = -10
            else:
                self.change_x = 10

    def starvation_check(self):
        if self.ticks_without_food > 50000:
            self.expire()
        if self.hunger_saturation < 1:
            self.expire()

    def find_local_food(self):
        collision_checker = Buffalo(self.rect.x, self.rect.y, self.current_map, self.current_map.game_tile_rows[int(self.rect.y / 10)][int(self.rect.x / 10)])
        nearby_food_list = []
        collision_checker.rect.x -= 60
        collision_checker.rect.y -= 60
        for row in range(13):
            for column in range(13):
                new_potential_food = (pygame.sprite.spritecollide(collision_checker, self.current_map.entity_group[Wheat], False))
                if new_potential_food:
                    nearby_food_list += new_potential_food
                collision_checker.rect.x += 10
            collision_checker.rect.x -= 140
            collision_checker.rect.y += 10

        targets_to_sort = []
        for target in nearby_food_list:
            dist = utilities.distance(target.rect.x, target.rect.y, self.rect.x, self.rect.y)
            targets_to_sort.append((dist, target))

        possible_targets = sorted(targets_to_sort)
        if possible_targets:
            return possible_targets[0][1]
        else:
            self.idle()
            return None

    def idle(self):
        action = random.randint(0, 4000)
        if action <= 10:
            self.change_x = 10
        elif 10 < action <= 20:
            self.change_x = -10
        elif 20 < action <= 30:
            self.change_y = 10
        elif 30 < action <= 40:
            self.change_y = -10
        elif action > 750:
            self.change_x = 0
            self.change_y = 0
