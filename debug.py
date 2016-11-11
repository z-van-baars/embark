import pygame
import utilities
import creature
import flora
import structure
import container
import npc
import art
import ui
import avatar

tile_strings = ["Dirt",
                "Flagstone",
                "Flagstone 2",
                "Wood 1",
                "Wood 1 Large",
                "Wood 2",
                "Wood 3",
                "Brown Cobblestones",
                "Grass 1",
                "Grass 2",
                "Grass 3",
                "Grass 4",
                "Grass 5",
                "Marble 1",
                "Stone Block",
                "Stone Block 2",
                "Stone Floor Grey",
                "Stone Floor Brown",
                "Dirt Path T UP",
                "Dirt Path T Down",
                "Dirt Path T Left",
                "Dirt Path T Right",
                "Dirt Path 4 Way",
                "Dirt Path Horizontal",
                "Dirt Path Vertical",
                "Dirt Path Elbow LD",
                "Dirt Path Elbow LU",
                "Dirt Path Elbow RD",
                "Dirt Path Elbow RU",
                "Water 1",
                "Water 2",
                "Water 3"]

entities = {"Avatar": avatar.Avatar,
            "Forge": structure.Forge,
            "Anvil": structure.Anvil,
            "Door": structure.Door,
            "Wall Stone": structure.StoneWall,
            "Wall Interior": structure.HouseInteriorWall,
            "Wall Interior Wide": structure.HouseInteriorWallWide,
            "Wall Interior Tall": structure.HouseInteriorWallTall,
            "Wall Topper": structure.WallTopBottom,
            "Wall Topper 2x2": structure.WallTopLarge,
            "Wall Topper 1x2": structure.WallTopTall,
            "Wall Topper 1x1": structure.WallTopFull,
            "Wall Topper Right": structure.WallTopRight,
            "Wall Topper Left": structure.WallTopLeft,
            "Stone Wall": structure.StoneWall,
            "Stone Wall Tall": structure.StoneWallTall,
            "Stone Wall Chains": structure.StoneWallChains,
            "Stone Wall Torch": structure.StoneWallTorch,
            "Palisade Vertical": structure.VerticalPalisade,
            "Palisade Horizontal": structure.HorizontalPalisade,
            "Palisade Corner LL": structure.LLCornerPalisade,
            "Palisade Corner LR": structure.LRCornerPalisade,
            "Palisade Corner UL": structure.ULCornerPalisade,
            "Palisade Corner UR": structure.URCornerPalisade,
            "Gate Vertical": structure.VertGate,
            "Gate Horizontal": structure.HorizGate,
            "House Thatch Small": structure.SmallThatchHouse,
            "House Thatch Medium": structure.MediumThatchHouse,
            "House Shingle Small": structure.SmallShingleHouse,
            "House Shingle Medium": structure.MediumShingleHouse,
            "House Shingle Large": structure.LargeShingleHouse,
            "Stone House Thatch Small": structure.SmallStoneThatchHouse,
            "Stone House Thatch Medium": structure.MediumStoneThatchHouse,
            "Stone House Shingle Small": structure.SmallStoneShingleHouse,
            "Stone House Shingle Medium": structure.MediumStoneShingleHouse,
            "Dungeon Entrance": structure.DungeonEntrance,
            "Stairs Up": structure.StairsUp,
            "Stairs Down": structure.StairsDown,
            "Altar Empty": structure.AltarEmpty,
            "Altar Empty Writing": structure.AltarEmptyWriting,
            "Altar": structure.Altar,
            "Candelabra": structure.Candelabra,
            "Signpost": structure.Signpost,
            "Chest": container.Chest,
            "Quest Chest": container.QuestChest,
            "Pot": structure.Pot,
            "Table Empty": structure.TableEmpty,
            "Table": structure.Table,
            "Barrel Vertical": structure.BarrelVertical,
            "Barrel Horizontal": structure.BarrelHorizontal,
            "Chair Forward": structure.ChairForward,
            "Chair Backward": structure.ChairBackward,
            "Stool Round": structure.StoolRound,
            "Stool Square": structure.StoolSquare,
            "Bookshelf Narrow": structure.NarrowBookshelf,
            "Bookshelf Narrow Empty": structure.EmptyNarrowBookshelf,
            "Bookshelf Wide": structure.WideBookshelf,
            "Bookshelf Wide Empty": structure.EmptyWideBookshelf,
            "Long Table Empty": structure.TableLongEmpty,
            "Long Table": structure.TableLong,
            "Castle Door": structure.CastleDoor,
            "Castle Tower": structure.CastleTower,
            "Castle Wall Short Narrow": structure.CastleWallNarrow,
            "Castle Wall Short Wide": structure.CastleWallWide,
            "Castle Wall Tall Narrow": structure.CastleWallTallNarrow,
            "Castle Wall Tall Wide": structure.CastleWallTallWide,
            "Wood Crate": structure.WoodCrate,
            "Desk Forward": structure.DeskForward,
            "Desk Backward": structure.DeskBackward,
            "Wardrobe Short": structure.WardrobeShort,
            "Wardrobe Narrow": structure.WardrobeNarrowTall,
            "Wardrobe Narrow Short": structure.WardrobeNarrowShort,
            "Bookshelf Wide Short Empty": structure.ShortEmptyWideBookshelf,
            "Bookshelf Narrow Short Empty": structure.ShortEmptyNarrowBookshelf,
            "Wardrobe": structure.Wardrobe,
            "Guard": npc.Guard,
            "Lord": npc.Lord,
            "Quest Lord": npc.QuestLord,
            "Villager": npc.Villager,
            "Sage": npc.Sage,
            "Merchant": npc.Merchant,
            "Wheat": flora.Wheat,
            "Pine Tree": flora.PineTree,
            "Small Oak Tree": flora.SmallOakTree,
            "Small Bare Oak Tree": flora.SmallOakTreeBare,
            "Small Fall Oak Tree": flora.SmallOakTreeFall,
            "Large Oak Tree": flora.LargeOakTree,
            "Large Bare Oak Tree": flora.LargeBareOakTree,
            "Large Bare Oak Tree Dark": flora.LargeBareDarkOakTree,
            "Large Yellow Oak Tree": flora.LargeYellowOakTree,
            "Large Fall Oak Tree": flora.LargeFallOakTree,
            "Skeleton": creature.Skeleton,
            "Grievebeast": creature.GrieveBeast,
            "Doompaw": creature.DoomPaw,
            "Shadebrute": creature.ShadeBrute,
            "Cindermask": creature.CinderMask,
            "Cow": creature.Cow,
            "Wood Fence Vertical": structure.WoodFenceV,
            "Wood Fence Horizontal": structure.WoodFenceH,
            "Wood Fence Left": structure.WoodFenceL,
            "Wood Fence Right": structure.WoodFenceR,
            "Wood Fence Down": structure.WoodFenceD,
            "Wood Fence Up": structure.WoodFenceU,
            "Wood Fence Upper Left": structure.WoodFenceUL,
            "Wood Fence Upper Right": structure.WoodFenceUR,
            "Wood Fence Lower Left": structure.WoodFenceDL,
            "Wood Fence Lower Right": structure.WoodFenceDR,
            "Wood Fence 4 Way": structure.WoodFence4way,
            "Wood Fence Vertical Left": structure.WoodFenceVL,
            "Wood Fence Vertical Right": structure.WoodFenceVR,
            "Wood Fence Horizontal Up": structure.WoodFenceHU,
            "Wood Fence Horizontal Down": structure.WoodFenceHD}

