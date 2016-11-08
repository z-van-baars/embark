import pygame
import entity
import utilities
import item
import ui
import random
import art
import weapon
import armor

pygame.init()
pygame.display.set_mode([0, 0])

global_rumors = [["The weather is starting to get colder."],
                 ["Good steel is hard to come by these days."]]
town_rumors = {"Swindon": [["Our town has been raided, and you're asking about rumors??!"]],
               "Threlkeld": [["I think jim needs to lay off the booze"],
                             ["The taxes around here are ridiculous.", "I think I might have to move somewhere cheaper, like Swindon"]]}
global_directions = [["Ya can't get theya from heyu."]]
town_directions = {"Swindon": [["I'd get out of here if I were you."]],
                   "Threlkeld": [["The market is at the center of town.", "The lord's castle is to the west of town."]]}

male_first_names = ["Rychard",
                    "Hudd",
                    "Hubert",
                    "Gylbard",
                    "Gervasius",
                    "Henry",
                    "Rolf",
                    "Frederic",
                    "Abel",
                    "John",
                    "Bernard",
                    "Elias",
                    "Armand",
                    "Curtis",
                    "Ferry",
                    "Gregory",
                    "Rex",
                    "Thomas",
                    "Geffery",
                    "Girard"
                    "Bertram",
                    "Milo",
                    "Owen",
                    "Elbert",
                    "Herbert",
                    "Gabriel",
                    "Cristoff",
                    "Karl",
                    "Mainard",
                    "Reeve",
                    "Tristram",
                    "Trystan",
                    "Yves",
                    "Reynauld",
                    "Petyr",
                    "Jem",
                    "Jaemes",
                    "Walter",
                    "Piers",
                    "Sam",
                    "Randall",
                    "Stephen",
                    "Steven",
                    "Hobard",
                    "Gale",
                    "Tyon"]
last_names = ["Talbot",
              "Merrick",
              "Ysembert",
              "Bartelmeu",
              "Asher",
              "Normann",
              "Barnard",
              "Bernier",
              "Fulbert",
              "Hamlin",
              "Alucard",
              "Cromwell",
              "Hildebrand",
              "Degore",
              "Botulf",
              "Bartholomeus",
              "Wilkin",
              "Teebald",
              "Hervey",
              "Harman",
              "Renfry",
              "Audri",
              "Guiraudet",
              "Oudart",
              "Gipp",
              "Urianus",
              "Huelin",
              "Gilliam",
              "Alphonse",
              "Maucolyn",
              "Gerontious",
              "Arnett",
              "Segar",
              "Ancel",
              "Searle",
              "Hunfray",
              "Bartel",
              "Perinnet",
              "Dru",
              "Guiart",
              "Hemmet",
              "Armundus",
              "Clarembaut",
              "Adinet",
              "Engerramet",
              "Ranulfus"]

stock_quantities = {"Small": (10, 20),
                    "Medium": (25, 40),
                    "Large": (50, 100),
                    "Huge": (200, 250)}

