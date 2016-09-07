import pygame
import random
import utilities
from tile import DisplayTile
from game_tile import GameTile
import npc
from avatar import Avatar
import creature
import flora


class Map(object):
    def __init__(self, dimensions):
        self.width = (dimensions[0] * 20)
        self.height = (dimensions[1] * 20)
        self.number_of_columns = dimensions[0]
        self.number_of_rows = dimensions[1]
        self.game_tile_rows = []
        self.x_shift = 0
        self.y_shift = 0

        self.display_tiles = pygame.sprite.Group()
        self.entity_group = {
                            "Terrain": [],
                            "Structure":[],
                            "Flora": [],
                            "Creature": [],
                            "Npc": [],
                            "Avatar": []
                            }
        self.number_of_buffalo = 0
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
                new_display_tile.rect.x = x_column * 20
                new_display_tile.rect.y = y_row * 20
                self.display_tiles.add(new_display_tile)
                this_row.append(GameTile(new_tile_type[0], x_column, y_row))
            self.game_tile_rows.append(this_row)

        self.generate_vegetation()

        npc.Guard(20, 20, self)

        Avatar(1, 1, self)

        for new_buffalo in range(self.number_of_buffalo):
            buffalo_placed = False
            while not buffalo_placed:
                coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
                tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
                if not tile.is_occupied:
                    creature.Buffalo(coordinates[0], coordinates[1], self)
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

    def generate_wheat_cluster(self):
        wheat_cluster_placed = False
        while not wheat_cluster_placed:
            coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
            tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
            if not tile.is_occupied():
                # needed to make neighbors
                cluster_center_wheat = flora.Wheat(tile.column, tile.row, self)
                wheat_cluster_placed = True
        nearby_tiles = utilities.get_nearby_tiles(self, (cluster_center_wheat.tile_x, cluster_center_wheat.tile_y), 8)
        number_of_neighbors = random.randint(3, 9)
        for wheat in range(number_of_neighbors):
            neighbor_placed = False
            while not neighbor_placed:
                tile = random.choice(nearby_tiles)
                if not tile.is_occupied():
                    flora.Wheat(tile.column, tile.row, self)
                    neighbor_placed = True

    def generate_forest(self):
        forest_placed = False
        while not forest_placed:
            coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
            tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
            if not tile.is_occupied():
                # needed to make neighbors
                forest_center_tree = flora.Tree(tile.column, tile.row, self)
                forest_placed = True
        number_of_neighbors = random.randint(9, 19)
        for new_tree in range(number_of_neighbors):
            neighbor_placed = False
            while not neighbor_placed:
                nearby_tiles = utilities.get_nearby_tiles(self, (forest_center_tree.tile_x, forest_center_tree.tile_y), forest_center_tree.group_generation_max_distance)
                tile = random.choice(nearby_tiles)
                if not tile.is_occupied():
                    flora.Tree(tile.column, tile.row, self)
                    neighbor_placed = True

    def world_scroll(self, shift_x, shift_y, screen_width, screen_height):
        if 0 >= self.x_shift + shift_x >= -(self.width - screen_width):
            self.x_shift += shift_x
        if 0 >= self.y_shift + shift_y >= -(self.height - screen_height):
            self.y_shift += shift_y
