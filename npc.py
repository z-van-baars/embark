import pygame
import entity
import utilities
import item
import ui
import random
import art
import weapon

pygame.init()
pygame.display.set_mode([0, 0])


class Npc(entity.Entity):
    occupies_tile = True
    interactable = True
    my_type = "Npc"
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map, display_name="New NPC"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.change_x = 0
        self.change_y = 0
        self.target_coordinates = None
        self.path = None
        self.speed = 1
        self.time_since_last_move = 0
        self.activated = False

        self.items_list = []
        self.health = 100
        self.max_health = 100

        self.dialogue_pages = [["Line 1",
                                "Line 2",
                                "Line 3"]]

    def tick_cycle(self):
        self.age += 1

    def use(self):
        print()


class Guard(Npc):
    height = 2

    def __init__(self, x, y, current_map, display_name="Town Guard"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.dialogue_pages = [["Hello Adventurer!",
                                "Welcome to the town of Swindon,",
                                "I keep the peace here."]]
        self.set_images()

    def set_images(self):
        self.sprite.image = art.guard_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def tick_cycle(self):
        self.age += 1

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()
        self.activated = False


class Villager(Npc):
    height = 2

    def __init__(self, x, y, current_map, display_name="Villager"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.dialogue_pages = [["Hello Adventurer!",
                                "Welcome to the town of Swindon,",
                                "I live here"]]
        self.set_images()

    def set_images(self):
        self.sprite.image = random.choice(art.male_villager_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def tick_cycle(self):
        self.age += 1

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()
        self.activated = False


class Merchant(Npc):
    height = 2

    def __init__(self, x, y, current_map, display_name="Merchant"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.gold = 100
        self.items_list = []
        for each in item.rubbish:
            for iteration in range(9):
                new_item = item.Item(each[0], each[1], each[2])
                self.items_list.append(new_item)
        for each in weapon.weapons:
            new_item = item.Item(each[0], each[1], each[2])
            self.items_list.append(new_item)
        self.dialogue_pages = [["Hello Adventurer! Lots to do here", "in Poopybutts."], [" Lots of quality goods for sale here"]]
        self.set_images()

    def tick_cycle(self):
        self.age += 1

    def set_images(self):
        self.sprite.image = art.merchant_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()
        self.activated = False
