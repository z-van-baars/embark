import pygame
import utilities
from utilities import GlobalVariables
from game_map import Map
import debug
import inventory

pygame.init()
pygame.display.set_mode([0, 0])

lower_left = pygame.image.load("art/ui_elements/lower_left.png").convert()
bag_icon = pygame.image.load("art/ui_elements/bag.png").convert()
bag_icon_selected = pygame.image.load("art/ui_elements/bag_highlight.png").convert()


def set_bottom_pane_stamp(current_map, mouse_pos):
    font = pygame.font.SysFont('Calibri', 18, True, False)
    tile_x = int((mouse_pos[0] - current_map.x_shift) / 20)
    tile_y = int((mouse_pos[1] - current_map.y_shift) / 20)
    

    if utilities.within_map(tile_x, tile_y, current_map):
        selected_tile = current_map.game_tile_rows[tile_y][tile_x]
        if selected_tile.is_occupied():
            for entity_type in selected_tile.entity_group:
                if selected_tile.entity_group[entity_type]:
                    if selected_tile.entity_group[entity_type][0].occupies_tile:
                        entity = selected_tile.entity_group[entity_type][0]
                        stamp = font.render(entity.display_name, True, utilities.colors.black)
            return stamp
    else:
        return None


def main(global_variables, map_dimensions):
    new_map = Map(map_dimensions)
    new_map.map_generation()
    done = False
    super_scroll = 1
    debug_stats = debug.DebugStatus(new_map, global_variables)
    debug_stats.tile_selector_graphic = debug.TileSelectorGraphic(0, 0, new_map)
    global_variables.debug_status = debug_stats
    bottom_pane = pygame.sprite.Sprite()
    bottom_pane.image = pygame.Surface([global_variables.screen_width - 280, 80])
    bottom_pane.image.fill((171, 171, 171))
    control_on = False
    bag = inventory.Inventory(global_variables.screen_width, global_variables.screen_height)
    while not done:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_map.world_scroll(0, (20 * super_scroll), global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_DOWN:
                    new_map.world_scroll(0, (-20 * super_scroll), global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_LEFT:
                    new_map.world_scroll((20 * super_scroll), 0, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_RIGHT:
                    new_map.world_scroll((-20 * super_scroll), 0, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_LSHIFT:
                    super_scroll = 10
                elif event.key == pygame.K_LCTRL:
                    control_on = True

                elif event.key == pygame.K_SPACE:
                    paused = True
                    while paused:
                        for new_event in pygame.event.get():
                            if new_event.type == pygame.QUIT:
                                paused = False
                                done = True
                            elif new_event.type == pygame.KEYDOWN:
                                if new_event.key == pygame.K_SPACE:
                                    paused = False
                elif event.key == pygame.K_d and control_on:
                    if not debug_stats.debug:
                        debug_stats.debug = True
                    else:
                        debug_stats.debug = False
                        debug_stats.entity_to_place = None
                        debug_stats.current_placement_entity_number = 0
                        debug_stats.clear = False
                        debug_stats.remove = False
                        debug_stats.current_removal_entity_number = 0

                if debug_stats.debug:
                    debug.event_processing(new_map, global_variables.debug_status, event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if debug_stats.debug:
                    debug.mouse_processing(new_map, global_variables.debug_status, mouse_pos, event)
                else:
                    if mouse_pos[0] > global_variables.screen_width - 80 and mouse_pos[1] > global_variables.screen_height - 80:
                        bag.open = True
                    else:
                        new_map.entity_group["Avatar"][0].assign_target(new_map, mouse_pos)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    super_scroll = 1
                elif event.key == pygame.K_LCTRL:
                    control_on = False

        bottom_pane_stamp = set_bottom_pane_stamp(new_map, mouse_pos)

        for tile in new_map.display_tiles:
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, tile.rect.x, tile.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(tile.image, [(tile.rect.x + new_map.x_shift), (tile.rect.y + new_map.y_shift)])
        for structure in new_map.entity_group["Structure"]:
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, structure.sprite.rect.x, structure.sprite.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(structure.sprite.image, [(structure.sprite.rect.x + new_map.x_shift), (structure.sprite.rect.y + new_map.y_shift)])
        for flora in new_map.entity_group["Flora"]:
            flora.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, flora.sprite.rect.x, flora.sprite.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(
                    flora.sprite.image,
                    [(flora.sprite.rect.x + new_map.x_shift),
                        (flora.sprite.rect.y + new_map.y_shift)])

        for creature in new_map.entity_group["Creature"]:
            creature.tick_cycle()
            if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, creature.sprite.rect.x, creature.sprite.rect.y, new_map.x_shift, new_map.y_shift):
                global_variables.screen.blit(creature.sprite.image, [(creature.sprite.rect.x + new_map.x_shift), (creature.sprite.rect.y + new_map.y_shift)])

        for npc in new_map.entity_group["Npc"]:
            npc.tick_cycle()
            global_variables.screen.blit(npc.sprite.image, [(npc.sprite.rect.x + new_map.x_shift), (npc.sprite.rect.y + new_map.y_shift)])

        for avatar in new_map.entity_group["Avatar"]:
            avatar.tick_cycle()
            global_variables.screen.blit(avatar.sprite.image, [(avatar.sprite.rect.x + new_map.x_shift), (avatar.sprite.rect.y + new_map.y_shift)])

        global_variables.screen.blit(lower_left, [0, global_variables.screen_height - 80])
        global_variables.screen.blit(bottom_pane.image, [200, global_variables.screen_height - 79])

        if mouse_pos[0] > global_variables.screen_width - 80 and mouse_pos[1] > global_variables.screen_height - 80:
            bag_image = bag_icon_selected
        else:
            bag_image = bag_icon
        global_variables.screen.blit(bag_image, [global_variables.screen_width - 80, global_variables.screen_height - 80])

        if bottom_pane_stamp and not debug_stats.debug:
            global_variables.screen.blit(bottom_pane_stamp, [210, global_variables.screen_height - 60])

        if debug_stats.debug:
            for each in new_map.entity_group["Creature"]:
                each.search_area_graphic = debug.FoodSearchRadius(new_map, each)
            debug_stats.tile_selector_graphic.update_image(mouse_pos)
            debug_stats.print_to_screen(global_variables.screen)
            pygame.draw.rect(global_variables.screen, (255, 255, 255), debug_stats.tile_selector_graphic.image, 1)
        if bag.open:
            done = bag.draw_to_screen(global_variables.screen, [global_variables.screen_width, global_variables.screen_height])
        pygame.display.flip()
        global_variables.clock.tick(60)
        global_variables.time += 1

global_variables = GlobalVariables(1000, 900 + 80, 20)

world_dimensions = (60, 60)

main(global_variables, world_dimensions)

