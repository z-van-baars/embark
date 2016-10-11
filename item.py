import random
import utilities


class Item(object):
    equippable = False

    def __init__(self, name, value, weight):
        super().__init__()
        self.name = name
        self.value = value
        self.weight = weight


def get_gold_ingot():
    return Item("Gold Ingot", 100, 1)


def get_iron_ingot():
    return Item("Iron Ingot", 10, 1)


def get_steel_ingot():
    return Item("Steel Ingot", 20, 1)


def get_wheat():
    return Item("Wheat", 5, 1)


def get_calipers():
    return Item("Calipers", 1, 1)


def get_lockpick():
    return Item("Lockpick", 5, 1)


rubbish = [("Scrap Paper", 1, 1), ("Broken Sword", 2, 5), ("Burnt Bread", 1, 2)]
treasures = [("Gold Bar", 30, 1), ("Ye Flaske", 1000, 1)]

qualities = ["Worthless ", "Shabby ", "Acceptable ", "Ordinary ", "Fine ", "Resplendent ", "Titanic "]
quality_colors = {"Worthless ": utilities.colors.worthless,
                  "Shabby ": utilities.colors.shabby,
                  "Acceptable ": utilities.colors.acceptable,
                  "Ordinary ": utilities.colors.ordinary,
                  "Fine ": utilities.colors.fine,
                  "Resplendent ": utilities.colors.resplendent,
                  "Titanic ": utilities.colors.titanic}

quality_value_multipliers = {"Worthless ": 0.1,
                             "Shabby ": 0.25,
                             "Acceptable ": 0.75,
                             "Ordinary ": 1,
                             "Fine ": 2.5,
                             "Resplendent ": 10,
                             "Titanic ": 20}

quality_damage_multipliers = {"Worthless ": 0.1,
                              "Shabby ": 0.5,
                              "Acceptable ": 0.9,
                              "Ordinary ": 1,
                              "Fine ": 1.1,
                              "Resplendent ": 1.4,
                              "Titanic ": 2.0}

materials = ["Bronze ", "Iron ", "Steel ", "Mithril ", "Adamantine "]
material_damage_multipliers = {"": 1.0,
                               "Bronze ": 0.5,
                               "Iron ": 1.0,
                               "Steel ": 5.0,
                               "Mithril ": 10,
                               "Adamantine ": 20}

material_value_multipliers = {"": 1.0,
                              "Bronze ": 1.0,
                              "Iron ": 2.0,
                              "Steel ": 5.0,
                              "Mithril ": 10,
                              "Adamantine ": 20}


def choose_quality(value, player_level):
    quality_roll = utilities.roll_dice(2, 5)
    quality_roll -= 1
    if random.randint(1, 100) < player_level:
        quality_roll += utilities.roll_dice(1, 5)
    quality = round(quality_roll / 2)
    return qualities[quality]


def choose_material(value, player_level):
    material_roll = utilities.roll_dice(2, 4) - 1
    material_roll = min(material_roll, (utilities.roll_dice(2, 4) - 1))
    material_roll = min(material_roll, (utilities.roll_dice(2, 4) - 1))
    material_roll = min(material_roll, (utilities.roll_dice(2, 4) - 1))
    if random.randint(1, 100) < value:
        material_roll += utilities.roll_dice(1, round(player_level / 4) + 1)
    material = round(material_roll / 4)
    if material > 4:
        material = 4
    return materials[material]


item_functions = [get_wheat, get_calipers, get_lockpick, get_gold_ingot, get_iron_ingot, get_steel_ingot]
