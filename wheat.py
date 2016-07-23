import pygame
import utilities
import entity
import random
from manure import Manure


class Wheat(entity.Entity):
    def __init__(self, x, y, current_map, age):
        super().__init__(x, y, (201, 227, 73), 6, 6, current_map, None)
        self.age = age
        self.food_value = 25
        self.growth_stages = []
        self.growth_stage = 0
        seedling = (100, (201, 227, 73))
        young = (250, (227, 196, 73))
        mature = (400, (189, 158, 30))
        withered = (700, (133, 107, 7))
        dead = (9999, (0, 0, 0))
        self.growth_stages = [seedling, young, mature, withered, dead]
        # the higher the more babbys
        self.likelihood_of_reproducing = 5
        # max and min number of babies possible in a single run of reproduce()
        self.minimum_number_of_babies = 1
        self.max_number_of_babies = 2

    def tick_cycle(self):
        self.age += 1
        if self.age > self.growth_stages[self.growth_stage][0]:
            self.growth_stage += 1
            self.image.fill(self.growth_stages[self.growth_stage][1])
        if self.growth_stage == 2:
            self.baby_roll()
        elif self.growth_stage == 4:
            self.expire()
            if random.randrange(0, 10) > 2:
                Wheat(self.tile_x, self.tile_y, self.current_map, random.randint(5, 20))

    def baby_roll(self):
        chance_to_reproduce = random.randint(0, self.likelihood_of_reproducing)
        if chance_to_reproduce < 1:
            for x in range(random.randint(self.minimum_number_of_babies, self.max_number_of_babies)):
                self.reproduce()

    def reproduce(self):
        growth_candidates = []
        tile_x = self.tile_x - 1
        tile_y = self.tile_y - 1
        for map_tile_row in range(3):
            for map_tile in range(3):
                if utilities.within_map(tile_x, tile_y, self.current_map):
                    wheat_at_this_tile = self.current_map.game_tile_rows[tile_y][tile_x].entity_group[Wheat]
                    if not wheat_at_this_tile:
                        growth_candidates.append((tile_x, tile_y))
                tile_x += 1
            tile_x = self.tile_x - 1
            tile_y += 1
        if growth_candidates:
            growth_tile = random.choice(growth_candidates)
            Wheat(growth_tile[0], growth_tile[1], self.current_map, random.randint(5, 20))
