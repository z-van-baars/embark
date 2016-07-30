import entity
import pygame


class Wall(entity.Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image = pygame.Surface([10, 10])
        self.image.fill((180, 210, 217))
        self.rect = self.image.get_rect()
        self.incompatible_objects = [Wall]

        self.rect.x = self.tile_x * 10
        self.rect.y = self.tile_y * 10
