import item
import art
import pygame
import random
import entity
import ui
import utilities


class Projectile(entity.MovingEntity):
    footprint = (1, 1)
    interactable = False
    my_type = "Projectile"

    def __init__(self, current_map, x, y, x2, y2, speed, damage, target):
        super().__init__(x, y, current_map)
        self.current_map = current_map
        self.sprite = pygame.sprite.Sprite()
        self.set_surfaces()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x2 + 10
        self.sprite.rect.y = y2 - 13
        self.true_x = x2 + 10
        self.true_y = y2 - 13
        self.target = target

        self.speed = speed
        self.damage = damage
        width = self.target.footprint[1]
        height = self.target.height
        self.target_x = (target.tile_x * 20) + (width * 20) - ((width / 2) * 20)
        self.target_y = (target.tile_y * 20) - (height * 20) + 20 + ((height / 2) * 20)
        self.change_x = None
        self.change_y = None

    def get_vector(self):
        (self.change_x, self.change_y) = utilities.get_vector(self, self.sprite.rect.x + 19, self.sprite.rect.y, self.target_x, self.target_y)

    def travel(self):
        if not self.change_x:
            self.get_vector()
        self.true_x -= self.change_x
        self.true_y -= self.change_y
        self.sprite.rect.x = round(self.true_x)
        self.sprite.rect.y = round(self.true_y)
        self.tile_x = int(self.sprite.rect.x / 20)
        self.tile_y = int(self.sprite.rect.y / 20)
        if not utilities.within_map(self.tile_x, self.tile_y, self.current_map):
            self.current_map.entity_group["Projectile"].remove(self)
        self.target_check()

    def target_check(self):
        target_top = self.target.tile_y * 20 - ((self.target.height / 2) * 20)
        target_bottom = self.target.tile_y * 20 + 20
        target_left = self.target.tile_x * 20
        target_right = self.target.tile_x * 20 + (20 * self.target.footprint[0])
        if utilities.check_if_inside(target_left,
                                     target_right,
                                     target_top,
                                     target_bottom,
                                     (self.sprite.rect.x + 20, self.sprite.rect.y)):
            self.target.health -= self.damage
            ui.HitBox(self.current_map, self.target.sprite.rect.x, self.target.sprite.rect.y, self.damage, "Avatar")
            self.target.healthbar.active = True
            self.current_map.entity_group["Projectile"].remove(self)


class Arrow(Projectile):
    def __init__(self, current_map, x, y, x2, y2, target):
        super().__init__(current_map, x, y, x2, y2, 5, 10, target)

    def set_surfaces(self):
        self.sprite.image = art.arrow_image


