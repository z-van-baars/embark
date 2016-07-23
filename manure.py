import pygame
import utilities
import entity
import random


class Manure(entity.Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, utilities.colors.brown, 2, 2, current_map)
    	