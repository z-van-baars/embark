import structure
import art
import random
import armor
import item
import weapon
import ui


stock_references = {"Weapons": weapon.weapon_functions,
                    "Armor": armor.armor_functions, 
                    "Swords": [weapon.weapon_functions[0], weapon.weapon_functions[3]], 
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


class Container(structure.Structure):
    interactable = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Chest"
        self.set_images(self.image_key)
        self.display_name = "Container"
        self.items = {"Weapon": [],
                      "Armor": [],
                      "Misc": []}
        self.value = 10
        self.opened = False

    def use(self, game_state):
        if not self.opened:
            self.items_list = []
            self.fill(game_state.player.level)
            self.opened = True
        new_loot_window = ui.LootMenu(game_state, (0, 0), self)
        new_loot_window.menu_onscreen()
        self.activated = False


class Chest(Container):
    interactable = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Chest"
        self.display_name = "Chest"
        self.set_images(self.image_key)
        self.stock_categories = ["Weapons", "Armor", "Treasures"]

    def fill(self, player_level):

        items_to_stock = []
        stock_minimum, stock_maximum = 2, 10
        number_of_items_to_stock = random.randint(stock_minimum, stock_maximum)
        for x in range(number_of_items_to_stock):
            possible_items = stock_references[random.choice(self.stock_categories)]
            items_to_stock.append(random.choice(possible_items)(20, player_level))
        for each in items_to_stock:
            self.items[each.my_type].append(each)


class Corpse(Container):
    interactable = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map, creature, player_level):
        self.corpse_type = creature.display_name
        super().__init__(x, y, current_map)
        self.display_name = creature.display_name + " Corpse"
        self.image_key = self.display_name
        self.set_images(self.image_key)
        self.stock_categories = ["Weapons", "Armor", "Commodities", "Treasures"]

        self.fill(player_level, self.corpse_type)
        self.opened = True

    def fill(self, player_level, corpse_type):
        items_to_stock = []
        stock_minimum, stock_maximum = 2, 10
        number_of_items_to_stock = random.randint(stock_minimum, stock_maximum)
        for x in range(number_of_items_to_stock):
            possible_items = stock_references[random.choice(self.stock_categories)]
            items_to_stock.append(random.choice(possible_items)(20, player_level))
        for each in items_to_stock:
            self.items[each.my_type].append(each)

    def tick_cycle(self):
        self.age += 1
        if self.age > 10000:
            self.expire(1, True)