entity_groups = ["Structures",
                 "Furniture",
                 "NPCs",
                 "Creatures",
                 "Flora",
                 "Avatar"]

structure_strings = ["Forge",
                     "Anvil",
                     "Door",
                     "Wall Interior",
                     "Wall Interior Tall",
                     "Wall Interior Wide",
                     "Castle Wall Short Narrow",
                     "Castle Wall Short Wide",
                     "Castle Wall Tall Narrow",
                     "Castle Wall Tall Wide",
                     "Castle Tower",
                     "Castle Door",
                     "Palisade Horizontal",
                     "Palisade Vertical",
                     "Palisade Corner UL",
                     "Palisade Corner UR",
                     "Palisade Corner LL",
                     "Palisade Corner LR",
                     "Stairs Up",
                     "Stairs Down",
                     "Wood Fence Vertical",
                     "Wood Fence Horizontal",
                     "Wood Fence Left",
                     "Wood Fence Right",
                     "Wood Fence Up",
                     "Wood Fence Down",
                     "Wood Fence Upper Left",
                     "Wood Fence Upper Right",
                     "Wood Fence Lower Left",
                     "Wood Fence Lower Right",
                     "Wood Fence 4 Way",
                     "Wood Fence Vertical Left",
                     "Wood Fence Vertical Right",
                     "Wood Fence Horizontal Up",
                     "Wood Fence Horizontal Down",
                     "Gate Vertical",
                     "Gate Horizontal",
                     "House Thatch Small",
                     "House Thatch Medium",
                     "House Shingle Small",
                     "House Shingle Medium",
                     "House Shingle Large",
                     "Stone House Shingle Small",
                     "Stone House Shingle Medium",
                     "Stone House Thatch Small",
                     "Stone House Thatch Medium",
                     "Signpost",
                     "Stone Wall",
                     "Stone Wall Tall",
                     "Stone Wall Chains",
                     "Stone Wall Torch",
                     "Dungeon Entrance",
                     "Wall Topper",
                     "Wall Topper 1x1",
                     "Wall Topper Left",
                     "Wall Topper Right",
                     "Wall Topper 2x2",
                     "Wall Topper 1x2"
                     ]

