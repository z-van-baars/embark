import pygame
import utilities
from utilities import GameState
from game_map import Map
import debug
import inventory
from avatar import Avatar
import ui
import weapon
import armor

pygame.init()
pygame.display.set_mode([0, 0])

lower_left = pygame.image.load("art/ui_elements/lower_left/lower_left.png").convert()
bag_deselected = pygame.image.load("art/ui_elements/bag.png").convert()
bag_selected = pygame.image.load("art/ui_elements/bag_highlight.png").convert()


def open_inventory(game_state, mouse_pos):
    inventory_window = inventory.InventoryMenu(game_state, mouse_pos)
    inventory_window.open = True
    inventory_window.menu_onscreen()


def menu_button_click(game_state):
    menu_window = ui.OptionsMenu(game_state)
    menu_window.open = True
    game_state = menu_window.menu_onscreen()
    return game_state


def set_bottom_pane_stamp(current_map, mouse_pos):
    font = pygame.font.SysFont('Calibri', 18, True, False)

    def get_name_stamp(selected_tile):
        for entity_type in selected_tile.entity_group:
            if selected_tile.entity_group[entity_type]:
                if selected_tile.entity_group[entity_type][0].occupies_tile:
                    entity = selected_tile.entity_group[entity_type][0]
                    stamp = font.render(entity.display_name, True, utilities.colors.border_gold)
        return stamp

    tile_x = int((mouse_pos[0] - current_map.x_shift) / 20)
    tile_y = int((mouse_pos[1] - current_map.y_shift) / 20)

    if utilities.within_map(tile_x, tile_y, current_map):
        selected_tile = current_map.game_tile_rows[tile_y][tile_x]
        if selected_tile and selected_tile.is_occupied():
            stamp = get_name_stamp(selected_tile)
            return stamp
        else:
            return None
    else:
        return None


def create_new_world(game_state):
    map_1 = Map("Swindon", (60, 60), (game_state.screen_width, game_state.screen_height))
    map_1.map_generation()

    Avatar(5, 5, map_1)
    game_state.maps[map_1.name] = map_1
    game_state.active_map = game_state.maps["Swindon"]
    game_state.player = game_state.active_map.entity_group["Avatar"][0]

    game_state.player.fight_frame = 0

    debug_stats = debug.DebugStatus(game_state.active_map, game_state)
    debug_stats.tile_selector_graphic = ui.TileSelectorGraphic(0, 0, game_state.active_map)
    game_state.debug_status = debug_stats

    item_1 = weapon.weapon_functions[0](1, game_state.player.level)

    initial_equipment = [item_1, armor.armor_functions[0]()]
    game_state.player.items_list = initial_equipment
    game_state.player.items_list[0].equip(game_state.player)
    map_1.update_object_layer()


