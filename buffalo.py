import pygame
import utilities
import entity
import random

class Buffalo(entity.Entity):
    def __init__(self, x, y):
        super().__init__((x + 2), (y + 2), utilities.colors.red, 6, 6)
        self.speed = 60
        self.age = 0
        self.ticks_without_food = 0
        self.change_x = 0
        self.change_y = 0

    def do_thing(self):
        self.age += 1
        self.ticks_without_food += 1
        self.idle()
        self.move()
        self.change_x = 0
        self.change_y = 0

    def move(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def idle(self):
        action = random.randint(0, 800)
        if action <= 10:
            self.change_x = 10
        elif 10 < action <= 20:
            self.change_x = -10
        elif 20 < action <= 30:
            self.change_y = 10
        elif 30 < action <= 40:
            self.change_y = -10
        elif action > 750:
            self.change_x = 0
            self.change_y = 0