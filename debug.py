import pygame
import utilities
import creature
import flora
import structure
import npc

entity_types = {
                "Guard": [npc.Guard],
                "Npc": [npc.Npc],
                "Wheat": [flora.Wheat],
                "Tree": [flora.Wheat],
                "Buffalo": [creature.Buffalo],
                "Wall": [structure.Wall]
                }

entity_strings = ["Guard", "Npc", "Wheat", "Buffalo", "Tree", "Wall"]


class TileSelectorGraphic(pygame.sprite.Sprite):
    def __init__(self, x, y, current_map):
        super().__init__()
        self.tile_x = x
        self.tile_y = y
        self.current_map = current_map

        self.update_image((0, 0))

    def update_image(self, mouse_pos):
        self.tile_x = int(mouse_pos[0] + self.current_map.x_shift) / 20
        self.tile_y = int(mouse_pos[1] + self.current_map.y_shift) / 20
        self.image = pygame.Rect((int(mouse_pos[0] / 20) * 20), (int(mouse_pos[1] / 20) * 20), 20, 20)


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


def event_processing(current_map, debug_status, event_key):
    if event_key == pygame.K_c:
        if debug_status.remove:
            debug_status.remove = False
        debug_status.clear = not debug_status.clear
    elif event_key == pygame.K_r:
        if debug_status.clear:
            debug_status.clear = False
        debug_status.remove = not debug_status.remove

    elif event_key == pygame.K_s:
        debug_status.draw_search_areas = not debug_status.draw_paths
    elif event_key == pygame.K_p:
        debug_status.draw_paths = not debug_status.draw_paths


def mouse_processing(current_map, debug_status, mouse_pos, event):
    tile_x = int((mouse_pos[0] + current_map.x_shift) / 20)
    tile_y = int((mouse_pos[1] + current_map.y_shift) / 20)
    if utilities.within_map(tile_x, tile_y, current_map):
        selected_tile = current_map.game_tile_rows[tile_y][tile_x]
        if debug_status.entity_type != 0:
            entity_types[entity_strings[debug_status.entity_type]](selected_tile.column, selected_tile.row, current_map)
        if debug_status.remove:
            remove_entity_at_tile(current_map, selected_tile, entity_strings[debug_status.entity_type])


def clear_entity_type(current_map, entity_type):
    for row in current_map.game_tile_rows:
        for tile in row:
            tile.entity_group[entity_type] = []
    current_map.entity_group[entity_type] = []


def remove_entity_at_tile(current_map, current_tile, entity_type):
    for each in current_tile.entity_group[entity_type]:
        current_tile.entity_group[entity_type].remove(each)
    current_map.entity_group[entity_type].remove(each)


class DebugStatus(object):
    def __init__(self, current_map, global_variables):
        self.font = pygame.font.SysFont('Calibri', 18, True, False)
        self.current_map = current_map
        self.global_variables = global_variables
        self.debug = False
        self.clear = False
        self.remove = False
        self.entity_type = 0
        self.draw_search_areas = False
        self.draw_paths = False
        self.path_stamp = self.font.render("Drawing Paths", True, utilities.colors.black)
        debug_mode_stamp = self.font.render("Debug Mode", True, utilities.colors.black)
        entity_type_stamp = self.font.render("Placing Item: ", True, utilities.colors.black)
        clear_stamp = self.font.render("Clear Items: All [E]ntities / All [A]nimals / All [V]egetation / All [T]errain", True, utilities.colors.black)
        removal_stamp = self.font.render("Click to remove from tile at cursor: ", True, utilities.colors.black)
        removal_types_stamp = self.font.render("[A]Creatures / [F]lora / [N]PCs / [E]ntities", True, utilities.colors.black)
        self.stamps = [
                        ((210, self.global_variables.screen_height - 70), debug_mode_stamp),
                        ((210, self.global_variables.screen_height - 55), entity_type_stamp),
                        ((210, self.global_variables.screen_height - 55), clear_stamp),
                        ((210, self.global_variables.screen_height - 55), removal_stamp),
                        ((480, self.global_variables.screen_height - 55), removal_types_stamp)
                    ]
        self.update_entity_stamp()

    def update_entity_stamp(self):
        self.entity_stamp = self.font.render(entity_strings[self.entity_type], True, utilities.colors.black)

    def print_to_screen(self, screen):
        screen.blit(self.stamps[0][1], self.stamps[0][0])
        if self.clear:
            screen.blit(self.stamps[2][1], self.stamps[2][0])
        if self.entity_type != 0:
            self.update_entity_stamp()
            screen.blit(self.stamps[1][1], self.stamps[1][0])
            screen.blit(self.entity_stamp, [315, self.global_variables.screen_height - 55])
        if self.remove:
            screen.blit(self.stamps[3][1], self.stamps[3][0])
        if self.global_variables.debug_status.draw_search_areas:
            for each in self.current_map.entity_group["Creature"]:
                new_search_area_graphic = FoodSearchRadius(self.current_map, each)
                new_search_area_graphic.update_stats()
                pygame.draw.circle(screen, (0, 0, 0), new_search_area_graphic.center, new_search_area_graphic.radius, 1)
        if self.global_variables.debug_status.draw_paths:
            screen.blit(self.path_stamp, [210, self.global_variables.screen_height - 40])
            for each in self.current_map.entity_group["Creature"]:
                if each.path:
                    for tile in each.path.tiles:
                        marker = TileMarker(tile.column, tile.row, self.current_map)
                        marker.update_image()
                        pygame.draw.rect(screen, (255, 0, 255), marker.image, 1)



