import item
import art
import pygame
import utilities


class Projectile(object):
    footprint = (1, 1)

    def __init__(self, current_map, x, y, x2, y2, speed, damage, target):
        self.current_map = current_map
        self.sprite = pygame.sprite.Sprite()
        self.set_surfaces()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x2 + 10
        self.sprite.rect.y = y2 - 13
        self.tile_x = x
        self.tile_y = y
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

        self.current_map.entity_group["Projectile"].append(self)

    def get_vector(self):
        (self.change_x, self.change_y) = utilities.get_vector(self, self.sprite.rect.x + 20, self.sprite.rect.y, self.target_x, self.target_y)

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
        target_top = self.target_y - ((self.target.height / 2) * 20)
        target_bottom = self.target_y + 20
        target_left = self.target_x
        target_right = self.target_x + (20 * self.target.footprint[0])
        if utilities.check_if_inside(target_left,
                                     target_right,
                                     target_top,
                                     target_bottom,
                                     (self.sprite.rect.x + 20, self.sprite.rect.y)):
            print("strike")
            self.current_map.entity_group["Projectile"].remove(self)


class Arrow(Projectile):
    def __init__(self, current_map, x, y, x2, y2, target):
        super().__init__(current_map, x, y, x2, y2, 5, 10, target)

    def set_surfaces(self):
        self.sprite.image = art.arrow_image


class Weapon(item.Item):
    equipable = True
    my_type = "Weapon"
    ranged = False

    def __init__(self, name, value, weight, attack, attack_speed):
        super().__init__(name, value, weight)
        self.attack_speed = attack_speed
        self.attack = attack


class Sword(Weapon):

    def __init__(self, name, value, weight, attack, attack_speed):
        super().__init__(name, value, weight, attack, attack_speed)
        self.sprite = pygame.sprite.Sprite()
        self.set_surfaces()
        self.sprite.rect = self.sprite.image.get_rect()

    def set_surfaces(self):
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


class Axe(Weapon):

    def __init__(self, name, value, weight, attack, attack_speed):
        super().__init__(name, value, weight, attack, attack_speed)
        self.sprite = pygame.sprite.Sprite()
        self.set_surfaces()
        self.sprite.rect = self.sprite.image.get_rect()

    def set_surfaces(self):
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

    def __init__(self, name, value, weight, attack, attack_speed):
        super().__init__(name, value, weight, attack, attack_speed)
        self.ammunition_type = Arrow
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = art.bow_image
        self.sprite.rect = self.sprite.image.get_rect()

    def fire(self, current_map, x, y, target_object):
        x2 = x * 20
        y2 = y * 20
        self.ammunition_type(current_map, x, y, x2, y2, target_object)


weapons = [("Iron Longsword", 10, 3, 5, 10), ("Iron Battleaxe", 25, 7, 10, 10), ("Oak Bow", 15, 4, 10, 10)]