class BlueFireball(Projectile):
    def __init__(self, current_map, x, y, x2, y2, target):
        self.casting = True
        self.frame = 0
        self.impacting = False
        super().__init__(current_map, x, y, x2, y2, 5, 5, target)
        self.sprite.rect.x = x2
        self.sprite.rect.y = y2 - 10
        self.true_x = x2
        self.true_y = y2 - 10

    def set_surfaces(self):
        self.travel_frames = []
        self.cast_frames = []
        self.impact_frames = []
        for x in range(2):
            self.travel_frames.append(art.blue_fireball_spritesheet.get_image(0, 0, 20, 20))
        for x in range(2):
            self.travel_frames.append(art.blue_fireball_spritesheet.get_image(20, 0, 20, 20))
        for x in range(2):
            self.travel_frames.append(art.blue_fireball_spritesheet.get_image(40, 0, 20, 20))
        for x in range(2):
            self.travel_frames.append(art.blue_fireball_spritesheet.get_image(60, 0, 20, 20))

        for x in range(5):
            self.cast_frames.append(art.blue_fireball_spritesheet.get_image(0, 20, 20, 20))
        for x in range(5):
            self.cast_frames.append(art.blue_fireball_spritesheet.get_image(20, 20, 20, 20))
        for x in range(5):
            self.cast_frames.append(art.blue_fireball_spritesheet.get_image(40, 20, 20, 20))
        for x in range(5):
            self.cast_frames.append(art.blue_fireball_spritesheet.get_image(60, 20, 20, 20))

        for x in range(5):
            self.impact_frames.append(art.blue_fireball_spritesheet.get_image(0, 40, 20, 20))
        for x in range(5):
            self.impact_frames.append(art.blue_fireball_spritesheet.get_image(20, 40, 20, 20))
        for x in range(5):
            self.impact_frames.append(art.blue_fireball_spritesheet.get_image(40, 40, 20, 20))
        for x in range(5):
            self.impact_frames.append(art.blue_fireball_spritesheet.get_image(60, 40, 20, 20))
        self.get_image()

    def get_image(self):
        if self.casting:
            self.frame += 1
            self.sprite.image = self.cast_frames[self.frame]
            if self.frame == len(self.cast_frames) - 1:
                self.casting = False
                self.frame = 0
        elif not self.casting and not self.impacting:
            self.frame += 1
            self.sprite.image = self.travel_frames[self.frame]
            if self.frame == len(self.travel_frames) - 1:
                self.frame = 0
        elif not self.casting and self.impacting:
            self.frame += 1
            self.sprite.image = self.impact_frames[self.frame]
            if self.frame == len(self.impact_frames) - 1:
                self.impacting = False
                self.current_map.entity_group["Projectile"].remove(self)

    def travel(self):
        if self.casting or self.impacting:
            self.get_image()
        else:
            if not self.change_x:
                self.get_vector()
            self.true_x -= self.change_x
            self.true_y -= self.change_y
            self.sprite.rect.x = round(self.true_x)
            self.sprite.rect.y = round(self.true_y)
            self.tile_x = int(self.sprite.rect.x / 20)
            self.tile_y = int(self.sprite.rect.y / 20)
            if not utilities.within_map(self.tile_x, self.tile_y, self.current_map):
                self.current_map.entity_group["Projectile"].remove(self)
            self.target_check()
            self.get_image()

    def target_check(self):
        target_top = self.target.tile_y * 20 - ((self.target.height / 2) * 20)
        target_bottom = self.target.tile_y * 20 + 20
        target_left = self.target.tile_x * 20
        target_right = self.target.tile_x * 20 + (20 * self.target.footprint[0])
        if utilities.check_if_inside(target_left,
                                     target_right,
                                     target_top,
                                     target_bottom,
                                     (self.sprite.rect.x + 20, self.sprite.rect.y)):
            self.target.health -= self.damage
            ui.HitBox(self.current_map, self.target.sprite.rect.x, self.target.sprite.rect.y, self.damage, "Other")
            self.target.healthbar.active = True
            self.impacting = True
            self.frame = 0


class Weapon(item.Item):
    equippable = True
    item_type = "Weapon"
    ranged = False

    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(material + name,
                         round(value *
                               item.material_value_multipliers[material]),
                         weight)
        self.material = material
        self.equipment_type = "Weapon"
        self.attack_speed = attack_speed
        self.melee_damage = round(melee_damage *
                                  item.material_damage_multipliers[material])
        self.ranged_damage = round(ranged_damage *
                                   item.material_damage_multipliers[material])
        self.sprite = pygame.sprite.Sprite()
        self.set_surfaces()
        self.sprite.rect = self.sprite.image.get_rect()
        self.is_equipped = False


