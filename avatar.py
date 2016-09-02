import pygame
import entity
import utilities
import navigate

pygame.init()
pygame.display.set_mode([0, 0])

avatar_image = pygame.image.load("art/avatar/avatar.png").convert()
avatar_image.set_colorkey(utilities.colors.key)


class Avatar(entity.Entity):
    occupies_tile = True

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.display_name = "PLAYER"
        self.sprite.image = avatar_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 10
        self.sprite.rect.y = self.tile_y * 10
        self.change_x = 0
        self.change_y = 0
        self.target_coordinates = None
        self.path = None
        self.speed = 10
        self.time_since_last_move = 0

        self.health = 100
        self.max_health = 100
        self.gold = 10

    def tick_cycle(self):
        self.age += 1
        self.time_since_last_move += 1
        if self.target_coordinates:
            # print(self.change_x, self.change_y, self.tile_x. self.tile_y)
            self.change_x, self.change_y = self.calculate_step((self.tile_x, self.tile_y))
            if self.path and len(self.path.tiles) > 0:
                if self.time_since_last_move >= self.speed:
                    self.time_since_last_move = 0
                    self.move()

    def assign_target(self, current_map, mouse_pos):
        my_position = (self.tile_x, self.tile_y)
        tile_x = int((mouse_pos[0] + current_map.x_shift) / 10)
        tile_y = int((mouse_pos[1] + current_map.y_shift) / 10)
        if utilities.within_map(tile_x, tile_y, current_map):
            self.target_coordinates = tile_x, tile_y
            self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)

    def calculate_step(self, my_position):
        # I have a target but no path to it
        if not self.path:
            self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
        # I am at my target
        if len(self.path.tiles) < 1:
            self.target_object, self.target_coordinates = None, None
            self.path = None
            return (0, 0)
        # I have a target and a path that is at least 1 tile long
        else:
            change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            if self.path.tiles[0].is_occupied():
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
                change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            return change_x, change_y

    def check_tile(self, x_change, y_change):
        x = self.tile_x
        y = self.tile_y
        x = x + x_change
        y = y + y_change
        if x < 0 or x > len(self.current_map.game_tile_rows[0]):
            return False
        if y < 0 or y > len(self.current_map.game_tile_rows):
            return False

        tile = self.current_map.game_tile_rows[y][x]
        if tile.is_occupied():
            return False
        else:
            return True

    def move(self):
        self.tile_x += self.change_x
        if self.tile_x < 0:
            self.tile_x = 0
        elif self.tile_x >= self.current_map.number_of_columns:
            self.tile_x = self.current_map.number_of_columns - 1
        self.tile_y += self.change_y
        if self.tile_y < 0:
            self.tile_y = 0
        elif self.tile_y >= self.current_map.number_of_rows:
            self.tile_y = self.current_map.number_of_rows - 1

        self.assign_tile()
        self.sprite.rect.x = self.tile_x * 10
        self.sprite.rect.y = self.tile_y * 10
        self.change_x = 0
        self.change_y = 0
        self.path.tiles.pop(0)
