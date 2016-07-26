import pygame
import utilities
import random


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height, current_map, food_type):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.width = width
        self.height = height
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.tile_x = x
        self.tile_y = y
        self.rect.x = self.tile_x * 10 + ((10 - self.width) / 2)
        self.rect.y = self.tile_y * 10 + ((10 - self.height) / 2)
        self.current_map = current_map
        self.current_tile = None
        self.is_valid = True
        self.food_type = food_type
        self.local_food_supply = []
        self.herd = None
        self.is_alpha = False
        self.incompatible_objects = None

        self.current_map.entity_group[type(self)].add(self)

        self.assign_tile()

    def __lt__(self, other):
        if self.tile_x < other.tile_x:
            return True
        elif self.tile_y < other.tile_y:
            return True
        else:
            return False

    def expire(self):
        self.is_valid = False
        self.current_tile.entity_group[type(self)].remove(self)
        self.current_map.entity_group[type(self)].remove(self)
        if self.is_alpha and self.herd:
            self.herd.members.remove(self)
            self.herd.choose_new_alpha()

    def assign_tile(self):
        if self.current_tile:
            self.current_tile.entity_group[type(self)].remove(self)
            self.current_tile = None
        self.current_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
        self.current_tile.entity_group[type(self)].append(self)

    def leave_tile(self):
        self.current_tile.entity_group[type(self)].remove(self)


    def find_local_food(self):
        nearby_food_list = []
        tile_x = self.tile_x - (self.horizontal_sight)
        tile_y = self.tile_y - (self.vertical_sight)
        for map_tile_row in range(self.vertical_sight * 2 + 1):
            for map_tile in range(self.horizontal_sight * 2 + 1):
                if utilities.within_map(tile_x, tile_y, self.current_map):
                    food_at_this_tile = self.current_map.game_tile_rows[tile_y][tile_x].entity_group[self.food_type]
                    nearby_food_list.extend(food_at_this_tile)
                tile_x += 1
            tile_x = self.tile_x - (self.horizontal_sight)
            tile_y += 1

        targets_to_sort = []
        self.local_food_supply = nearby_food_list
        for target in nearby_food_list:
            dist = utilities.distance(target.tile_x, target.tile_y, self.tile_x, self.tile_y)
            targets_to_sort.append((dist, target))

        possible_targets = sorted(targets_to_sort)
        if possible_targets:
            return possible_targets[0][1]
        else:
            return None