furniture_strings = ["Table Empty",
                     "Table",
                     "Long Table Empty",
                     "Long Table",
                     "Chair Forward",
                     "Chair Backward",
                     "Stool Round",
                     "Stool Square",
                     "Desk Forward",
                     "Desk Backward",
                     "Wood Crate",
                     "Bookshelf Narrow",
                     "Bookshelf Narrow Empty",
                     "Bookshelf Narrow Short Empty",
                     "Bookshelf Wide",
                     "Bookshelf Wide Empty",
                     "Bookshelf Wide Short Empty",
                     "Wardrobe",
                     "Wardrobe Short",
                     "Wardrobe Narrow",
                     "Wardrobe Narrow Short",
                     "Pot",
                     "Chest",
                     "Quest Chest",
                     "Barrel Vertical",
                     "Barrel Horizontal",
                     "Candelabra",
                     "Altar",
                     "Altar Empty",
                     "Altar Empty Writing"
                     ]

creature_strings = ["Doompaw",
                    "Skeleton",
                    "Grievebeast",
                    "Shadebrute",
                    "Cindermask",
                    "Cow"]

npc_strings = ["Guard",
               "Villager",
               "Lord",
               "Sage",
               "Merchant",
               "Quest Lord"]


flora_strings = ["Wheat",
                 "Pine Tree",
                 "Large Oak Tree",
                 "Large Fall Oak Tree",
                 "Large Yellow Oak Tree",
                 "Large Bare Oak Tree",
                 "Large Bare Oak Tree Dark",
                 "Small Oak Tree",
                 "Small Fall Oak Tree",
                 "Small Bare Oak Tree"]

avatar_strings = ["Avatar"]

string_lists = {"Flora": flora_strings, "NPCs": npc_strings, "Creatures": creature_strings, "Structures": structure_strings, "Furniture": furniture_strings, "Avatar": avatar_strings}
for string_list in string_lists:
    string_lists[string_list] = sorted(string_lists[string_list])


class TileMarker(pygame.sprite.Sprite):
    def __init__(self, x, y, current_map):
        super().__init__()
        self.tile_x = x
        self.tile_y = y
        self.current_map = current_map

        self.update_image()

    def update_image(self):

        top = int(self.tile_y * 20) + self.current_map.y_shift
        left = int(self.tile_x * 20) + self.current_map.x_shift
        self.image = pygame.Rect(left, top, 20, 20)


class FoodSearchRadius(pygame.sprite.Sprite):
    def __init__(self, current_map, entity):
        super().__init__()
        self.current_map = current_map
        self.entity = entity
        self.center = (entity.sprite.rect.x, entity.sprite.rect.y)
        self.radius = (self.entity.sight_range * 20)

        self.update_stats()

    def update_stats(self):
        self.center = (self.entity.sprite.rect.x + 5 + self.current_map.x_shift, self.entity.sprite.rect.y + 5 + self.current_map.y_shift)
        self.radius = (self.entity.sight_range * 20)


