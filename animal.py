import entity
import utilities
import navigate
import random


class Animal(entity.Entity):
    def __init__(self, x, y, current_map, food_type):
        super().__init__(x, y, current_map)
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
        if self.is_alpha and self.herd:
            self.herd.members.remove(self)
            self.herd.choose_new_alpha()

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
            if not utilities.tile_is_valid(game_map, target_x, target_y, self.incompatible_objects):
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
        self.rect.x = self.tile_x * 10
        self.rect.y = self.tile_y * 10
        self.change_x = 0
        self.change_y = 0
        self.path.tiles.pop(0)

