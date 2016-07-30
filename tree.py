import pygame
import utilities
import random
import vegetation
from wall import Wall

pygame.init()
pygame.display.set_mode([0, 0])

tree_image_1 = pygame.image.load("art/tree/tree_1.png").convert()
tree_image_1.set_colorkey(utilities.colors.key)

tree_image_2 = pygame.image.load("art/tree/tree_2.png")
tree_image_2.set_colorkey(utilities.colors.key)

tree_image_3 = pygame.image.load("art/tree/tree_3.png")
tree_image_3.set_colorkey(utilities.colors.key)

possible_tree_images = [tree_image_1, tree_image_2, tree_image_3]


class Tree(vegetation.Vegetation):
    occupies_tile = True

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.age = random.randint(0, 40)
        self.group_generation_max_distance = 20

        self.sprite.image = random.choice(possible_tree_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 10
        self.sprite.rect.y = self.tile_y * 10 - 10
        
