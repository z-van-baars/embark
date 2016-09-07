import pygame
import entity
import utilities

pygame.init()
pygame.display.set_mode([0, 0])

guard_image = pygame.image.load("art/npc/guard.png").convert()
guard_image.set_colorkey(utilities.colors.key)


class Npc(entity.Entity):
    occupies_tile = True
    interactable = True
    my_type = "Npc"

    def __init__(self, x, y, current_map, display_name="New NPC"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.sprite.image = pygame.Surface([20, 40])
        self.sprite.image.fill((255, 187, 0))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20
        self.change_x = 0
        self.change_y = 0
        self.target_coordinates = None
        self.path = None
        self.speed = 1
        self.time_since_last_move = 0

        self.health = 100
        self.max_health = 100

    def tick_cycle(self):
        self.age += 1

    def dialogue(self):
        print("%s: Hello from the kingdom of poopburg" % self.display_name)


class Guard(Npc):
    def __init__(self, x, y, current_map, display_name="Town Guard"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.sprite.image = guard_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - 1) * 20
        self.speed = 1

        self.health = 100
        self.max_health = 100

    def tick_cycle(self):
        self.age += 1

    def dialogue(self):
        print("%s: Welcome to the town of poopybutts, in the kingdom of poopburg" % self.display_name)
