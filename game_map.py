import pygame
import random
import utilities
from utilities import GlobalVariables
from tile import DisplayTile
from buffalo import Buffalo
from wheat import Wheat
from game_tile import GameTile
from herd import Herd
from wall import Wall
from tree import Tree


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
        self.entity_group[Wheat] = []
        self.entity_group[Buffalo] = []
        self.entity_group[Wall] = []
        self.entity_group[Tree] = []
        self.herds = []

        self.number_of_buffalo = 0
        self.number_of_buffalo_herds = 0
        self.number_of_forests = 1
        self.number_of_wheat_clusters = 0

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
                this_row.append(GameTile(new_tile_type[0], x_column, y_row))
            self.game_tile_rows.append(this_row)

        self.generate_vegetation()

        for new_herd in range(self.number_of_buffalo_herds):
            self.generate_buffalo_herd(Buffalo)
        for new_buffalo in range(self.number_of_buffalo):
            buffalo_placed = False
            while not buffalo_placed:
                coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
                tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
                if not tile.is_occupied:
                    Buffalo(coordinates[0], coordinates[1], self)
                    buffalo_placed = True

    def generate_vegetation(self):
        for forests in range(self.number_of_forests):
            self.generate_forest()
        for wheat_clusters in range(self.number_of_wheat_clusters):
            self.generate_wheat_cluster()

    def get_random_coordinates(self, x_lower, x_upper, y_lower, y_upper):
        x_position = random.randint(x_lower, x_upper)
        y_position = random.randint(y_lower, y_upper)

        return (x_position, y_position)

    def generate_buffalo_herd(self, animal_type):
        alpha_placed = False
        new_herd = Herd(self)
        while not alpha_placed:
            coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
            tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
            if not tile.is_occupied():
                # needed to make neighbors
                new_herd_alpha = animal_type(coordinates[0], coordinates[1], self, new_herd)
                new_herd.alpha = new_herd_alpha
                new_herd_alpha.is_alpha = True
                alpha_placed = True
        nearby_tiles = utilities.get_nearby_tiles(self, (new_herd_alpha.tile_x, new_herd_alpha.tile_y), new_herd_alpha.herd_radius)
        number_of_herd_members = random.randint(new_herd_alpha.min_initial_herd_size, new_herd_alpha.max_initial_herd_size)
        for beast in range(number_of_herd_members):
            beast_placed = False
            while not beast_placed:
                tile = random.choice(nearby_tiles)
                if not tile.is_occupied():
                    Buffalo(tile.column, tile.row, self, new_herd)
                    beast_placed = True
        self.herds.append(new_herd)

    def generate_wheat_cluster(self):
        wheat_cluster_placed = False
        while not wheat_cluster_placed:
            coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
            tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
            if not tile.is_occupied():
                # needed to make neighbors
                cluster_center_wheat = Wheat(tile.column, tile.row, self)
                wheat_cluster_placed = True
        nearby_tiles = utilities.get_nearby_tiles(self, (cluster_center_wheat.tile_x, cluster_center_wheat.tile_y), 8)
        number_of_neighbors = random.randint(3, 9)
        for wheat in range(number_of_neighbors):
            neighbor_placed = False
            while not neighbor_placed:
                tile = random.choice(nearby_tiles)
                if not tile.is_occupied():
                    Wheat(tile.column, tile.row, self)
                    neighbor_placed = True

    def generate_forest(self):
        forest_placed = False
        while not forest_placed:
            coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
            tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
            if not tile.is_occupied():
                # needed to make neighbors
                forest_center_tree = Tree(tile.column, tile.row, self)
                forest_placed = True
        number_of_neighbors = random.randint(9, 19)
        for new_tree in range(number_of_neighbors):
            neighbor_placed = False
            while not neighbor_placed:
                nearby_tiles = utilities.get_nearby_tiles(self, (forest_center_tree.tile_x, forest_center_tree.tile_y), forest_center_tree.group_generation_max_distance)
                tile = random.choice(nearby_tiles)
                if not tile.is_occupied():
                    Tree(tile.column, tile.row, self)
                    neighbor_placed = True

    def world_scroll(self, shift_x, shift_y, screen_width, screen_height):
        if 0 >= self.x_shift + shift_x >= -(self.width - screen_width):
            self.x_shift += shift_x
        if 0 >= self.y_shift + shift_y >= -(self.height - screen_height):
            self.y_shift += shift_y
