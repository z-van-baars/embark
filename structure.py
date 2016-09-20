import entity
import pygame
import ui
import art
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

        self.sprite.image = art.stone_wall_image
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

        self.sprite.image = art.house_interior_wall
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
        self.sprite.image = random.choice(art.vertical_palisade_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class HorizontalPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()

    def set_images(self):
        self.sprite.image = random.choice(art.horizontal_palisade_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class ULCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()

    def set_images(self):

        self.sprite.image = art.ul_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class URCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()

    def set_images(self):
        self.sprite.image = art.ur_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class LLCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()

    def set_images(self):

        self.sprite.image = art.ll_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class LRCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()

    def set_images(self):
        self.sprite.image = art.lr_palisade
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


class Signpost(Structure):
    interactable = True
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.display_name = "Signpost"
        self.set_images()
        self.dialogue_pages = [["Line 1",
                                "Line 2",
                                "Line 3"]]

    def set_images(self):
        self.sprite.image = art.signpost_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def use(self, game_state):
        new_signpost_menu = ui.SignpostMenu(game_state, (0, 0), self)
        new_signpost_menu.menu_onscreen()
        self.activated = False


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

        self.open_image = art.chest_open_image
        self.sprite.image = art.chest_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20

    def use(self, game_state):
        new_loot_window = ui.LootMenu(game_state, (0, 0), self)
        new_loot_window.menu_onscreen()
        self.activated = False


class Forge(Structure):
    interactable = False
    occupies_tile = True
    footprint = (2, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "Forge"

    def set_images(self):
        self.sprite.image = art.forge_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class Anvil(Structure):
    interactable = False
    occupies_tile = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "Anvil"

    def set_images(self):

        self.sprite.image = art.anvil_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20


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
        self.sprite.image = art.door_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def use(self, game_state):
        game_state.active_map.healthbars.remove(game_state.player.healthbar)
        game_state.active_map = self.twin_map
        game_state.active_map.healthbars.append(game_state.player.healthbar)
        game_state.player.tile_x = self.destination_x
        game_state.player.tile_y = self.destination_y
        game_state.player.leave_tile()
        game_state.player.assign_map(game_state.active_map)
        game_state.player.assign_tile()
        game_state.screen.fill(utilities.colors.black)
        game_state.player.sprite.rect.x = game_state.player.tile_x * 20
        game_state.player.sprite.rect.y = (game_state.player.tile_y - 1) * 20

        self.activated = False


class VertGate(Door):
    footprint = (1, 2)

    def __init__(self, x, y, current_map, twin_map, x2, y2):
        super().__init__(x, y, current_map, twin_map, x2, y2)
        self.display_name = "Vertical Gate"

    def set_images(self):
        self.sprite.image = art.vert_door_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class HorizGate(Door):
    footprint = (2, 1)

    def __init__(self, x, y, current_map, twin_map, x2, y2):
        super().__init__(x, y, current_map, twin_map, x2, y2)
        self.display_name = "Horizontal Gate"

    def set_images(self):
        self.sprite.image = art.horiz_gate_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class House(Structure):
    interactable = False
    footprint = (4, 3)
    height = 3

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "House"

    def set_images(self):
        self.sprite.image = random.choice(art.house_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class SmallThatchHouse(Structure):
    interactable = False
    footprint = (4, 3)
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "House"

    def set_images(self):
        self.sprite.image = random.choice(art.small_thatch_house_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class SmallShingleHouse(Structure):
    interactable = False
    footprint = (4, 3)
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "House"

    def set_images(self):
        self.sprite.image = random.choice(art.small_shingle_house_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class MediumThatchHouse(Structure):
    interactable = False
    footprint = (6, 3)
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "House"

    def set_images(self):
        self.sprite.image = random.choice(art.medium_thatch_house_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class MediumShingleHouse(Structure):
    interactable = False
    footprint = (6, 3)
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "House"

    def set_images(self):
        self.sprite.image = random.choice(art.medium_shingle_house_images)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


class LargeShingleHouse(Structure):
    interactable = False
    footprint = (6, 3)
    height = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.set_images()
        self.display_name = "House"

    def set_images(self):
        self.sprite.image = art.large_shingle_house_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20


