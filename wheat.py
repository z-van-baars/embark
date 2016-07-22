import pygame
import utilities
import entity
import random


class Wheat(entity.Entity):
    def __init__(self, x, y):
        super().__init__((x + 2), (y + 2), utilities.colors.wheat_gold, 6, 6)
        self.age = 0

    def do_thing(self):
        self.age += 1