def clear_entity_type(current_map, current_entity_type):
    for row in current_map.game_tile_rows:
        for tile in row:
            tile.entity_group[current_entity_type] = []
    current_map.entity_group[current_entity_type] = []


def c_key(debug_status):
    if debug_status.remove:
        debug_status.remove = False
    if debug_status.edit:
        debug_status.edit = False
    if debug_status.place:
        debug_status.place = False
    if debug_status.paint:
        debug_status.paint = False
    debug_status.clear = not debug_status.clear


def r_key(debug_status):
    if debug_status.clear:
        debug_status.clear = False
    if debug_status.edit:
        debug_status.edit = False
    if debug_status.place:
        debug_status.place = False
    if debug_status.paint:
        debug_status.paint = False
    debug_status.remove = not debug_status.remove


def t_key(debug_status):
    if debug_status.clear:
        debug_status.clear = False
    if debug_status.edit:
        debug_status.edit = False
    if debug_status.remove:
        debug_status.remove = False
    if debug_status.paint:
        debug_status.paint = False
    debug_status.place = not debug_status.place


def s_key(debug_status):
    debug_status.draw_search_areas = not debug_status.draw_paths


def p_key(debug_status):
    debug_status.draw_paths = not debug_status.draw_paths


def e_key(debug_status):
    if debug_status.clear:
        debug_status.clear = False
    if debug_status.remove:
        debug_status.remove = False
    if debug_status.place:
        debug_status.place = False
    if debug_status.paint:
        debug_status.paint = False
    debug_status.edit = not debug_status.edit


def f_key(debug_status):
    if debug_status.clear:
        debug_status.clear = False
    if debug_status.remove:
        debug_status.remove = False
    if debug_status.place:
        debug_status.place = False
    if debug_status.edit:
        debug_status.edit = False
    debug_status.paint = not debug_status.paint


def u_key(debug_status):
    if debug_status.paint:
        if debug_status.brush_size[1] < 10:
            debug_status.brush_size = (debug_status.brush_size[0], debug_status.brush_size[1] + 1)


def i_key(debug_status):
    if debug_status.paint:
        if debug_status.brush_size[0] < 10:
            debug_status.brush_size = (debug_status.brush_size[0] + 1, debug_status.brush_size[1])


def j_key(debug_status):
    if debug_status.paint:
        if debug_status.brush_size[1] > 1:
            debug_status.brush_size = (debug_status.brush_size[0], debug_status.brush_size[1] - 1)


def k_key(debug_status):
    if debug_status.paint:
        if debug_status.brush_size[0] > 1:
            debug_status.brush_size = (debug_status.brush_size[0] - 1, debug_status.brush_size[1])


def z_key(debug_status):
    if debug_status.place:
        if not debug_status.current_entity_type_number == 0:
            debug_status.current_entity_type_number -= 1
    if debug_status.paint:
        if not debug_status.tile_number == 0:
            debug_status.tile_number -= 1


def x_key(debug_status):
    if debug_status.place:
        if not debug_status.current_entity_type_number == (len(string_lists[debug_status.current_entity_group]) - 1):
            debug_status.current_entity_type_number += 1
    if debug_status.paint:
        if not debug_status.tile_number == (len(tile_strings) - 1):
            debug_status.tile_number += 1


def comma_key(debug_status):
    if not debug_status.current_entity_group_number == 0:
        debug_status.current_entity_group_number -= 1
        debug_status.current_entity_type_number = 0
        debug_status.current_entity_group = entity_groups[debug_status.current_entity_group_number]
        debug_status.update_entity_group_stamp()


def period_key(debug_status):
    if not debug_status.current_entity_group_number == (len(entity_groups) - 1):
        debug_status.current_entity_group_number += 1
        debug_status.current_entity_type_number = 0
        debug_status.current_entity_group = entity_groups[debug_status.current_entity_group_number]
        debug_status.update_entity_group_stamp()


def do_nothing(debug_status):
    pass