class Sword(Weapon):

    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(name, material, value, weight, melee_damage, ranged_damage, attack_speed)
        self.range = 1.5

    def set_surfaces(self):
        self.icon = art.sword_icon
        self.frames = []
        for x in range(3):
            self.frames.append(art.sword_spritesheet.get_image(0, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.sword_spritesheet.get_image(20, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.sword_spritesheet.get_image(40, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.sword_spritesheet.get_image(60, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.sword_spritesheet.get_image(80, 0, 40, 80))
        for x in range(5):
            self.frames.append(art.sword_spritesheet.get_image(120, 0, 40, 80))
        self.sprite.image = self.frames[0]

    def set_frame(self, frame):
        self.sprite.image = self.frames[frame]


class Mace(Weapon):

    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(name, material, value, weight, melee_damage, ranged_damage, attack_speed)
        self.range = 1.5

    def set_surfaces(self):
        self.icon = art.mace_icon
        self.frames = []
        for x in range(3):
            self.frames.append(art.mace_spritesheet.get_image(0, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.mace_spritesheet.get_image(20, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.mace_spritesheet.get_image(40, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.mace_spritesheet.get_image(60, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.mace_spritesheet.get_image(80, 0, 40, 80))
        for x in range(5):
            self.frames.append(art.mace_spritesheet.get_image(120, 0, 40, 80))
        self.sprite.image = self.frames[0]

    def set_frame(self, frame):
        self.sprite.image = self.frames[frame]


class Spear(Weapon):

    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(name, material, value, weight, melee_damage, ranged_damage, attack_speed)
        self.range = 1.5

    def set_surfaces(self):
        self.icon = art.spear_icon
        self.frames = []
        for x in range(3):
            self.frames.append(art.spear_spritesheet.get_image(0, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.spear_spritesheet.get_image(20, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.spear_spritesheet.get_image(40, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.spear_spritesheet.get_image(60, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.spear_spritesheet.get_image(80, 0, 40, 80))
        for x in range(5):
            self.frames.append(art.spear_spritesheet.get_image(120, 0, 40, 80))
        self.sprite.image = self.frames[0]

    def set_frame(self, frame):
        self.sprite.image = self.frames[frame]


class Dagger(Weapon):

    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(name, material, value, weight, melee_damage, ranged_damage, attack_speed)
        self.range = 1.5

    def set_surfaces(self):
        self.icon = art.dagger_icon
        self.frames = []
        for x in range(3):
            self.frames.append(art.dagger_spritesheet.get_image(0, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.dagger_spritesheet.get_image(20, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.dagger_spritesheet.get_image(40, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.dagger_spritesheet.get_image(60, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.dagger_spritesheet.get_image(80, 0, 40, 80))
        for x in range(5):
            self.frames.append(art.dagger_spritesheet.get_image(120, 0, 40, 80))
        self.sprite.image = self.frames[0]

    def set_frame(self, frame):
        self.sprite.image = self.frames[frame]


class Axe(Weapon):

    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(name, material, value, weight, melee_damage, ranged_damage, attack_speed)
        self.range = 1.5

    def set_surfaces(self):
        self.icon = art.axe_icon
        self.frames = []
        for x in range(3):
            self.frames.append(art.axe_spritesheet.get_image(0, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.axe_spritesheet.get_image(20, 0, 20, 80))
        for x in range(3):
            self.frames.append(art.axe_spritesheet.get_image(40, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.axe_spritesheet.get_image(60, 0, 20, 80))
        for x in range(4):
            self.frames.append(art.axe_spritesheet.get_image(80, 0, 40, 80))
        for x in range(5):
            self.frames.append(art.axe_spritesheet.get_image(120, 0, 40, 80))
        self.sprite.image = self.frames[0]

    def set_frame(self, frame):
        self.sprite.image = self.frames[frame]


class Bow(Weapon):
    ranged = True

    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(name, material, value, weight, melee_damage, ranged_damage, attack_speed)
        self.ammunition_type = Arrow
        self.range = 14

    def set_surfaces(self):
        self.icon = art.bow_icon
        self.frames = []
        for x in range(1):
            self.frames.append(art.bow_spritesheet.get_image(0, 0, 40, 80))
        for x in range(6):
            self.frames.append(art.bow_spritesheet.get_image(20, 0, 40, 80))
        for x in range(6):
            self.frames.append(art.bow_spritesheet.get_image(60, 0, 40, 80))
        for x in range(4):
            self.frames.append(art.bow_spritesheet.get_image(100, 0, 40, 80))
        for x in range(3):
            self.frames.append(art.bow_spritesheet.get_image(140, 0, 40, 80))
        for x in range(4):
            self.frames.append(art.bow_spritesheet.get_image(20, 0, 40, 80))
        self.sprite.image = self.frames[0]

    def set_frame(self, frame):
        self.sprite.image = self.frames[frame]

    def fire(self, current_map, x, y, target_object):
        x2 = x * 20
        y2 = y * 20
        self.ammunition_type(current_map, x, y, x2, y2, target_object)


class MagicBow(Bow):
    def __init__(self, name, material, value, weight, melee_damage, ranged_damage, attack_speed):
        super().__init__(name, material, value, weight, melee_damage, ranged_damage, attack_speed)
        self.ammunition_type = BlueFireball

        self.sprite.image = art.shadebrute_spritesheet.get_image(100, 100, 10, 10)


def get_longsword(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    # quality = item.choose_quality(value, level)
    return Sword("Longsword", material, 30, 5, 10, 0, 5)


def get_bow(value, level, material=None):
    return Bow("Bow", "", 15, 3, 0, 10, 10)


def get_axe(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    # quality = item.choose_quality(value, level)
    return Axe("Battleaxe", material, 25, 7, 13, 0, 10)


def get_mace(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    # quality = item.choose_quality(value, level)
    return Mace("Mace", material, 20, 7, 15, 0, 12)


def get_spear(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    # quality = item.choose_quality(value, level)
    return Spear("Spear", material, 15, 6, 10, 0, 15)


def get_dagger(value, level, material=None):
    if material is None:
        material = item.choose_material(value, level)
    # quality = item.choose_quality(value, level)
    return Dagger("Dagger", material, 10, 3, 3, 0, 8)


def get_magic_bow(value, level, material=None):
    return MagicBow("Magic Bow", "", 15, 4, 0, 10, 10)


weapon_functions = [get_longsword, get_bow, get_axe, get_dagger, get_mace, get_spear, get_magic_bow]

