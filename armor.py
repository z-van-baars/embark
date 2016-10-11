import item
import art
import pygame
import random
import entity
import ui
import utilities


class Armor(item.Item):
    equippable = True
    my_type = "Weapon"
    ranged = False

    def __init__(self, name, material, value, weight, armor_value):
        super().__init__(material + name,
                         round(value *
                               item.material_value_multipliers[material]),
                         weight)
        self.material = material
        self.armor_value = armor_value
        self.set_surfaces()
        self.is_equipped = False

    def equip(self, player):
        if player.equipped_armor:
            player.equipped_armor.unequip(player)
        player.armor += self.armor_value
        player.equipped_armor = self
        self.is_equipped = True

    def unequip(self, player):
        player.armor -= self.armor_value
        player.equipped_armor = None
        self.is_equipped = False


class Boots(Armor):

    def __init__(self, name, material, value, weight, armor_value):
        super().__init__(name, material, value, weight, armor_value)

    def set_surfaces(self):
        self.icon = art.boots_icon


def get_boots():
    return Boots("Boots", "Iron ", 10, 2, 5)


armor_functions = [get_boots]
