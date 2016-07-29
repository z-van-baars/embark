import pygame
import entity


class Vegetation(entity.Entity):
    def __init__(self, x, y, color, width, height, current_map):
        super().__init__(x, y, color, width, height, current_map, None)
        self.age = 0
        self.group_generation_max_distance = 0

    def tick_cycle(self):
        self.age += 1
