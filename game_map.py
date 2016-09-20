import pygame
import random
import utilities
from tile import DisplayTile
from tile import ImageTile
from game_tile import GameTile
import npc
from avatar import Avatar
import creature
import flora
import structure

pygame.init()
pygame.display.set_mode([0, 0])


class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width * 20, height * 20])
        self.image.fill(utilities.colors.black)
        self.rect = self.image.get_rect()


class Map(object):
    def __init__(self, name, dimensions, screen_dimensions, interior):
        self.background = None
        self.name = name
        self.screen_dimensions = screen_dimensions
        self.width = (dimensions[0] * 20)
        self.height = (dimensions[1] * 20)
        self.number_of_columns = dimensions[0]
        self.number_of_rows = dimensions[1]
        self.game_tile_rows = []

        self.interior = interior
        self.number_of_buffalo = 0
        self.number_of_forests = 0
        self.number_of_wheat_clusters = 0


        self.display_tiles = pygame.sprite.Group()
        self.x_shift = 0
        self.y_shift = 0
        self.hitboxes = []
        
        self.entity_group = {
                            "Terrain": [],
                            "Structure":[],
                            "Flora": [],
                            "Creature": [],
                            "Npc": [],
                            "Avatar": []
                            }

    def map_generation(self):
        wood_1 = pygame.image.load("art/wood_tile.png").convert()
        grass_1 = pygame.image.load("art/background/grass_1.png").convert()
        interior_terrain_types = [wood_1]
        exterior_terrain_types = [grass_1]
        self.game_tile_rows = []
        self.healthbars = []
        self.background = Background(int(self.width / 20), int(self.height / 20))

        if not self.interior:

            for y_row in range(self.number_of_rows):
                this_row = []
                for x_column in range(self.number_of_columns):
                    new_tile_image = random.choice(exterior_terrain_types)
                    x = x_column * 20
                    y = y_row * 20
                    this_row.append(GameTile(x_column, y_row))
                    self.background.image.blit(new_tile_image, (x, y))
                self.game_tile_rows.append(this_row)
            self.generate_vegetation()

            for new_buffalo in range(self.number_of_buffalo):
                buffalo_placed = False
                while not buffalo_placed:
                    coordinates = self.get_random_coordinates(0, self.number_of_columns - 1, 0, self.number_of_rows - 1)
                    tile = self.game_tile_rows[coordinates[1]][coordinates[0]]
                    if not tile.is_occupied:
                        creature.Buffalo(coordinates[0], coordinates[1], self)
                        buffalo_placed = True
        else:
            for y_row in range(self.number_of_rows):
                this_row = []
                for x_column in range(self.number_of_columns):
                    new_tile_image = random.choice(interior_terrain_types)
                    x = x_column * 20
                    y = y_row * 20
                    this_row.append(GameTile(x_column, y_row))
                    self.background.image.blit(new_tile_image, (x, y))
                self.game_tile_rows.append(this_row)

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

    def scroll_check(self, x, y):
        if x + self.x_shift < 200:
           self.world_scroll(20, 0, self.screen_dimensions[0], self.screen_dimensions[1])
        elif x + self.x_shift > self.screen_dimensions[0] - 200:
            self.world_scroll(-20, 0, self.screen_dimensions[0], self.screen_dimensions[1])
        if y + self.y_shift < 200:
            self.world_scroll(0, 20, self.screen_dimensions[0], self.screen_dimensions[1])
        elif y + self.y_shift > self.screen_dimensions[1] - 280:
            self.world_scroll(0, -20, self.screen_dimensions[0], self.screen_dimensions[1])

    def world_scroll(self, shift_x, shift_y, screen_width, screen_height):
        if 0 >= self.x_shift + shift_x >= -(self.width - screen_width):
            self.x_shift += shift_x
        if 0 >= self.y_shift + shift_y >= -(self.height - screen_height):
            self.y_shift += shift_y

    def draw_to_screen(self, screen, screen_width, screen_height):
        objects_to_draw = []
        for each in self.entity_group:
            for entity in self.entity_group[each]:
                objects_to_draw.append(entity)
        rows_to_draw = []
        for y_level in range(self.height):
            this_row = []
            for entity in objects_to_draw:
                if entity.tile_y == y_level:
                    this_row.append(entity)
            rows_to_draw.append(this_row)

        for row in rows_to_draw:
            for entity in row:
                if utilities.any_tile_visible(screen_width, screen_height, self.x_shift, self.y_shift, entity):
                    screen.blit(entity.sprite.image, [(entity.sprite.rect.x + self.x_shift), (entity.sprite.rect.y + self.y_shift)])
                objects_to_draw.remove(entity)

