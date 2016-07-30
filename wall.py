import entity
import pygame


class Wall(entity.Entity):
    occupies_tile = True

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        
        self.sprite.image = pygame.Surface([10, 10])
        self.sprite.image.fill((180, 210, 217))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 10
        self.sprite.rect.y = self.tile_y * 10
