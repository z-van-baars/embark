import pygame
import entity

pygame.init()
pygame.display.set_mode([0, 0])


class Flora(entity.StationaryEntity):
    my_type = "Flora"
    interactable = False
    occupies_tile = True

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_index = None

    def tick_cycle(self):
        self.age += 1


class Tree(Flora):
    footprint = (1, 2)
    width = 2
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Pine Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class PineTree(Flora):
    footprint = (1, 2)
    height = 4
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Pine Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class SmallOakTree(Flora):
    footprint = (1, 2)
    height = 3
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Small Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class SmallOakTreeFall(Flora):
    footprint = (1, 2)
    height = 3
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Small Fall Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class SmallOakTreeBare(Flora):
    footprint = (1, 2)
    height = 3
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Small Bare Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class LargeOakTree(Flora):
    footprint = (1, 2)
    height = 5
    width = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Large Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class LargeFallOakTree(Flora):
    footprint = (1, 2)
    height = 5
    width = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Large Fall Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class LargeYellowOakTree(Flora):
    footprint = (1, 2)
    height = 5
    width = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Large Yellow Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class LargeBareOakTree(Flora):
    footprint = (1, 2)
    height = 5
    width = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Large Bare Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class LargeBareDarkOakTree(Flora):
    footprint = (1, 2)
    height = 5
    width = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Large Dark Bare Oak Tree"
        self.set_images(self.image_key)
        self.display_name = "Tree"


class Wheat(Flora):
    footprint = (1, 1)
    height = 2
    width = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wheat"
        self.set_images(self.image_key)
        self.display_name = "Wheat"