def main(game_state):
    #game_state = utilities.import_game_state()
    create_new_world(game_state)
    debug_stats = game_state.debug_status

    tiny_font = pygame.font.SysFont('Calibri', 11, True, False)
    done = False
    super_scroll = 1
    control_on = False

    bag_button = ui.Button(bag_deselected,
                           bag_selected,
                           open_inventory,
                           game_state.screen_width - 80,
                           game_state.screen_height - 80)

    menu_button = ui.Button(ui.menu_button_deselected,
                            ui.menu_button_selected,
                            menu_button_click,
                            game_state.screen_width - 32,
                            0)
    game_state.player.equipped_armor = None
    while not done:

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_state.active_map.world_scroll(0,
                                                       (20 * super_scroll),
                                                       game_state.screen_width,
                                                       game_state.screen_height)
                elif event.key == pygame.K_DOWN:
                    game_state.active_map.world_scroll(0,
                                                       (-20 * super_scroll),
                                                       game_state.screen_width,
                                                       game_state.screen_height)
                elif event.key == pygame.K_LEFT:
                    game_state.active_map.world_scroll((20 * super_scroll),
                                                       0,
                                                       game_state.screen_width,
                                                       game_state.screen_height)
                elif event.key == pygame.K_RIGHT:
                    game_state.active_map.world_scroll((-20 * super_scroll),
                                                       0,
                                                       game_state.screen_width,
                                                       game_state.screen_height)
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

                elif event.key == pygame.K_HOME:
                    new_map_editor = ui.MapEditor(game_state)
                    new_map_editor.menu_onscreen()

                if debug_stats.debug:
                    debug.key_event_processing(game_state.debug_status, event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if debug_stats.debug:
                    debug.mouse_processing(game_state.active_map,
                                           game_state.debug_status,
                                           mouse_pos,
                                           event,
                                           game_state)
                else:
                    if utilities.check_if_inside(bag_button.sprite.rect.x,
                                                 bag_button.sprite.rect.right,
                                                 bag_button.sprite.rect.y,
                                                 bag_button.sprite.rect.bottom,
                                                 mouse_pos):
                        bag_button.click(game_state, mouse_pos)
                    elif utilities.check_if_inside(menu_button.sprite.rect.x,
                                                   menu_button.sprite.rect.right,
                                                   menu_button.sprite.rect.y,
                                                   menu_button.sprite.rect.bottom,
                                                   mouse_pos):
                        game_state = menu_button.click(game_state)
                    else:
                        if len(game_state.active_map.entity_group["Avatar"]) > 0:
                            game_state.active_map.entity_group["Avatar"][0].assign_target(game_state,
                                                                                          game_state.active_map,
                                                                                          mouse_pos)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    super_scroll = 1
                elif event.key == pygame.K_LCTRL:
                    control_on = False

        for projectile in game_state.active_map.entity_group["Projectile"]:
            projectile.travel()
        for each in game_state.active_map.entity_group["Structure"]:
            each.tick_cycle()
        for flora in game_state.active_map.entity_group["Flora"]:
            flora.tick_cycle()

        for npc in game_state.active_map.entity_group["Npc"]:
            npc.tick_cycle()

        for avatar in game_state.active_map.entity_group["Avatar"]:
            avatar.tick_cycle(game_state)

        for each in game_state.active_map.entity_group["Creature"]:
            each.tick_cycle(game_state.player, (game_state.player.tile_x, game_state.player.tile_y))

        bottom_pane_stamp = set_bottom_pane_stamp(game_state.active_map, mouse_pos)
        game_state.screen.fill(utilities.colors.black)

        game_state.screen.blit(game_state.active_map.background.image, [0 + game_state.active_map.x_shift, 0 + game_state.active_map.y_shift])
        for each in game_state.active_map.object_layer.z_levels:
            game_state.screen.blit(each.image, [0 + game_state.active_map.x_shift, 0 + game_state.active_map.y_shift])

            game_state.active_map.draw_actors(game_state.screen,
                                              game_state.screen_width,
                                              game_state.screen_height,
                                              game_state.active_map.object_layer.z_levels.index(each) + 1)

        if utilities.check_if_inside(bag_button.sprite.rect.x,
                                     bag_button.sprite.rect.right,
                                     bag_button.sprite.rect.y,
                                     bag_button.sprite.rect.bottom,
                                     mouse_pos):
            bag_button.sprite.image = bag_button.selected
        else:
            bag_button.sprite.image = bag_button.regular

        if utilities.check_if_inside(menu_button.sprite.rect.x,
                                     menu_button.sprite.rect.right,
                                     menu_button.sprite.rect.y,
                                     menu_button.sprite.rect.bottom,
                                     mouse_pos):
            menu_button.sprite.image = menu_button.selected
        else:
            menu_button.sprite.image = menu_button.regular
        game_state.screen.blit(bag_button.sprite.image, [bag_button.sprite.rect.x, bag_button.sprite.rect.y])
        game_state.screen.blit(menu_button.sprite.image, [menu_button.sprite.rect.x, menu_button.sprite.rect.y])

        for each in game_state.active_map.hitboxes:
            if not each.expiration_check():
                game_state.screen.blit(each.sprite.image,
                                       [each.sprite.rect.x + game_state.active_map.x_shift,
                                        each.sprite.rect.y + game_state.active_map.y_shift])

                damage_stamp = tiny_font.render(str(each.damage), True, utilities.colors.white)
                game_state.screen.blit(damage_stamp,
                                       [each.sprite.rect.x + game_state.active_map.x_shift + 1,
                                        each.sprite.rect.y + game_state.active_map.y_shift + 1])
            else:
                game_state.active_map.hitboxes.remove(each)
        for each in game_state.active_map.healthbars:
            if each.active:
                game_state.screen.blit(each.red.image,
                                       [each.red.rect.x + game_state.active_map.x_shift,
                                        each.red.rect.y + game_state.active_map.y_shift])
                game_state.screen.blit(each.green.image,
                                       [each.green.rect.x + game_state.active_map.x_shift,
                                        each.green.rect.y + game_state.active_map.y_shift])
        game_state.screen.blit(lower_left, [0, game_state.screen_height - 80])
        if bottom_pane_stamp and not debug_stats.debug:
            game_state.screen.blit(bottom_pane_stamp, [10, game_state.screen_height - 60])
        if debug_stats.debug:
            for each in game_state.active_map.entity_group["Creature"]:
                each.search_area_graphic = debug.FoodSearchRadius(game_state.active_map, each)
            debug_stats.tile_selector_graphic.update_image(mouse_pos)
            debug_stats.print_to_screen(game_state.screen)
            pygame.draw.rect(game_state.screen, (255, 255, 255), debug_stats.tile_selector_graphic.image, 1)
            if debug_stats.place:
                footprint = debug.entities[debug.string_lists[debug_stats.current_entity_group][debug_stats.current_entity_type_number]].footprint
                initial_x = int(mouse_pos[0] / 20)
                initial_y = int(mouse_pos[1] / 20) - (footprint[1] - 1)
                for tile_y in range(initial_y, initial_y + (footprint[1])):
                    for tile_x in range(initial_x, initial_x + footprint[0]):
                        new_graphic = ui.TileSelectorGraphic(tile_x, tile_y, game_state.active_map)
                        new_graphic.update_image((tile_x * 20, tile_y * 20))
                        pygame.draw.rect(game_state.screen, (255, 255, 255), new_graphic.image, 1)
            if debug_stats.paint:
                footprint = debug_stats.brush_size
                initial_x = int(mouse_pos[0] / 20)
                initial_y = int(mouse_pos[1] / 20) - (footprint[1] - 1)
                for tile_y in range(initial_y, initial_y + (footprint[1])):
                    for tile_x in range(initial_x, initial_x + footprint[0]):
                        new_graphic = ui.TileSelectorGraphic(tile_x, tile_y, game_state.active_map)
                        new_graphic.update_image((tile_x * 20, tile_y * 20))
                        pygame.draw.rect(game_state.screen, (255, 255, 255), new_graphic.image, 1)

        pygame.display.flip()
        game_state.clock.tick(60)
        game_state.time += 1


game_state = GameState(800, 500 + 80, 20)

main(game_state)
