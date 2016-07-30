import pygame
import utilities
import random
from manure import Manure
from wall import Wall
from tree import Tree
import vegetation
import buffalo

pygame.init()
pygame.display.set_mode([0, 0])

wheat_seedling_image = pygame.image.load("art/wheat/wheat_seedling.png").convert()
wheat_seedling_image.set_colorkey(utilities.colors.key)

wheat_young_image = pygame.image.load("art/wheat/wheat_young.png")
wheat_young_image.set_colorkey(utilities.colors.key)

wheat_mature_image_1 = pygame.image.load("art/wheat/wheat_mature_1.png")
wheat_mature_image_1.set_colorkey(utilities.colors.key)

wheat_mature_image_2 = pygame.image.load("art/wheat/wheat_mature_2.png")
wheat_mature_image_2.set_colorkey(utilities.colors.key)

wheat_mature_image_3 = pygame.image.load("art/wheat/wheat_mature_3.png")
wheat_mature_image_3.set_colorkey(utilities.colors.key)
wheat_mature_images = [wheat_mature_image_1, wheat_mature_image_2, wheat_mature_image_3]

wheat_withered_image = pygame.image.load("art/wheat/wheat_withered.png")
wheat_withered_image.set_colorkey(utilities.colors.key)

wheat_dead_image = pygame.image.load("art/wheat/wheat_dead.png")
wheat_dead_image.set_colorkey(utilities.colors.key)


class Wheat(vegetation.Vegetation):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.age = random.randint(0, 40)
        self.food_value = 0
        self.growth_stages = []
        self.growth_stage = 0
        seedling = (1000)
        young = (3000)
        mature = (4000)
        withered = (7000)
        dead = (9999)

        self.growth_stages = [(seedling, wheat_seedling_image, 5),
                                (young, wheat_young_image, 20),
                                (mature, random.choice(wheat_mature_images), 50),
                                (withered, wheat_withered_image, 5),
                                (dead, wheat_dead_image, 0)]
        # the higher the more babbys
        self.likelihood_of_reproducing = 5
        # max and min number of babies possible in a single run of reproduce()
        self.minimum_number_of_babies = 1
        self.max_number_of_babies = 2
        self.incompatible_objects = [Wheat, Wall, Tree]
        self.group_generation_max_distance = 8
        self.image = wheat_seedling_image
        self.rect = self.image.get_rect()
        self.rect.x = self.tile_x * 10
        self.rect.y = self.tile_y * 10

    def tick_cycle(self):
        self.age += 1
        if self.age > self.growth_stages[self.growth_stage][0]:
            self.growth_stage += 1
            self.image = self.growth_stages[self.growth_stage][1]
            self.food_value = self.growth_stages[self.growth_stage][2]
        if self.growth_stage == 2:
            self.baby_roll()
        elif self.growth_stage == 4:
            self.expire()
            if random.randrange(0, 10) > 2:
                Wheat(self.tile_x, self.tile_y, self.current_map)

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
                    this_tile = self.current_map.game_tile_rows[tile_y][tile_x]
                    wheat_at_this_tile = this_tile.entity_group[Wheat]
                    wall_at_this_tile = this_tile.entity_group[Wall]
                    tree_at_this_tile = this_tile.entity_group[Tree]
                    if not wheat_at_this_tile and not wall_at_this_tile and not tree_at_this_tile:
                        growth_candidates.append((tile_x, tile_y))
                tile_x += 1
            tile_x = self.tile_x - 1
            tile_y += 1
        if growth_candidates:
            growth_tile = random.choice(growth_candidates)
            Wheat(growth_tile[0], growth_tile[1], self.current_map)