key_functions = {pygame.K_c: c_key,
                 pygame.K_r: r_key,
                 pygame.K_t: t_key,
                 pygame.K_s: s_key,
                 pygame.K_p: p_key,
                 pygame.K_e: e_key,
                 pygame.K_z: z_key,
                 pygame.K_x: x_key,
                 pygame.K_f: f_key,
                 pygame.K_u: u_key,
                 pygame.K_i: i_key,
                 pygame.K_j: j_key,
                 pygame.K_k: k_key,
                 pygame.K_COMMA: comma_key,
                 pygame.K_PERIOD: period_key}


def key_event_processing(debug_status, event_key):
    key_functions.get(event_key, do_nothing)(debug_status)


def place_click(game_state, debug_status, current_map, selected_tile):
    entity_string = string_lists[debug_status.current_entity_group][debug_status.current_entity_type_number]
    entity_to_place = entities[entity_string]
    if not entity_to_place.gateway:
        if not utilities.any_tile_blocked(selected_tile, current_map, entity_to_place):
            if entity_to_place.my_type == "Avatar":
                game_state.player.tile_x = selected_tile.column
                game_state.player.tile_y = selected_tile.row
                #game_state.player.leave_tile()
                game_state.player.assign_map(current_map)
                game_state.player.assign_tile()
                game_state.player.set_images(game_state.player.image_key)
                game_state.player.set_frame(game_state.player.action)
                game_state.player.sprite.rect.x = game_state.player.tile_x * 20
                game_state.player.sprite.rect.y = (game_state.player.tile_y - 1) * 20
                for category in game_state.player.items:
                    for each_item in game_state.player.items[category]:
                        each_item.set_surfaces()
            else:
                entity_to_place(selected_tile.column, selected_tile.row, current_map)
        else:
            print("BLOCKED!")
    else:
        entity_to_place(selected_tile.column, selected_tile.row, current_map)
    current_map.update_object_layer()


def edit_click(game_state, debug_status, selected_tile, mouse_pos):
    if selected_tile.entity_group["Npc"]:
        new_npc_edit_menu = ui.NpcEditor(game_state,
                                         mouse_pos,
                                         selected_tile.entity_group["Npc"][0])
        new_npc_edit_menu.menu_onscreen()
    if selected_tile.entity_group["Structure"]:
        for each in selected_tile.entity_group["Structure"]:
            if each.display_name == "Signpost":
                new_dialogue_edit_menu = ui.SignpostEditor(game_state,
                                                           mouse_pos,
                                                           selected_tile.entity_group["Structure"][0])
                new_dialogue_edit_menu.menu_onscreen()
            if each.display_name == "Chest":
                new_chest_edit_menu = ui.ChestEditMenu(game_state,
                                                       mouse_pos,
                                                       selected_tile.entity_group["Structure"][0])
                new_chest_edit_menu.menu_onscreen()
            if each.gateway:
                door_edit_menu = ui.DoorEditMenu(game_state,
                                                 mouse_pos,
                                                 each)
                door_edit_menu.menu_onscreen()


def remove_click(current_map, current_tile):
    for entity_type in current_tile.entity_group:
        for entity in current_tile.entity_group[entity_type]:
            entity.expire(1, False)
    current_map.update_object_layer()


def paint_click(current_map, current_tile, tile_string, brush_size):
    footprint = brush_size
    initial_x = current_tile.column
    initial_y = current_tile.row - (footprint[1] - 1)
    for tile_y in range(initial_y, initial_y + (footprint[1])):
        for tile_x in range(initial_x, initial_x + footprint[0]):
            current_map.background.image.blit(art.tile_images[tile_string], [tile_x * 20,
                                                                             tile_y * 20])

def mouse_processing(current_map, debug_status, mouse_pos, event, game_state):
    tile_x = int((mouse_pos[0] - current_map.x_shift) / 20)
    tile_y = int((mouse_pos[1] - current_map.y_shift) / 20)

    if utilities.within_map(tile_x, tile_y, current_map):
        selected_tile = current_map.game_tile_rows[tile_y][tile_x]
        if debug_status.remove:
            remove_click(current_map, selected_tile)
        if debug_status.place:
            place_click(game_state, debug_status, current_map, selected_tile)
        if debug_status.edit:
            edit_click(game_state, debug_status, selected_tile, mouse_pos)
        if debug_status.paint:
            paint_click(current_map, selected_tile, tile_strings[debug_status.tile_number], debug_status.brush_size)


