import pygame
import utilities
from utilities import GlobalVariables
from game_map import Map
import debug
import inventory
import item
import combat
from npc import Guard
from npc import Merchant
import structure
from avatar import Avatar
from creature import Skeleton
from flora import Tree
import ui
import pickle

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


def main(global_variables):
    tiny_font = pygame.font.SysFont('Calibri', 11, True, False)
    map_1 = pickle.load(open("maps/map_1.p", "rb"))
    utilities.restore_surfaces(map_1)
    

    map_2 = Map((50, 20), (global_variables.screen_width, global_variables.screen_height), False)
    map_3 = Map((36, 36), (global_variables.screen_width, global_variables.screen_height), False)
    map_4 = Map((20, 12), (global_variables.screen_width, global_variables.screen_height), False)

    map_2.map_generation()
    map_3.map_generation()
    map_4.map_generation()
    global_variables.maps = [map_1, map_2, map_3, map_4]
    global_variables.active_map = global_variables.maps[0]

    done = False
    super_scroll = 1
    debug_stats = debug.DebugStatus(global_variables.active_map, global_variables)
    debug_stats.tile_selector_graphic = ui.TileSelectorGraphic(0, 0, global_variables.active_map)
    global_variables.debug_status = debug_stats
    bottom_pane = pygame.sprite.Sprite()
    bottom_pane.image = pygame.Surface([global_variables.screen_width - 280, 80])
    bottom_pane.image.fill((171, 171, 171))
    control_on = False

    structure.Door(4, 11, map_4, map_1, 26, 11)

    #Chest(22, 22, map_1)
        
    # Skeleton(25, 25, map_1)

    global_variables.player = global_variables.active_map.entity_group["Avatar"][0]


    global_variables.active_map.entity_group["Avatar"][0].bag = inventory.Inventory(global_variables.screen_width, global_variables.screen_height)
    dagger = item.Item(item.weapons[0][0], item.weapons[0][1], item.weapons[0][2])
    bow = item.Item(item.weapons[2][0], item.weapons[2][1], item.weapons[2][2])
    flaske = item.Item(item.treasures[1][0], item.treasures[1][1], item.treasures[1][2])
    initial_equipment = [dagger, bow, flaske]
    global_variables.active_map.entity_group["Avatar"][0].bag.items_list = initial_equipment

    while not done:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    global_variables.active_map.world_scroll(0, (20 * super_scroll), global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_DOWN:
                    global_variables.active_map.world_scroll(0, (-20 * super_scroll), global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_LEFT:
                    global_variables.active_map.world_scroll((20 * super_scroll), 0, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_RIGHT:
                    global_variables.active_map.world_scroll((-20 * super_scroll), 0, global_variables.screen_width, global_variables.screen_height)
                elif event.key == pygame.K_LSHIFT:
                    super_scroll = 10
                elif event.key == pygame.K_LCTRL:
                    control_on = True

                elif event.key == pygame.K_m:
                    utilities.export_map(global_variables.active_map)
                elif event.key == pygame.K_l:
                    utilities.import_map(global_variables)
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
                    debug.event_processing(global_variables.active_map, global_variables.debug_status, event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if debug_stats.debug:
                    debug.mouse_processing(global_variables.active_map, global_variables.debug_status, mouse_pos, event)
                else:
                    if mouse_pos[0] > global_variables.screen_width - 80 and mouse_pos[1] > global_variables.screen_height - 80:
                        global_variables.active_map.entity_group["Avatar"][0].bag.open = True
                    else:
                        global_variables.active_map.entity_group["Avatar"][0].assign_target(global_variables, global_variables.active_map, mouse_pos)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    super_scroll = 1
                elif event.key == pygame.K_LCTRL:
                    control_on = False






        for flora in global_variables.active_map.entity_group["Flora"]:
            flora.tick_cycle()

        for npc in global_variables.active_map.entity_group["Npc"]:
            npc.tick_cycle()

        for avatar in global_variables.active_map.entity_group["Avatar"]:
            avatar.tick_cycle()
            if avatar.fighting:
                avatar.healthbar.get_state(avatar.health, avatar.tile_x, avatar.tile_y)
                global_variables.screen.blit(avatar.healthbar.red.image, [avatar.healthbar.red.rect.x + global_variables.active_map.x_shift, avatar.healthbar.red.rect.y + global_variables.active_map.y_shift])
                global_variables.screen.blit(avatar.healthbar.green.image, [avatar.healthbar.green.rect.x + global_variables.active_map.x_shift, avatar.healthbar.green.rect.y + global_variables.active_map.y_shift])



        

        for each in global_variables.active_map.entity_group["Npc"]:
            if each.activated:
                each.use(global_variables)
        for each in global_variables.active_map.entity_group["Structure"]:
            if each.activated:
                each.use(global_variables)
        for each in global_variables.active_map.entity_group["Creature"]:
            each.tick_cycle()
            if each.activated:
                each.use(global_variables)
            if each.fighting:
                combat.fight_tick(global_variables.screen, global_variables.active_map.entity_group["Avatar"][0], each)
                each.healthbar.get_state(each.health, each.tile_x, each.tile_y)
                global_variables.screen.blit(each.healthbar.red.image, [each.healthbar.red.rect.x + global_variables.active_map.x_shift, each.healthbar.red.rect.y + global_variables.active_map.y_shift])
                global_variables.screen.blit(each.healthbar.green.image, [each.healthbar.green.rect.x + global_variables.active_map.x_shift, each.healthbar.green.rect.y + global_variables.active_map.y_shift])

        bottom_pane_stamp = set_bottom_pane_stamp(global_variables.active_map, mouse_pos)
        global_variables.screen.fill(utilities.colors.black)

        # for tile in global_variables.active_map.display_tiles:
            # if utilities.on_screen(global_variables.screen_width, global_variables.screen_height, tile.rect.x, tile.rect.y, global_variables.active_map.x_shift, global_variables.active_map.y_shift):
                # global_variables.screen.blit(tile.image, [(tile.rect.x + global_variables.active_map.x_shift), (tile.rect.y + global_variables.active_map.y_shift)])
        global_variables.screen.blit(global_variables.active_map.background.image, [0 + global_variables.active_map.x_shift, 0 + global_variables.active_map.y_shift])

        global_variables.active_map.draw_to_screen(global_variables.screen, global_variables.screen_width, global_variables.screen_height)

        if mouse_pos[0] > global_variables.screen_width - 80 and mouse_pos[1] > global_variables.screen_height - 80:
            bag_image = bag_icon_selected
        else:
            bag_image = bag_icon
        global_variables.screen.blit(bag_image, [global_variables.screen_width - 80, global_variables.screen_height - 80])

        for each in global_variables.active_map.hitboxes:
            if not each.expiration_check():
                global_variables.screen.blit(each.sprite.image, [each.sprite.rect.x + global_variables.active_map.x_shift, each.sprite.rect.y + global_variables.active_map.y_shift])
                damage_stamp = tiny_font.render(str(each.damage), True, utilities.colors.white)
                global_variables.screen.blit(damage_stamp, [each.sprite.rect.x + global_variables.active_map.x_shift + 1, each.sprite.rect.y + global_variables.active_map.y_shift + 1])
            else:
                global_variables.active_map.hitboxes.remove(each)
        global_variables.screen.blit(lower_left, [0, global_variables.screen_height - 80])
        global_variables.screen.blit(bottom_pane.image, [200, global_variables.screen_height - 79])
        if bottom_pane_stamp and not debug_stats.debug:
            global_variables.screen.blit(bottom_pane_stamp, [210, global_variables.screen_height - 60])
        if debug_stats.debug:
            for each in global_variables.active_map.entity_group["Creature"]:
                each.search_area_graphic = debug.FoodSearchRadius(global_variables.active_map, each)
            debug_stats.tile_selector_graphic.update_image(mouse_pos)
            debug_stats.print_to_screen(global_variables.screen)
            pygame.draw.rect(global_variables.screen, (255, 255, 255), debug_stats.tile_selector_graphic.image, 1)
        if global_variables.active_map.entity_group["Avatar"][0].bag.open:
            done = global_variables.active_map.entity_group["Avatar"][0].bag.draw_to_screen(global_variables.screen, [global_variables.screen_width, global_variables.screen_height])

        pygame.display.flip()
        global_variables.clock.tick(60)
        global_variables.time += 1

global_variables = GlobalVariables(800, 500 + 80, 20)

main(global_variables)