stock_references = {"Swords": [weapon.weapon_functions[0], weapon.weapon_functions[3]], 
                    "Spears": [weapon.weapon_functions[5]],
                    "Axes": [weapon.weapon_functions[2]],
                    "Maces": [weapon.weapon_functions[4]],
                    "Bows": [weapon.weapon_functions[1]],
                    "Clothing": armor.clothing_functions,
                    "Helmets": [armor.armor_functions[3], armor.armor_functions[4]],
                    "Boots": [armor.armor_functions[0]],
                    "Breastplates": [armor.armor_functions[2]],
                    "Gauntlets": [armor.armor_functions[1]],
                    "Commodities": item.commodity_functions,
                    "Junk": item.junk_functions,
                    "Tools": item.tool_functions,
                    "Treasures": item.treasure_functions}


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
        self.image_index = None

        self.gold = 10
        self.items = {"Weapon": [],
                      "Armor": [],
                      "Misc": []}
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
        if current_map.name in town_rumors:
            my_rumors = random.choice(town_rumors[current_map.name])
        else:
            my_rumors = random.choice(global_rumors)
        if current_map.name in town_directions:
            my_directions = random.choice(town_directions[current_map.name])
        else:
            my_directions = random.choice(global_directions)
        self.dialogue = {"Rumors": my_rumors,
                         "Directions": my_directions}
        self.greeting = [["Hello Adventurer, welcome to the town of Swindon,",
                          "I keep the peace here, so don't cause trouble, and we'll have no problems."]]
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
        self.display_name = "{0} {1}".format(random.choice(male_first_names), random.choice(last_names))
        self.speed = 1
        self.health = 100
        self.max_health = 100
        # character limit is 70
        if current_map.name in town_rumors:
            my_rumors = random.choice(town_rumors[current_map.name])
        else:
            my_rumors = random.choice(global_rumors)
        if current_map.name in town_directions:
            my_directions = random.choice(town_directions[current_map.name])
        else:
            my_directions = random.choice(global_directions)
        self.dialogue = {"Rumors": my_rumors,
                         "Directions": my_directions}
        self.greeting = [["Hello Adventurer! Welcome to the town of Swindon,"]]
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
        if current_map.name in town_rumors:
            my_rumors = random.choice(town_rumors[current_map.name])
        else:
            my_rumors = random.choice(global_rumors)
        if current_map.name in town_directions:
            my_directions = random.choice(town_directions[current_map.name])
        else:
            my_directions = random.choice(global_directions)
        self.dialogue = {"Rumors": my_rumors,
                         "Directions": my_directions}
        self.greeting = [["Be quick Adventurer, I am the lord of {0} and have many matters to attend to."]]
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
        if current_map.name in town_rumors:
            my_rumors = random.choice(town_rumors[current_map.name])
        else:
            my_rumors = random.choice(global_rumors)
        if current_map.name in town_directions:
            my_directions = random.choice(town_directions[current_map.name])
        else:
            my_directions = random.choice(global_directions)
        self.dialogue = {"Rumors": my_rumors,
                         "Directions": my_directions}
        self.greeting = [["Hello adventurer.  Are you a follower of the arcane arts?",
                          "I advise the lord on all matters magical and arcane.",
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
    is_merchant = True

    def __init__(self, x, y, current_map, display_name="Merchant"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.gold = 100
        if current_map.name in town_rumors:
            my_rumors = random.choice(town_rumors[current_map.name])
        else:
            my_rumors = random.choice(global_rumors)
        if current_map.name in town_directions:
            my_directions = random.choice(town_directions[current_map.name])
        else:
            my_directions = random.choice(global_directions)
        self.dialogue = {"Rumors": my_rumors,
                         "Directions": my_directions}
        self.greeting = [["Hello Adventurer! Lots to do here in __TOWN_NAME__."], [" Lots of quality goods for sale here"]]
        self.image_key = "Merchant"
        self.set_images(self.image_key)
        
        self.stock_categories = ["Commodities", "Helmets", "Swords", "Axes", "Tools"]
        self.stock_quantity = "Medium"
        self.restock_items(50)


    def tick_cycle(self):
        self.age += 1

    def use(self, game_state):
        new_dialogue_menu = ui.DialogueMenu(game_state, (0, 0), self)
        new_dialogue_menu.menu_onscreen()
        self.activated = False

    def restock_items(self, player_level):
        items_to_stock = []
        stock_minimum, stock_maximum = stock_quantities[self.stock_quantity]
        number_of_items_to_stock = random.randint(stock_minimum, stock_maximum)
        for x in range(number_of_items_to_stock):
            possible_items = stock_references[random.choice(self.stock_categories)]
            items_to_stock.append(random.choice(possible_items)(20, player_level))
        for each in items_to_stock:
            self.items[each.my_type].append(each)
