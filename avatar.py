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
    my_type = "Avatar"

    def __init__(self, x, y, current_map):
        super().__init__(x, y + 1, current_map)
        self.display_name = "PLAYER"
        self.sprite.image = avatar_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - 1) * 20
        self.change_x = 0
        self.change_y = 0
        self.target_coordinates = None
        self.target_object = None
        self.path = None
        self.speed = 10
        self.time_since_last_move = 0

        self.health = 100
        self.max_health = 100
        self.gold = 10
        self.actions = [
                    "None",
                    "Move",
                    "Attack",
                    "Use"]
        self.action = 0

    def tick_cycle(self):
        my_position = (self.tile_x, self.tile_y)
        self.age += 1
        self.time_since_last_move += 1
        if self.action == 0:
            pass
        elif self.action == 1:
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.change_x, self.change_y = self.calculate_step(my_position, self.target_object, self.target_coordinates)
                self.move()
        elif self.action == 2:
            pass
        elif self.action == 3:
            if not self.target_object.tile_x == self.target_coordinates[0] or not self.target_object.tile_y == self.target_coordinates[1]:
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.change_x, self.change_y = self.calculate_step(my_position, self.target_object, self.target_coordinates)
                self.move()
            if not self.path:
                # is the target still there?
                self.use(self.target_object)

    def use(self, target_object):
        statement = "used " + target_object.display_name
        print(statement)
        target_object.dialogue()

    def assign_target(self, current_map, mouse_pos):
        my_position = (self.tile_x, self.tile_y)
        tile_x = int((mouse_pos[0] - current_map.x_shift) / 20)
        tile_y = int((mouse_pos[1] - current_map.y_shift) / 20)
        # 0 == invalid (cant move there and wont process the click)
        # 1 == empty space, will move to this spot
        # 2 == interactible thing, door, chest, creature, npc - will path to this object and then interact
        target_type = None
        if not utilities.within_map(tile_x, tile_y, current_map):
            target_type = 0
        else:
            if current_map.game_tile_rows[tile_y][tile_x].is_occupied():
                if current_map.game_tile_rows[tile_y][tile_x].entity_group["Npc"]:
                    self.target_object = current_map.game_tile_rows[tile_y][tile_x].entity_group["Npc"][0]
                    target_type = 2
                else:
                    target_type = 0
            else:
                target_type = 1

        self.get_path_behavior(current_map, my_position, tile_x, tile_y, target_type)

    def get_path_behavior(self, current_map, my_position, tile_x, tile_y, target_type):
        if target_type == 0:
            print('Invalid target, cannot path')
        elif target_type == 1:
            self.target_coordinates = tile_x, tile_y
            self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
            self.action = 1
        elif target_type == 2:
            self.target_coordinates = tile_x, tile_y
            self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
            self.target_coordinates = tile_x, tile_y
            target_tile = current_map.game_tile_rows[self.target_coordinates[1]][self.target_coordinates[0]]
            self.path.tiles.insert(0, target_tile)
            self.action = 3

    def calculate_step(self, my_position, target_object, target_coordinates):
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
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - 1) * 20
        self.change_x = 0
        self.change_y = 0

        # am I at my target?
        if len(self.path.tiles) < 2:
            self.target_coordinates = None
            self.path = None
            self.action = 0
        else:
            self.path.tiles.pop(0)
