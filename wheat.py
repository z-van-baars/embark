import pygame
import utilities
import entity
import random


class Wheat(entity.Entity):
    def __init__(self, x, y, current_map):
        super().__init__((x + 2), (y + 2), utilities.colors.wheat_gold, 6, 6, current_map)
        self.age = 0
        self.food_value = 25

    def do_thing(self):
        self.age += 1