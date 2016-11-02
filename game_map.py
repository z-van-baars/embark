import pygame
import random
import utilities
from game_tile import GameTile
import creature
import flora

pygame.init()
pygame.display.set_mode([0, 0])


class ObjectLayer(object):
    def __init__(self):
        super().__init__()
        self.z_levels = []


class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width * 20, height * 20])
        self.image.fill(utilities.colors.black)
        self.rect = self.image.get_rect()


class Map(object):
    def __init__(self, name, dimensions, screen_dimensions):
        self.background = None
        self.name = name
        self.screen_dimensions = screen_dimensions
        self.width = (dimensions[0] * 20)
        self.height = (dimensions[1] * 20)
        self.number_of_columns = dimensions[0]
        self.number_of_rows = dimensions[1]
        self.game_tile_rows = []

        self.number_of_buffalo = 0
        self.number_of_forests = 0
        self.number_of_wheat_clusters = 0
        self.display_tiles = pygame.sprite.Group()
        self.x_shift = 0
        self.y_shift = 0
        self.hitboxes = []
        self.entity_group = {"Terrain": [],
                             "Structure": [],
                             "Flora": [],
                             "Creature": [],
                             "Npc": [],
                             "Avatar": [],
                             "Projectile": []}

    def map_generation(self):
        grass_1 = pygame.image.load("art/background/grass_1.png").convert()
        self.game_tile_rows = []
        self.healthbars = []
        self.background = Background(int(self.width / 20), int(self.height / 20))

        for y_row in range(self.number_of_rows):
            this_row = []
            for x_column in range(self.number_of_columns):
                x = x_column * 20
                y = y_row * 20
                this_row.append(GameTile(x_column, y_row))
                self.background.image.blit(grass_1, (x, y))
            self.game_tile_rows.append(this_row)

    def update_object_layer(self):
        self.object_layer = ObjectLayer()
        max_height = 1
        for each in self.entity_group["Flora"]:
            max_height = max(each.height, max_height)
        for each in self.entity_group["Terrain"]:
            max_height = max(each.height, max_height)
        for each in self.entity_group["Structure"]:
            max_height = max(each.height, max_height)
        for z in range(max_height + 1):
            new_z_level = Background(self.width / 20, self.height / 20)

            self.build_object_layer_z_level(int(self.width / 20), int(self.height / 20), new_z_level, z)
            self.object_layer.z_levels.append(new_z_level)

    def build_object_layer_z_level(self, width, height, background_layer, z_level):
        # get_image(x pixels, y pixels, width pixels, height pixels)

        background_layer.image.fill(utilities.colors.key)

        objects_to_draw = []
        for each in self.entity_group["Flora"]:
            if each.height >= z_level:
                objects_to_draw.append(each)
        for each in self.entity_group["Terrain"]:
            if each.height >= z_level:
                objects_to_draw.append(each)
        for each in self.entity_group["Structure"]:
            if each.height >= z_level:
                objects_to_draw.append(each)
        rows_to_draw = []
        for y_level in range(int(self.height / 20)):
            this_row = []
            for entity in objects_to_draw:
                if entity.tile_y == y_level:
                    this_row.append(entity)
            rows_to_draw.append(this_row)

        for row in rows_to_draw:
            for entity in row:
                image_height = entity.height * 20
                image_slice = utilities.get_image(entity.sprite.image, 0, image_height - (z_level * 20), entity.width * 20, 20)
                background_layer.image.blit(image_slice, [entity.tile_x * 20 + int((entity.footprint[0] * 20 - entity.width * 20) / 2),
                                                          (entity.tile_y - z_level + 1) * 20])
        background_layer.image.set_colorkey(utilities.colors.key)

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
        self.x_shift += shift_x
        self.y_shift += shift_y
        if self.x_shift > 0:
            self.x_shift = 0
        elif self.x_shift < -(self.width - screen_width) and self.width > screen_width:
            self.x_shift = -(self.width - screen_width)
        if self.y_shift > 0:
            self.y_shift = 0
        elif self.y_shift < -(self.height - screen_height + 80) and self.height > screen_height:
            self.y_shift = -(self.height - screen_height + 80)

    def draw_actors(self, screen, screen_width, screen_height, z_level):
        actors_to_draw = []
        for each in self.entity_group["Avatar"]:
            if each.height >= z_level:
                actors_to_draw.append(each)
        for each in self.entity_group["Npc"]:
            if each.height >= z_level:
                actors_to_draw.append(each)
        for each in self.entity_group["Creature"]:
            if each.height >= z_level:
                actors_to_draw.append(each)
        for each in self.entity_group["Projectile"]:
            actors_to_draw.append(each)
        rows_to_draw = []
        for y_level in range(self.height):
            this_row = []
            for entity in actors_to_draw:
                if entity.tile_y == y_level:
                    this_row.append(entity)
            rows_to_draw.append(this_row)

        for row in rows_to_draw:
            for entity in row:
                if utilities.any_tile_visible(screen_width, screen_height, self.x_shift, self.y_shift, entity):
                    # screen.blit(entity.sprite.image, [(entity.sprite.rect.x + self.x_shift), (entity.sprite.rect.y + self.y_shift)])
                    image_height = entity.height * 20
                    image_slice = utilities.get_image(entity.sprite.image, 0, image_height - (z_level * 20), entity.width * 20, 20)
                    screen.blit(image_slice, [entity.tile_x * 20 + int((entity.footprint[0] * 20 - entity.width * 20) / 2) + self.x_shift,
                                              (entity.tile_y - z_level + 1) * 20 + self.y_shift])
                    if entity.my_type == "Avatar" or entity.my_type == "Npc" or entity.my_type == "Creature":
                        if entity.equipped_weapon:
                            screen.blit(entity.equipped_weapon.sprite.image,
                                        [(entity.sprite.rect.x + self.x_shift - 1),
                                         (entity.sprite.rect.y + self.y_shift - 42)])



