import entity
import utilities
import navigate
import random
import pygame

pygame.init()
pygame.display.set_mode([0, 0])


class Creature(entity.Entity):
    def __init__(self, x, y, current_map, food_type):
        super().__init__(x, y, current_map)
        self.type = "Creature"
        self.food_type = food_type
        self.local_food_supply = []
        self.eating = False
        self.is_alpha = False
        self.change_x = 0
        self.change_y = 0
        self.target_coordinates = None
        self.target_object = None
        self.path = None
        self.search_area_graphic = None

    def expire(self):
        self.is_valid = False
        self.current_tile.entity_group[type(self)].remove(self)
        self.current_map.entity_group[type(self)].remove(self)

    def leave_tile(self):
        self.current_tile.entity_group[type(self)].remove(self)

    def find_local_food(self, current_map, accessable_tiles=None):
        nearby_food_list = []
        nearby_tiles = utilities.get_nearby_tiles(current_map, (self.tile_x, self.tile_y), self.sight_range)
        for each in nearby_tiles:
            if not each == self.current_tile:
                food_at_this_tile = each.entity_group[self.food_type]
                nearby_food_list.extend(food_at_this_tile)
        return nearby_food_list

    def select_closest_target(self, list_of_targets):
        targets_to_sort = []
        for target in list_of_targets:
            dist = navigate.distance(target.tile_x, target.tile_y, self.tile_x, self.tile_y)
            targets_to_sort.append((dist, target))

        possible_targets = sorted(targets_to_sort)
        if possible_targets:
            return possible_targets[0][1]
        else:
            return None

    def choose_random_target(self, game_map, my_position):
        target_x, target_y = my_position
        while my_position == (target_x, target_y):
            target_x = random.randint(0, game_map.number_of_columns - 1)
            target_y = random.randint(0, game_map.number_of_rows - 1)
            tile = game_map.game_tile_rows[target_y][target_x]
            if tile.is_occupied():
                target_x, target_y = my_position
        return (target_x, target_y)

    def eat(self):
        if self.current_tile.entity_group[self.food_type]:
            self.eating = True
            for food_object in self.current_tile.entity_group[self.food_type]:
                self.current_hunger_saturation += min(food_object.food_value, self.bite_size)
                food_object.food_value -= self.bite_size
                self.ticks_without_food = 0
                if food_object.food_value <= 0:
                    food_object.expire()
                    self.target_object = None
                    self.target_coordinates = None
                    self.path = None
                if self.current_hunger_saturation > self.max_hunger_saturation:
                    self.current_hunger_saturation = self.max_hunger_saturation

    def starvation_check(self):
        if self.current_hunger_saturation < 1:
            self.expire()

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
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20
        self.change_x = 0
        self.change_y = 0
        self.path.tiles.pop(0)


class Buffalo(Creature):
    occupies_tile = True

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map, "Wheat")

        buffalo_image_1 = pygame.image.load("art/buffalo/buffalo_1.png").convert()
        buffalo_image_1.set_colorkey(utilities.colors.key)

        self.display_name = "Buffalo"
        self.speed = 10
        self.current_hunger_saturation = 20000
        self.hunger_threshold = 35000
        self.max_hunger_saturation = 40000
        self.horizontal_sight = 6
        self.vertical_sight = 6
        self.sight_range = 10
        self.bite_size = 5
        self.ticks_without_eating = 0
        self.time_since_last_move = 0
        self.sprite.image = buffalo_image_1
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20

    def tick_cycle(self):
        self.age += 1
        self.current_hunger_saturation -= 1
        self.time_since_last_move += 1

        if self.current_hunger_saturation < self.hunger_threshold:
            self.change_x, self.change_y = self.solve_hunger((self.tile_x, self.tile_y))
        else:
            self.secondary_behavior()

        if not self.eating:
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.move()
        self.starvation_check()

    def solve_hunger(self, my_position):
        '''because of what I have in mind, it could end up doing activities that are a bit abstracted from gathering food
        but bottomline is: the end result will be different than if it started from a position of no hunger'''
        self.eating = False
        self.ticks_without_eating += 1
        if self.current_tile.entity_group["Flora"] and self.ticks_without_eating > 30:
            self.eat()
            return 0, 0
        else:
            # Runs too often - needs better conditionals
            if not self.target_coordinates:
                self.target_object, self.target_coordinates = self.choose_target(self.current_map, my_position)

            if not self.path or len(self.path.tiles) < 1:
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
                if len(self.path.tiles) < 2:
                    self.target_object, self.target_coordinates = self.choose_target(self.current_map, my_position)
                    self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)

            change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            if self.path.tiles[0].is_occupied():
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
                change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            return change_x, change_y

    def secondary_behavior(self):
        self.idle()

    def choose_target(self, current_map, my_position):
        nearby_food = self.find_local_food(current_map)
        if nearby_food:
            target_object = random.choice(nearby_food)
            target_coordinates = (target_object.tile_x, target_object.tile_y)
        else:
            target_coordinates = self.choose_random_target(current_map, my_position)
            target_object = None
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
