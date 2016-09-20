import pygame
import utilities


class Entity(object):
    occupies_tile = False

    def __init__(self, x, y, current_map):
        super().__init__()
        self.tile_x = x
        self.tile_y = y
        self.current_map = current_map
        self.current_tile = None
        self.is_valid = True
        self.age = 0
        self.sprite = pygame.sprite.Sprite()
        self.display_name = "-N/A-"

        self.current_map.entity_group[self.my_type].append(self)
        self.assign_tile()

    def __lt__(self, other):
        if self.tile_x < other.tile_x:
            return True
        elif self.tile_y < other.tile_y:
            return True
        else:
            return False

    def expire(self):
        self.is_valid = False
        self.current_map.entity_group[self.my_type].remove(self)


    def assign_tile(self):        
        if self.current_tile:
            self.leave_tile()

        self.current_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
        initial_x = self.tile_x
        initial_y = self.tile_y - (self.footprint[1] - 1)
        for tile_y in range(initial_y, initial_y + (self.footprint[1])):
            for tile_x in range(initial_x, initial_x + self.footprint[0]):
                tile = self.current_map.game_tile_rows[tile_y][tile_x]
                tile.entity_group[self.my_type].append(self)

    def house_assign_tile(self):
        self.current_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
        initial_x = self.current_tile.column
        initial_y = self.current_tile.row - 2
        for tile_y in range(initial_y, initial_y + 3):
            for tile_x in range(initial_x, initial_x + 4):
                if utilities.within_map(tile_x, tile_y, self.current_map):
                    self.current_map.game_tile_rows[tile_y][tile_x].entity_group["Structure"].append(self)


    def assign_map(self, new_map):
        if self.current_map:
            self.current_map.entity_group[self.my_type].remove(self)
        self.current_map = new_map

        self.current_map.entity_group[self.my_type].append(self)        

    def leave_tile(self):
        initial_x = self.current_tile.column
        initial_y = self.current_tile.row - (self.footprint[1] - 1)
        for tile_y in range(initial_y, initial_y + (self.footprint[1])):
            for tile_x in range(initial_x, initial_x + self.footprint[0]):                
                tile = self.current_map.game_tile_rows[tile_y][tile_x]
                tile.entity_group[self.my_type].remove(self)
        self.current_tile = None

