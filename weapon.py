import item
import art
import pygame


class Weapon(item.Item):
    equipable = True
    my_type = "Weapon"
    ranged = False

    def __init__(self, name, value, weight, attack, attack_speed):
        super().__init__(name, value, weight)
        self.attack_speed = attack_speed
        self.attack = attack
        self.sprite = pygame.sprite.Sprite()
        self.set_surfaces()
        self.sprite.rect = self.sprite.image.get_rect()


class Sword(Weapon):

    def __init__(self, name, value, weight, attack, attack_speed):
        super().__init__(name, value, weight, attack, attack_speed)

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

    def set_surfaces(self):
        pass


weapons = [("Iron Longsword", 10, 3, 5, 10), ("Iron Battleaxe", 25, 7, 10, 10), ("Oak Bow", 15, 4, 10, 10)]
