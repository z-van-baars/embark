import pygame
import random
import utilities
from utilities import GlobalVariables
from tile import Tile
from buffalo import Buffalo
from wheat import Wheat


class Map(object):
    def __init__(self, dimensions):
        self.width = (dimensions[0] * 10)
        self.height = (dimensions[1] * 10)
        self.columns = dimensions[0]
        self.rows = dimensions[1]
        self.x_shift = 0
        self.y_shift = 0
        self.tiles = pygame.sprite.Group()
        self.entity_group = {}
        self.entity_group[Wheat] = pygame.sprite.Group()
        self.entity_group[Buffalo] = pygame.sprite.Group()

        grass_1 = ("Grass 1", (utilities.colors.light_green))
        grass_2 = ("Grass 2", (utilities.colors.dark_green))

        self.terrain_types = [grass_1, grass_2]


    def map_generation(self):
        for y_row in range(self.rows):
            for x_column in range(self.columns):
                new_tile_type = random.choice(self.terrain_types)
                new_tile = Tile(new_tile_type)
                new_tile.rect.x = x_column * 10
                new_tile.rect.y = y_row * 10
                self.tiles.add(new_tile)

        self.generate_vegetation()

        for new_buf in range(10):

            x_position = random.randint(0, self.columns - 1)
            y_position = random.randint(0, self.rows - 1)

            x_position *= 10
            y_position *= 10

            new_buffalo = Buffalo(x_position, y_position, self)

            self.entity_group[Buffalo].add(new_buffalo)

    def generate_vegetation(self):
        number_of_wheat_clusters = random.randint(4, 10)

        for wheat_clusters in range(number_of_wheat_clusters):

            self.generate_wheat_cluster()

    def get_random_coordinates(self, x_lower, x_upper, y_lower, y_upper):
        x_position = random.randint(x_lower, x_upper)
        y_position = random.randint(y_lower, y_upper)

        x_position *= 10
        y_position *= 10
        return (x_position, y_position)


    def generate_wheat_cluster(self):
        wheat_cluster_placed = False
        while not wheat_cluster_placed:
            coordinates = self.get_random_coordinates(0, self.columns - 1, 0, self.rows - 1)
            cluster_center_wheat = Wheat(coordinates[0], coordinates[1], self)
            vegetation_collisions = []
            vegetation_collisions = (pygame.sprite.spritecollide(cluster_center_wheat, self.entity_group[Wheat], False))
            if not vegetation_collisions:
                wheat_cluster_placed = True
        self.entity_group[Wheat].add(cluster_center_wheat)
        cluster_left_edge = ((cluster_center_wheat.rect.x - 2) / 10) - 7
        cluster_right_edge = ((cluster_center_wheat.rect.x - 2) / 10) + 7
        cluster_top_edge = ((cluster_center_wheat.rect.y - 2) / 10) - 7
        cluster_bottom_edge = ((cluster_center_wheat.rect.y - 2) / 10) + 7
        number_of_neighbors = random.randint(3, 9)
        for wheat in range(number_of_neighbors):
            neighbor_placed = False
            while not neighbor_placed:
                coordinates = self.get_random_coordinates(cluster_left_edge, cluster_right_edge, cluster_top_edge, cluster_bottom_edge)
                new_neighbor = Wheat(coordinates[0], coordinates[1], self)
                vegetation_collisions = []
                vegetation_collisions = (pygame.sprite.spritecollide(new_neighbor, self.entity_group[Wheat], False))
                if not vegetation_collisions:
                    neighbor_placed = True
            self.entity_group[Wheat].add(new_neighbor)


    def world_scroll(self, shift_x, shift_y, screen_width, screen_height):
        if 0 >= self.x_shift + shift_x >= -(self.width - screen_width):
            self.x_shift += shift_x
        if 0 >= self.y_shift + shift_y >= -(self.height - screen_height):
            self.y_shift += shift_y
