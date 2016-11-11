import item
import art
import pygame
import random
import entity
import ui
import utilities


class Armor(item.Item):
    equippable = True
    item_type = "Armor"
    ranged = False

    def __init__(self, name, material, value, weight, armor_value, equipment_type):
        super().__init__(material + name,
                         round(value *
                               item.material_value_multipliers[material]),
                         weight)
        self.equipment_type = equipment_type
        self.armor_name = name
        self.material = material
        self.armor_value = armor_value
        self.is_equipped = False
        self.sprite = pygame.sprite.Sprite()
        self.set_surfaces()

    def set_surfaces(self):
        self.icon = art.armor_icons[self.equipment_type][self.material]
        self.spritesheet = art.armor_spritesheets[self.equipment_type][self.armor_name][self.material]
        self.walk_frames = [self.spritesheet.get_image(0, 0, 20, 40)]
        for x in range(5):
            self.walk_frames.append(self.spritesheet.get_image(20, 0, 20, 40))
        for x in range(5):
            self.walk_frames.append(self.spritesheet.get_image(60, 0, 20, 40))
        for x in range(5):
            self.walk_frames.append(self.spritesheet.get_image(80, 0, 20, 40))
        for x in range(5):
            self.walk_frames.append(self.spritesheet.get_image(100, 0, 20, 40))
        for x in range(5):
            self.walk_frames.append(self.spritesheet.get_image(120, 0, 20, 40))
        for x in range(5):
            self.walk_frames.append(self.spritesheet.get_image(140, 0, 20, 40))
        self.attack_frames = []
        for x in range(1):
            self.attack_frames.append(self.spritesheet.get_image(0, 80, 20, 40))
        for x in range(6):
            self.attack_frames.append(self.spritesheet.get_image(20, 80, 20, 40))
        for x in range(6):
            self.attack_frames.append(self.spritesheet.get_image(40, 80, 20, 40))
        for x in range(4):
            self.attack_frames.append(self.spritesheet.get_image(60, 80, 20, 40))
        for x in range(3):
            self.attack_frames.append(self.spritesheet.get_image(80, 80, 40, 40))
        for x in range(4):
            self.attack_frames.append(self.spritesheet.get_image(120, 80, 40, 40))
        self.ranged_frames = []
        for x in range(1):
            self.ranged_frames.append(self.spritesheet.get_image(0, 160, 40, 40))
        for x in range(6):
            self.ranged_frames.append(self.spritesheet.get_image(40, 160, 40, 40))
        for x in range(6):
            self.ranged_frames.append(self.spritesheet.get_image(80, 160, 40, 40))
        for x in range(4):
            self.ranged_frames.append(self.spritesheet.get_image(120, 160, 40, 40))
        for x in range(3):
            self.ranged_frames.append(self.spritesheet.get_image(160, 160, 40, 40))
        for x in range(4):
            self.ranged_frames.append(self.spritesheet.get_image(0, 160, 40, 40))
        self.sprite.image = self.walk_frames[0]

    def set_frame(self, frame, action):
        if action == 0:
            frame_list = self.walk_frames
        elif action == 1:
            frame_list = self.attack_frames
        elif action == 2:
            frame_list = self.ranged_frames
        self.sprite.image = frame_list[frame]


class Boots(Armor):

    def __init__(self, name, material, value, weight, armor_value):
        super().__init__(name, material, value, weight, armor_value, "Boots")


class Gloves(Armor):

    def __init__(self, name, material, value, weight, armor_value):
        super().__init__(name, material, value, weight, armor_value, "Gloves")


class Helmet(Armor):

    def __init__(self, name, material, value, weight, armor_value):
        super().__init__(name, material, value, weight, armor_value, "Helmet")


class BodyArmor(Armor):
    def __init__(self, name, material, value, weight, armor_value):
        super().__init__(name, material, value, weight, armor_value, "Body Armor")


def get_hood(value, level, material=None):
    return Helmet("Hood", "", 10, 1, 0)


def get_helmet(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    return Helmet("Helm", material, 20, 5, 10)


def get_full_helmet(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    return Helmet("Full Helm", material, 30, 10, 15)


def get_breastplate(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    return BodyArmor("Breastplate", material, 50, 25, 25)


def get_tunic(value, level, material=None):
    return BodyArmor("Tunic", "", 5, 2, 2)


def get_gloves(value, level, material=None):
    return Gloves("Gloves", "", 5, 1, 1)


def get_gauntlets(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    return Gloves("Gauntlets", material, 10, 2, 5)


def get_boots(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    return Boots("Boots", material, 10, 5, 10)


def get_leather_boots(value, level, material=None):
    return Boots("Boots", "", 10, 2, 2)


clothing_functions = [get_gloves, get_tunic, get_hood, get_leather_boots]
armor_functions = [get_boots, get_gauntlets, get_breastplate, get_helmet, get_full_helmet]
