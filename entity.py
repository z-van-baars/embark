import pygame
import utilities

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height, current_map):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_map = current_map

    def __lt__(self, other):
        if self.rect.x < other.rect.x:
            return True
        elif self.rect.y < other.rect.y:
            return True
        else:
            return False

    def expire(self):
        self.current_map.entity_group[type(self)].remove(self)
