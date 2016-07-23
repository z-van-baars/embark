import pygame
import random
import utilities
from utilities import GlobalVariables
from tile import DisplayTile
from buffalo import Buffalo
from wheat import Wheat
from game_tile import GameTile


class Map(object):
    def __init__(self, dimensions):
        self.width = (dimensions[0] * 10)
        self.height = (dimensions[1] * 10)
        self.number_of_columns = dimensions[0]
        self.number_of_rows = dimensions[1]
        self.game_tile_rows = []
        self.x_shift = 0
        self.y_shift = 0

        self.display_tiles = pygame.sprite.Group()
        self.entity_group = {}
        self.entity_group[Wheat] = pygame.sprite.Group()
        self.entity_group[Buffalo] = pygame.sprite.Group()

        self.number_of_buffalo = 20
        self.number_of_wheat_clusters = 30

        grass_1 = ("Grass 1", (utilities.colors.light_green))
        grass_2 = ("Grass 2", (utilities.colors.dark_green))

        self.terrain_types = [grass_1, grass_2]

    def map_generation(self):
        for y_row in range(self.number_of_rows):
            this_row = []
            for x_column in range(self.number_of_columns):
                new_tile_type = random.choice(self.terrain_types)
                new_display_tile = DisplayTile(new_tile_type)
                new_display_tile.rect.x = x_column * 10
                new_display_tile.rect.y = y_row * 10
                self.display_tiles.add(new_display_tile)

                new_game_tile = GameTile(new_tile_type[0], x_column, y_row)
                this_row.append(new_game_tile)
            self.game_tile_rows.append(this_row)

        self.generate_vegetation()

        for new_buf in range(self.number_of_buffalo):

            x_position = random.randint(0, self.number_of_columns - 1)
            y_position = random.randint(0, self.number_of_rows - 1)

            Buffalo(x_position, y_position, self)

    def generate_vegetation(self):
        for wheat_clusters in range(self.number_of_wheat_clusters):
            self.generate_wheat_cluster()

    def get_random_coordinates(self, x_lower, x_upper, y_lower, y_upper):
        x_position = random.randint(x_lower, x_upper)
        y_position = random.randint(y_lower, y_upper)

        return (x_position, y_position)


    def generate_wheat_cluster(self):
        wheat_cluster_placed = False
        while not wheat_cluster_placed:
            space_occupied = False
            coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
            if self.game_tile_rows[coordinates[1]][coordinates[0]].entity_group[Wheat]:
                space_occupied = True
            if not space_occupied:
                # needed to make neighbors
                cluster_center_wheat = Wheat(coordinates[0], coordinates[1], self)
                wheat_cluster_placed = True
        self.entity_group[Wheat].add(cluster_center_wheat)
        cluster_left_edge = max(cluster_center_wheat.tile_x - 7, 0)
        cluster_right_edge = min(cluster_center_wheat.tile_x + 7, (self.number_of_columns - 1))
        cluster_top_edge = max(cluster_center_wheat.tile_y - 7, 0)
        cluster_bottom_edge = min(cluster_center_wheat.tile_y + 7, (self.number_of_rows - 1))
        number_of_neighbors = random.randint(3, 9)
        for wheat in range(number_of_neighbors):
            neighbor_placed = False
            while not neighbor_placed:
                space_occupied = False
                coordinates = self.get_random_coordinates(cluster_left_edge, cluster_right_edge, cluster_top_edge, cluster_bottom_edge)
                if self.game_tile_rows[coordinates[1]][coordinates[0]].entity_group[Wheat]:
                    space_occupied = True
                if not space_occupied:
                    Wheat(coordinates[0], coordinates[1], self)
                    neighbor_placed = True


    def world_scroll(self, shift_x, shift_y, screen_width, screen_height):
        if 0 >= self.x_shift + shift_x >= -(self.width - screen_width):
            self.x_shift += shift_x
        if 0 >= self.y_shift + shift_y >= -(self.height - screen_height):
            self.y_shift += shift_y
