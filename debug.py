import pygame
import utilities
import creature
import flora
import structure
import npc
import art
import ui

tile_strings = ["Dirt",
                "Flagstone",
                "Wood 1",
                "Wood 2",
                "Wood 3",
                "Grass 1",
                "Grass 2",
                "Grass 3",
                "Grass 4",
                "Grass 5",
                "Marble 1",
                "Stone Block",
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
                "Water"]

entities = {"Forge": structure.Forge,
            "Anvil": structure.Anvil,
            "Wall Stone": structure.StoneWall,
            "Wall Interior": structure.HouseInteriorWall,
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
            "Signpost": structure.Signpost,
            "Chest": structure.Chest,
            "Guard": npc.Guard,
            "Villager": npc.Villager,
            "Merchant": npc.Merchant,
            "Wheat": flora.Wheat,
            "Tree": flora.Tree,
            "Skeleton": creature.Skeleton,
            "Grievebeast": creature.GrieveBeast,
            "Shadebrute": creature.ShadeBrute}

entity_groups = ["Structures",
                 "NPCs",
                 "Creatures",
                 "Flora"]

structure_strings = ["Forge",
                     "Anvil",
                     "Wall Stone",
                     "Wall Interior",
                     "Palisade Horizontal",
                     "Palisade Vertical",
                     "Palisade Corner UL",
                     "Palisade Corner UR",
                     "Palisade Corner LL",
                     "Palisade Corner LR",
                     "Gate Vertical",
                     "Gate Horizontal",
                     "House Thatch Small",
                     "House Thatch Medium",
                     "House Shingle Small",
                     "House Shingle Medium",
                     "House Shingle Large",
                     "Signpost",
                     "Chest"]

creature_strings = ["Skeleton",
                    "Grievebeast",
                    "Shadebrute"]

npc_strings = ["Guard",
               "Villager",
               "Merchant"]


flora_strings = ["Wheat",
                 "Tree"]

string_lists = {"Flora": flora_strings, "NPCs": npc_strings, "Creatures": creature_strings, "Structures": structure_strings}
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
                 pygame.K_COMMA: comma_key,
                 pygame.K_PERIOD: period_key}


def key_event_processing(debug_status, event_key):
    key_functions.get(event_key, do_nothing)(debug_status)


def place_click(debug_status, current_map, selected_tile):
    entity_string = string_lists[debug_status.current_entity_group][debug_status.current_entity_type_number]
    entity_to_place = entities[entity_string]
    if not utilities.any_tile_blocked(selected_tile, current_map, entity_to_place):
        entity_to_place(selected_tile.column, selected_tile.row, current_map)
    else:
        print("BLOCKED!")


def edit_click(game_state, debug_status, selected_tile, mouse_pos):
    if selected_tile.entity_group["Npc"]:
        new_dialogue_edit_menu = ui.DialogueEditor(game_state,
                                                   mouse_pos,
                                                   selected_tile.entity_group["Npc"][0])
        new_dialogue_edit_menu.menu_onscreen()
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


def remove_click(current_map, current_tile):
    for entity_type in current_tile.entity_group:
        for entity in current_tile.entity_group[entity_type]:
            entity.expire()


def paint_click(current_map, current_tile, tile_string):
    current_map.background.image.blit(art.tile_images[tile_string], [current_tile.column * 20,
                                                                     current_tile.row * 20])


def mouse_processing(current_map, debug_status, mouse_pos, event, game_state):
    tile_x = int((mouse_pos[0] - current_map.x_shift) / 20)
    tile_y = int((mouse_pos[1] - current_map.y_shift) / 20)

    if utilities.within_map(tile_x, tile_y, current_map):
        selected_tile = current_map.game_tile_rows[tile_y][tile_x]
        if debug_status.remove:
            remove_click(current_map, selected_tile)
        if debug_status.place:
            place_click(debug_status, current_map, selected_tile)
        if debug_status.edit:
            edit_click(game_state, debug_status, selected_tile, mouse_pos)
        if debug_status.paint:
            paint_click(current_map, selected_tile, tile_strings[debug_status.tile_number])


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

        self.tile_number = 0
        self.current_entity_group_number = 0
        self.current_entity_type_number = 0
        self.current_entity_group = entity_groups[self.current_entity_type_number]

        self.draw_search_areas = False
        self.draw_paths = False
        self.reset_surfaces()

    def reset_surfaces(self):
        self.font = pygame.font.SysFont('Calibri', 18, True, False)
        self.path_stamp = self.font.render("Drawing Paths", True, utilities.colors.black)
        debug_mode_stamp = self.font.render("Debug Mode", True, utilities.colors.black)
        clear_stamp = self.font.render("Clear Items: All [E]ntities / All [A]nimals / All [V]egetation / All [T]errain", True, utilities.colors.black)
        removal_stamp = self.font.render("Click to remove from tile at cursor: ", True, utilities.colors.black)
        place_stamp = self.font.render("Click to place items at cursor", True, utilities.colors.black)
        paint_stamp = self.font.render("Click to paint background terrain", True, utilities.colors.black)
        self.stamps = [((210, self.game_state.screen_height - 70), debug_mode_stamp),
                       ((210, self.game_state.screen_height - 55), place_stamp),
                       ((210, self.game_state.screen_height - 55), clear_stamp),
                       ((210, self.game_state.screen_height - 55), removal_stamp),
                       ((210, self.game_state.screen_height - 55), paint_stamp)]
        self.update_entity_group_stamp()
        self.update_entity_stamp()

    def update_entity_group_stamp(self):
        self.entity_group_stamp = self.font.render(self.current_entity_group, True, utilities.colors.black)

    def update_entity_stamp(self):
        self.entity_stamp = self.font.render(string_lists[self.current_entity_group][self.current_entity_type_number], True, utilities.colors.black)

    def print_to_screen(self, screen):
        screen.blit(self.stamps[0][1], self.stamps[0][0])
        if self.clear:
            screen.blit(self.stamps[2][1], self.stamps[2][0])
        if self.place:
            self.update_entity_stamp()
            screen.blit(self.stamps[1][1], self.stamps[1][0])
            screen.blit(self.entity_group_stamp, [210, self.game_state.screen_height - 40])
            screen.blit(self.entity_stamp, [210, self.game_state.screen_height - 25])
        if self.remove:
            screen.blit(self.stamps[3][1], self.stamps[3][0])
        if self.edit:
            screen.blit(self.font.render("Editing", True, utilities.colors.black), [210, self.game_state.screen_height - 55])
        if self.paint:
            screen.blit(self.stamps[4][1], self.stamps[4][0])
            screen.blit(self.font.render(tile_strings[self.tile_number], True, utilities.colors.black), [210, self.game_state.screen_height - 40])
        if self.draw_search_areas:
            for each in self.current_map.entity_group["Creature"]:
                new_search_area_graphic = FoodSearchRadius(self.current_map, each)
                new_search_area_graphic.update_stats()
                pygame.draw.circle(screen, (0, 0, 0), new_search_area_graphic.center, new_search_area_graphic.radius, 1)
        if self.draw_paths:
            screen.blit(self.path_stamp, [210, self.game_state.screen_height - 40])
            for each in self.current_map.entity_group["Creature"]:
                if each.path:
                    for tile in each.path.tiles:
                        marker = TileMarker(tile.column, tile.row, self.current_map)
                        marker.update_image()
                        pygame.draw.rect(screen, (255, 0, 255), marker.image, 1)
