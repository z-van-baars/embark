import pygame
import utilities


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height, current_map):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.width = width
        self.height = height
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.tile_x = x
        self.tile_y = y
        self.rect.x = self.tile_x * 10 + ((10 - self.width) / 2)
        self.rect.y = self.tile_y * 10 + ((10 - self.height) / 2)
        self.current_map = current_map
        self.current_tile = None
        self.is_valid = True

        self.current_map.entity_group[type(self)].add(self)

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
        self.current_tile.entity_group[type(self)].remove(self)
        self.current_map.entity_group[type(self)].remove(self)

    def assign_tile(self):
        if self.current_tile:
            self.current_tile.entity_group[type(self)].remove(self)
            self.current_tile = None
        self.current_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
        self.current_tile.entity_group[type(self)].append(self)

    def leave_tile(self):
        self.current_tile.entity_group[type(self)].remove(self)
