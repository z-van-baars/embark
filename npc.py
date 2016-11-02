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


class Npc(entity.SentientEntity):
    occupies_tile = True
    interactable = True
    my_type = "Npc"
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map, display_name="New NPC"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.target_coordinates = None
        self.path = None
        self.speed = 1
        self.time_since_last_move = 0
        self.activated = False
        self.equipped_weapon = None
        self.image_index = None

        self.gold = 10
        self.items_list = []
        self.health = 100
        self.max_health = 100

        self.dialogue_pages = [["Line 1",
                                "Line 2",
                                "Line 3"]]

    def tick_cycle(self):
        self.age += 1


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
        self.image_key = "Guard"
        self.set_images(self.image_key)

    def tick_cycle(self):
        self.age += 1

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()


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
        self.image_key = "Male Villager"
        self.set_images(self.image_key)

    def tick_cycle(self):
        self.age += 1

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()
        self.activated = False


class Lord(Npc):
    height = 2

    def __init__(self, x, y, current_map, display_name="Lord"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.dialogue_pages = [["Be quick Adventurer, I am the lord of",
                                "Threlkeld and have many matters to attend to."]]
        self.image_key = "Lord"
        self.set_images(self.image_key)

    def tick_cycle(self):
        self.age += 1

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()
        self.activated = False


class Sage(Npc):
    height = 2

    def __init__(self, x, y, current_map, display_name="Sage"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.dialogue_pages = [["I advise the lord on all matters magical and arcane.",
                                "There is more to this world than meets the eye."]]
        self.image_key = "Sage"
        self.set_images(self.image_key)

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
        self.dialogue_pages = [["Hello Adventurer! Lots to do here", "in Poopybutts."], [" Lots of quality goods for sale here"]]
        self.image_key = "Merchant"
        self.set_images(self.image_key)
        self.restock_items(50)

    def tick_cycle(self):
        self.age += 1

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()
        self.activated = False

    def restock_items(self, player_level):
        for x in range(20):
            possible_items = [random.choice(weapon.weapon_functions)(20, player_level),
                              random.choice(random.choice(item.item_functions))()]
            self.items_list.append(random.choice(possible_items))
