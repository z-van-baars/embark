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
        self.current_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
        self.is_valid = True

    def __lt__(self, other):
        if self.tile_x < other.tile_x:
            return True
        elif self.tile_y < other.tile_y:
            return True
        else:
            return False

    def expire(self):
        self.current_map.entity_group[type(self)].remove(self)
