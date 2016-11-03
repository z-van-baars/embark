import entity
import pygame
import ui
import art
import utilities
import random
import weapon

pygame.init()
pygame.display.set_mode([0, 0])


class Structure(entity.StationaryEntity):
    occupies_tile = True
    interactable = False
    my_type = "Structure"

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.activated = False
        self.image_index = None

    def tick_cycle(self):
        pass


class WallTopLeft(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wall Top Left"
        self.set_images(self.image_key)
        self.display_name = ""


class WallTopRight(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wall Top Right"
        self.set_images(self.image_key)
        self.display_name = ""


class WallTopBottom(Structure):
    occupies_tile = False
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wall Top Bottom"
        self.set_images(self.image_key)
        self.display_name = ""


class WallTopFull(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wall Top Full"
        self.set_images(self.image_key)
        self.display_name = ""


class WallTopTall(Structure):
    interactable = False
    footprint = (1, 2)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wall Top Tall"
        self.set_images(self.image_key)
        self.display_name = ""


class WallTopLarge(Structure):
    interactable = False
    footprint = (2, 2)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wall Top Large"
        self.set_images(self.image_key)
        self.display_name = ""


class DungeonEntrance(Structure):
    interactable = False
    footprint = (4, 6)
    height = 7
    width = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Dungeon Entrance"
        self.set_images(self.image_key)
        self.display_name = "Dungeon Entrance"


class SmallThatchHouse(Structure):
    interactable = False
    footprint = (4, 3)
    height = 4
    width = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Small Thatch"
        self.set_images(self.image_key)
        self.display_name = "House"


class SmallShingleHouse(Structure):
    interactable = False
    footprint = (4, 3)
    height = 4
    width = 4

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Small Shingle"
        self.set_images(self.image_key)
        self.display_name = "House"


class MediumThatchHouse(Structure):
    interactable = False
    footprint = (6, 3)
    height = 4
    width = 6

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Medium Thatch"
        self.set_images(self.image_key)
        self.display_name = "House"


class MediumShingleHouse(Structure):
    interactable = False
    footprint = (6, 3)
    height = 4
    width = 6

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Medium Shingle"
        self.set_images(self.image_key)
        self.display_name = "House"


class LargeShingleHouse(Structure):
    interactable = False
    footprint = (6, 3)
    height = 4
    width = 6

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Large Shingle"
        self.set_images(self.image_key)
        self.display_name = "House"


class ChairForward(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Chair Forward"
        self.display_name = "Chair"
        self.set_images(self.image_key)


class ChairBackward(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Chair Backward"
        self.display_name = "Chair"
        self.set_images(self.image_key)


class WoodCrate(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wood Crate"
        self.display_name = "Wood Crate"
        self.set_images(self.image_key)


class Pot(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Pot"
        self.display_name = "Pot"
        self.set_images(self.image_key)


class BarrelVertical(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Barrel Vertical"
        self.display_name = "Barrel"
        self.set_images(self.image_key)


class BarrelHorizontal(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Barrel Horizontal"
        self.display_name = "Barrel"
        self.set_images(self.image_key)


class TableEmpty(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Table Empty"
        self.display_name = "Table"
        self.set_images(self.image_key)


class Table(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = Table
        self.display_name = "Table"
        self.set_images(self.image_key)


class DeskForward(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Desk Forward"
        self.display_name = "Desk"
        self.set_images(self.image_key)


class DeskBackward(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Desk Backward"
        self.display_name = "Desk"
        self.set_images(self.image_key)


class EmptyNarrowBookshelf(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Bookshelf Narrow Empty"
        self.display_name = "Bookshelf"
        self.set_images(self.image_key)


class ShortEmptyNarrowBookshelf(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Bookshelf Short Narrow Empty"
        self.display_name = "Bookshelf"
        self.set_images(self.image_key)


class NarrowBookshelf(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Bookshelf Narrow"
        self.display_name = "Bookshelf"
        self.set_images(self.image_key)


class EmptyWideBookshelf(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Bookshelf Wide Empty"
        self.display_name = "Bookshelf"
        self.set_images(self.image_key)


class ShortEmptyWideBookshelf(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Bookshelf Short Wide Empty"
        self.display_name = "Bookshelf"
        self.set_images(self.image_key)


class WideBookshelf(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Bookshelf Wide"
        self.display_name = "Bookshelf"
        self.set_images(self.image_key)


class Wardrobe(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wardrobe"
        self.display_name = "Wardrobe"
        self.set_images(self.image_key)


class WardrobeNarrowTall(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wardrobe Tall Narrow"
        self.display_name = "Wardrobe"
        self.set_images(self.image_key)


class WardrobeNarrowShort(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wardrobe Short Narrow"
        self.display_name = "Wardrobe"
        self.set_images(self.image_key)


class WardrobeShort(Structure):
    interactable = False
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wardrobe Short"
        self.display_name = "Wardrobe"
        self.set_images(self.image_key)


class HouseInteriorWall(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Interior Wall"
        self.display_name = "Wall"
        self.set_images(self.image_key)


class HouseInteriorWallTall(Structure):
    interactable = False
    footprint = (1, 2)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Interior Wall Tall"
        self.display_name = "Wall"
        self.set_images(self.image_key)


class HouseInteriorWallWide(Structure):
    interactable = False
    footprint = (2, 2)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "House Interior Wall Wide"
        self.display_name = "Wall"
        self.set_images(self.image_key)


class StoneWall(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Stone Wall"
        self.display_name = "Wall"
        self.set_images(self.image_key)

    def set_images(self):
        self.sprite.image = art.stone_wall
        self.set_image_state()


class StoneWallTall(Structure):
    interactable = False
    footprint = (1, 2)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Stone Wall Tall"
        self.display_name = "Wall"
        self.set_images(self.image_key)


class StoneWallChains(Structure):
    interactable = False
    footprint = (1, 2)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Stone Wall Chains"
        self.display_name = "Wall"
        self.set_images(self.image_key)


class StoneWallTorch(Structure):
    interactable = False
    footprint = (1, 2)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Stone Wall Torch"
        self.display_name = "Wall"
        self.set_images(self.image_key)


class Palisade(Structure):
    interactable = False
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Vertical Palisade"
        self.display_name = "Palisade Wall"
        self.set_images(self.image_key)


class WoodFenceH(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence H"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceHU(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence HU"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceHD(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence HD"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceV(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence V"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceVR(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence VR"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceVL(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence R"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceL(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence L"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceR(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence R"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceU(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence U"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceD(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence D"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceUR(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence UR"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceUL(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence UL"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceDR(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence DR"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFenceDL(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence DL"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)


class WoodFence4way(Structure):
    interactable = False
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Wooden Fence 4 Way"
        self.display_name = "Wooden Fence"
        self.set_images(self.image_key)

    def set_images(self):
        self.sprite.image = art.wood_fence_4_way
        self.set_image_state()


class VerticalPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Palisade Vertical"
        self.set_images(self.image_key)


class HorizontalPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Palisade Horizontal"
        self.set_images(self.image_key)


class ULCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "UL Palisade"
        self.set_images(self.image_key)


class URCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "UR Palisade"
        self.set_images(self.image_key)


class LLCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "LL Palisade"
        self.set_images(self.image_key)


class LRCornerPalisade(Palisade):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "LR Palisade"
        self.set_images(self.image_key)


class Forge(Structure):
    interactable = False
    occupies_tile = True
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Forge"
        self.set_images(self.image_key)
        self.display_name = "Forge"


class Anvil(Structure):
    interactable = False
    occupies_tile = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Anvil"
        self.set_images(self.image_key)
        self.display_name = "Anvil"


class Signpost(Structure):
    interactable = True
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.display_name = "Signpost"
        self.image_key = "Signpost"
        self.set_images(self.image_key)
        self.dialogue_pages = [["Line 1",
                                "Line 2",
                                "Line 3"]]

    def use(self, game_state):
        new_signpost_menu = ui.SignpostMenu(game_state, (0, 0), self)
        new_signpost_menu.menu_onscreen()
        self.activated = False


class Container(Structure):
    interactable = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Chest"
        self.set_images(self.image_key)
        self.display_name = "Container"
        self.items_list = []
        self.value = 10
        self.opened = False

    def use(self, game_state):
        if not self.opened:
            self.items_list = []
            self.fill(game_state.player.level)
            self.opened = True
        new_loot_window = ui.LootMenu(game_state, (0, 0), self)
        new_loot_window.menu_onscreen()
        self.activated = False


class Chest(Container):
    interactable = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.image_key = "Chest"
        self.display_name = "Chest"
        self.set_images(self.image_key)

    def fill(self, player_level):
        for x in range(random.randint(2, 10)):
            self.items_list.append(random.choice(weapon.weapon_functions)(self.value, player_level))


class Door(Structure):
    interactable = True
    footprint = (1, 1)
    height = 2
    gateway = True

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map)
        self.image_key = "Door"
        self.set_images(self.image_key)

        self.display_name = "Door"
        self.twin_map = twin_map
        self.destination_x = x2
        self.destination_y = y2

    def use(self, game_state):
        if self.twin_map is not None and self.twin_map in game_state.maps:
            twin_map = game_state.maps[self.twin_map]
            game_state.active_map.healthbars.remove(game_state.player.healthbar)
            game_state.active_map = twin_map
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


class StairsUp(Door):
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.display_name = "Stairs"
        self.image_key = "Stairs Up"
        self.set_images(self.image_key)


class StairsDown(Door):
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.display_name = "Stairs"
        self.image_key = "Stairs Down"
        self.set_images(self.image_key)


class VertGate(Door):
    footprint = (1, 2)
    height = 2

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.image_key = "Vert Gate"
        self.set_images(self.image_key)
        self.display_name = "Vertical Gate"


class HorizGate(Door):
    footprint = (2, 1)
    height = 1
    width = 2

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.image_key = "Horiz Gate"
        self.set_images(self.image_key)
        self.display_name = "Horizontal Gate"


class Altar(Door):
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.display_name = "Altar"
        self.image_key = "Altar"
        self.set_images(self.image_key)


class AltarEmptyWriting(Door):
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.display_name = "Altar"
        self.image_key = "Altar Empty Writing"
        self.set_images(self.image_key)


class AltarEmpty(Door):
    footprint = (2, 1)
    height = 2
    width = 2

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.display_name = "Altar"
        self.image_key = "Altar Empty"


class Candelabra(Door):
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map, x2=0, y2=1, twin_map=None):
        super().__init__(x, y, current_map, x2, y2, twin_map)
        self.display_name = "Candelabra"
        self.image_key = "Candelabra"
        self.set_images