class DebugStatus(object):
    def __init__(self, current_map, game_state):
        self.current_map = current_map
        self.game_state = game_state
        self.debug = False
        self.clear = False
        self.place = False
        self.edit = False
        self.remove = False
        self.paint = False

        self.brush_size = (1, 1)
        self.tile_number = 0
        self.current_entity_group_number = 0
        self.current_entity_type_number = 0
        self.current_entity_group = entity_groups[self.current_entity_type_number]

        self.draw_search_areas = False
        self.draw_paths = False
        self.reset_surfaces()

    def reset_surfaces(self):
        self.font = pygame.font.SysFont('Calibri', 18, True, False)
        self.tiny_font = pygame.font.SysFont('Calibri', 12, True, False)
        self.path_stamp = self.tiny_font.render("Drawing Paths", True, utilities.colors.border_gold)
        debug_mode_stamp = self.font.render("Debug Mode", True, utilities.colors.border_gold)
        clear_stamp = self.tiny_font.render("Clear Items: All [E]ntities / All [A]nimals / All [V]egetation / All [T]errain",
                                            True, utilities.colors.border_gold)
        removal_stamp = self.tiny_font.render("Click to remove from tile at cursor: ", True, utilities.colors.border_gold)
        place_stamp = self.tiny_font.render("Click to place items at cursor", True, utilities.colors.border_gold)
        paint_stamp = self.tiny_font.render("Click to paint background terrain", True, utilities.colors.border_gold)
        self.stamps = [((10, self.game_state.screen_height - 70), debug_mode_stamp),
                       ((10, self.game_state.screen_height - 50), place_stamp),
                       ((10, self.game_state.screen_height - 50), clear_stamp),
                       ((10, self.game_state.screen_height - 50), removal_stamp),
                       ((10, self.game_state.screen_height - 50), paint_stamp)]
        self.update_entity_group_stamp()
        self.update_entity_stamp()

    def update_entity_group_stamp(self):
        self.entity_group_stamp = self.tiny_font.render(self.current_entity_group, True, utilities.colors.border_gold)

    def update_entity_stamp(self):
        self.entity_stamp = self.tiny_font.render(string_lists[self.current_entity_group][self.current_entity_type_number],
                                                  True,
                                                  utilities.colors.border_gold)

    def print_to_screen(self, screen):
        screen.blit(self.stamps[0][1], self.stamps[0][0])
        if self.clear:
            screen.blit(self.stamps[2][1], self.stamps[2][0])
        if self.place:
            self.update_entity_stamp()
            screen.blit(self.stamps[1][1], self.stamps[1][0])
            screen.blit(self.entity_group_stamp, [10, self.game_state.screen_height - 40])
            screen.blit(self.entity_stamp, [10, self.game_state.screen_height - 30])
        if self.remove:
            screen.blit(self.stamps[3][1], self.stamps[3][0])
        if self.edit:
            screen.blit(self.font.render("Editing", True, utilities.colors.border_gold), [10, self.game_state.screen_height - 50])
        if self.paint:
            screen.blit(self.stamps[4][1], self.stamps[4][0])
            screen.blit(self.font.render(tile_strings[self.tile_number],
                                         True,
                                         utilities.colors.border_gold),
                        [10, self.game_state.screen_height - 40])
        if self.draw_search_areas:
            for each in self.current_map.entity_group["Creature"]:
                new_search_area_graphic = FoodSearchRadius(self.current_map, each)
                new_search_area_graphic.update_stats()
                pygame.draw.circle(screen, (0, 0, 0), new_search_area_graphic.center, new_search_area_graphic.radius, 1)
        if self.draw_paths:
            screen.blit(self.path_stamp, [10, self.game_state.screen_height - 40])
            for each in self.current_map.entity_group["Creature"]:
                if each.path:
                    for tile in each.path.tiles:
                        marker = TileMarker(tile.column, tile.row, self.current_map)
                        marker.update_image()
                        pygame.draw.rect(screen, (255, 0, 255), marker.image, 1)
