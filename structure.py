import entity
import pygame
import ui
import utilities
import item
import random

pygame.init()
pygame.display.set_mode([0, 0])


class Structure(entity.Entity):
    occupies_tile = True
    my_type = "Structure"

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.activated = False


class StoneWall(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.display_name = "Stone Wall"
        self.set_images()

    def set_images(self):
        stone_wall_image = pygame.image.load("art/structures/walls/wall.png").convert()
        self.sprite.image = stone_wall_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class HouseInteriorWall(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        
        self.display_name = "Wall"
        self.set_images()

    def set_images(self):
        house_interior_wall = pygame.image.load("art/structures/walls/house_interior_1.png")
        self.sprite.image = house_interior_wall
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20



class Palisade(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.display_name = "Palisade Wall"
        self.set_images()


class VerticalPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        

    def set_images(self):
        vertical_palisade_1 = pygame.image.load("art/structures/walls/v_palisade_1.png").convert()
        vertical_palisade_2 = pygame.image.load("art/structures/walls/v_palisade_2.png").convert()
        vertical_palisade_1.set_colorkey(utilities.colors.key)
        vertical_palisade_2.set_colorkey(utilities.colors.key)
        vertical_palisade_images = [vertical_palisade_1, vertical_palisade_2]
        self.sprite.image = random.choice(vertical_palisade_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class HorizontalPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        
    def set_images(self):
        horizontal_palisade_1 = pygame.image.load("art/structures/walls/h_palisade_1.png").convert()
        horizontal_palisade_2 = pygame.image.load("art/structures/walls/h_palisade_2.png").convert()
        horizontal_palisade_3 = pygame.image.load("art/structures/walls/h_palisade_3.png").convert()
        horizontal_palisade_1.set_colorkey(utilities.colors.key)
        horizontal_palisade_2.set_colorkey(utilities.colors.key)
        horizontal_palisade_3.set_colorkey(utilities.colors.key)
        horizontal_palisade_images = [horizontal_palisade_1, horizontal_palisade_2, horizontal_palisade_3]
        self.sprite.image = random.choice(horizontal_palisade_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class ULCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        
    def set_images(self):
        ul_palisade = pygame.image.load("art/structures/walls/ul_palisade_corner.png").convert()
        ul_palisade.set_colorkey(utilities.colors.key)

        self.sprite.image = ul_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class URCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()

    def set_images(self):
        ur_palisade = pygame.image.load("art/structures/walls/ur_palisade_corner.png").convert()
        ur_palisade.set_colorkey(utilities.colors.key)

        self.sprite.image = ur_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class LLCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()

    def set_images(self):
        ll_palisade = pygame.image.load("art/structures/walls/ll_palisade_corner.png").convert()
        ll_palisade.set_colorkey(utilities.colors.key)

        self.sprite.image = ll_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class LRCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()


    def set_images(self):
        lr_palisade = pygame.image.load("art/structures/walls/lr_palisade_corner.png").convert()
        lr_palisade.set_colorkey(utilities.colors.key)
        self.sprite.image = lr_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class Chest(Structure):
    interactable = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "Chest"
        self.items_list = []
        for x in range(10):
            gold_bar = item.Item(item.treasures[0][0], item.treasures[0][1], item.treasures[0][2])
            self.items_list.append(gold_bar)

    def set_images(self):
        chest_image = pygame.image.load("art/structures/chest.png").convert()
        chest_open_image = pygame.image.load("art/structures/chest_open.png").convert()
        chest_image.set_colorkey(utilities.colors.key)
        chest_open_image.set_colorkey(utilities.colors.key)
        self.open_image = chest_open_image
        self.sprite.image = chest_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20

    def use(self, global_variables):
        new_loot_window = ui.LootMenu(global_variables, (0, 0), self)
        new_loot_window.menu_onscreen()
        self.activated = False


class Door(Structure):
    interactable = True
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map, twin_map, x2, y2):
        super().__init__(x, y, current_map)
        self.set_images()

        self.display_name = "Door"
        self.twin_map = twin_map
        self.destination_x = x2
        self.destination_y = y2

    def set_images(self):
        door_image = pygame.image.load("art/structures/door.png").convert()
        door_image.set_colorkey(utilities.colors.key)
        self.sprite.image = door_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def use(self, global_variables):
        global_variables.active_map = self.twin_map
        global_variables.player.tile_x = self.destination_x
        global_variables.player.tile_y = self.destination_y
        global_variables.player.leave_tile()
        global_variables.player.assign_map(global_variables.active_map)
        global_variables.player.assign_tile()
        global_variables.screen.fill(utilities.colors.black)
        global_variables.player.sprite.rect.x = global_variables.player.tile_x * 20
        global_variables.player.sprite.rect.y = (global_variables.player.tile_y - 1) * 20

        self.activated = False
        


class House(Structure):
    interactable = False
    footprint = (4, 3)
    height = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        
        self.display_name = "House"

    def set_images(self):
        house_image_1 = pygame.image.load("art/structures/houses/house_1.png").convert()
        house_image_2 = pygame.image.load("art/structures/houses/house_2.png").convert()
        house_image_3 = pygame.image.load("art/structures/houses/house_3.png").convert()
        house_image_4 = pygame.image.load("art/structures/houses/house_4.png").convert()
        house_image_5 = pygame.image.load("art/structures/houses/house_5.png").convert()
        house_image_1.set_colorkey(utilities.colors.key)
        house_image_2.set_colorkey(utilities.colors.key)
        house_image_3.set_colorkey(utilities.colors.key)
        house_image_4.set_colorkey(utilities.colors.key)
        house_image_5.set_colorkey(utilities.colors.key)
        house_images = [house_image_1, house_image_2, house_image_3, house_image_4, house_image_5]
        self.sprite.image = random.choice(house_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

class SmallHouse(Structure):
    interactable = False
    footprint = (4, 3)
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        
        self.display_name = "House"

    def set_images(self):
        small_house_image = pygame.image.load("art/structures/houses/small_house_1.png").convert()
        small_house_image.set_colorkey(utilities.colors.key)
        self.sprite.image = small_house_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

class LargeHouse(Structure):
    interactable = False
    footprint = (6, 3)
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        
        self.display_name = "House"

    def set_images(self):
        large_house_image = pygame.image.load("art/structures/houses/large_house_1.png").convert()
        large_house_image.set_colorkey(utilities.colors.key)
        self.sprite.image = large_house_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class Hut(Structure):
    interactable = False
    footprint = (3, 2)
    height = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        
        self.display_name = "Hut"

    def set_images(self):
        hut_image = pygame.image.load("art/structures/houses/hut_1.png")
        hut_image.set_colorkey(utilities.colors.key)
        self.sprite.image = hut_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


