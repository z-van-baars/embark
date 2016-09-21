import random
import utilities


class Item(object):
    equipable = False

    def __init__(self, name, value, weight):
        super().__init__()
        self.name = name
        self.value = value
        self.weight = weight


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

materials = ["Bronze ", "Iron ", "Steel "]
material_damage_multipliers = {"Bronze ": 0.5,
                               "Iron ": 1.0,
                               "Steel ": 5.0}

material_value_multipliers = {"Bronze ": 0.5,
                              "Iron ": 1.0,
                              "Steel ": 5.0}


def get_quality(value):
    quality_roll = utilities.roll_dice(3, 4)
    if random.randint(0, 100) < value:
        quality_roll += utilities.roll_dice(3, 4)
    quality = round(quality_roll / 3)
    return qualities[quality]


def get_material(value):
    return random.choice(materials)
