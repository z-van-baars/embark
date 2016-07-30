import pygame
import entity


class Vegetation(entity.Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.age = 0
        self.group_generation_max_distance = 0

    def tick_cycle(self):
        self.age += 1
