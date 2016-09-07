import entity
import pygame

pygame.init()
pygame.display.set_mode([0, 0])

wall_image = pygame.image.load("art/avatar/avatar.png").convert()


class Structure(entity.Entity):
    occupies_tile = True
    my_type = "Structure"

    def __init__(self, x, y, current_map):
        super().__init__()


class Wall(Structure):
    occupies_tile = True

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.sprite.image = wall_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20
