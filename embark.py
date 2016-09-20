import pygame
import utilities
from utilities import GameState
from game_map import Map
import debug
import inventory
import combat
from avatar import Avatar
import ui
import weapon

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


def create_new_world(game_state):
    map_1 = Map("Swindon", (40, 40), (game_state.screen_width, game_state.screen_height), False)
    map_1.map_generation()
    Avatar(5, 5, map_1)
    game_state.maps[map_1.name] = map_1
    game_state.active_map = game_state.maps["Swindon"]


def main(game_state):
    # game_state = utilities.import_game_state()
    create_new_world(game_state)

    tiny_font = pygame.font.SysFont('Calibri', 11, True, False)
    done = False
    super_scroll = 1
    bottom_pane = pygame.sprite.Sprite()
    bottom_pane.image = pygame.Surface([game_state.screen_width - 280, 80])
    bottom_pane.image.fill((171, 171, 171))
    control_on = False

    game_state.player = game_state.active_map.entity_group["Avatar"][0]

    game_state.player.fight_frame = 0

    debug_stats = debug.DebugStatus(game_state.active_map, game_state)
    debug_stats.tile_selector_graphic = ui.TileSelectorGraphic(0, 0, game_state.active_map)
    game_state.debug_status = debug_stats

    game_state.active_map.entity_group["Avatar"][0].bag = inventory.Inventory(game_state.screen_width, game_state.screen_height)
    sword = weapon.Sword(weapon.weapons[0][0], weapon.weapons[0][1], weapon.weapons[0][2], weapon.weapons[0][3], weapon.weapons[0][4])
    # bow = weapon.Bow(weapon.weapons[2][0], weapon.weapons[2][1], weapon.weapons[2][2], weapon.weapons[2][3], weapon.weapons[2][4])
    axe = weapon.Axe(weapon.weapons[1][0], weapon.weapons[1][1], weapon.weapons[1][2], weapon.weapons[1][3], weapon.weapons[1][4])
    initial_equipment = [sword, axe]
    game_state.player.bag.items_list = initial_equipment
    game_state.player.equipped_weapon = game_state.player.bag.items_list[0]

    while not done:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_state.active_map.world_scroll(0, (20 * super_scroll), game_state.screen_width, game_state.screen_height)
                elif event.key == pygame.K_DOWN:
                    game_state.active_map.world_scroll(0, (-20 * super_scroll), game_state.screen_width, game_state.screen_height)
                elif event.key == pygame.K_LEFT:
                    game_state.active_map.world_scroll((20 * super_scroll), 0, game_state.screen_width, game_state.screen_height)
                elif event.key == pygame.K_RIGHT:
                    game_state.active_map.world_scroll((-20 * super_scroll), 0, game_state.screen_width, game_state.screen_height)
                elif event.key == pygame.K_LSHIFT:
                    super_scroll = 10
                elif event.key == pygame.K_LCTRL:
                    control_on = True

                elif event.key == pygame.K_m:
                    utilities.export_game_state(game_state)
                elif event.key == pygame.K_l:
                    game_state = utilities.import_game_state()
                    debug_stats = game_state.debug_status
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
                    debug.key_event_processing(game_state.debug_status, event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if debug_stats.debug:
                    debug.mouse_processing(game_state.active_map, game_state.debug_status, mouse_pos, event, game_state)
                else:
                    if mouse_pos[0] > game_state.screen_width - 80 and mouse_pos[1] > game_state.screen_height - 80:
                        game_state.active_map.entity_group["Avatar"][0].bag.open = True
                    else:
                        game_state.active_map.entity_group["Avatar"][0].assign_target(game_state, game_state.active_map, mouse_pos)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    super_scroll = 1
                elif event.key == pygame.K_LCTRL:
                    control_on = False

        for flora in game_state.active_map.entity_group["Flora"]:
            flora.tick_cycle()

        for npc in game_state.active_map.entity_group["Npc"]:
            npc.tick_cycle()

        for avatar in game_state.active_map.entity_group["Avatar"]:
            avatar.tick_cycle()
            if avatar.fighting:
                
                game_state.screen.blit(avatar.healthbar.red.image, [avatar.healthbar.red.rect.x + game_state.active_map.x_shift, avatar.healthbar.red.rect.y + game_state.active_map.y_shift])
                game_state.screen.blit(avatar.healthbar.green.image, [avatar.healthbar.green.rect.x + game_state.active_map.x_shift, avatar.healthbar.green.rect.y + game_state.active_map.y_shift])

        for each in game_state.active_map.entity_group["Npc"]:
            if each.activated:
                each.use(game_state)
        for each in game_state.active_map.entity_group["Structure"]:
            if each.activated:
                each.use(game_state)
        for each in game_state.active_map.entity_group["Creature"]:
            each.tick_cycle()
            if each.activated:
                each.use(game_state)
            if each.fighting:
                combat.fight_tick(game_state.screen, game_state.active_map.entity_group["Avatar"][0], each)
                each.healthbar.get_state(each.health, each.tile_x, each.tile_y)

        bottom_pane_stamp = set_bottom_pane_stamp(game_state.active_map, mouse_pos)
        game_state.screen.fill(utilities.colors.black)

        game_state.screen.blit(game_state.active_map.background.image, [0 + game_state.active_map.x_shift, 0 + game_state.active_map.y_shift])

        game_state.active_map.draw_to_screen(game_state.screen, game_state.screen_width, game_state.screen_height)

        if mouse_pos[0] > game_state.screen_width - 80 and mouse_pos[1] > game_state.screen_height - 80:
            bag_image = bag_icon_selected
        else:
            bag_image = bag_icon
        game_state.screen.blit(bag_image, [game_state.screen_width - 80, game_state.screen_height - 80])

        for each in game_state.active_map.hitboxes:
            if not each.expiration_check():
                game_state.screen.blit(each.sprite.image, [each.sprite.rect.x + game_state.active_map.x_shift, each.sprite.rect.y + game_state.active_map.y_shift])

                damage_stamp = tiny_font.render(str(each.damage), True, utilities.colors.white)
                game_state.screen.blit(damage_stamp, [each.sprite.rect.x + game_state.active_map.x_shift + 1, each.sprite.rect.y + game_state.active_map.y_shift + 1])
            else:
                game_state.active_map.hitboxes.remove(each)
        for each in game_state.active_map.healthbars:
            if each.active:
                game_state.screen.blit(each.red.image, [each.red.rect.x + game_state.active_map.x_shift, each.red.rect.y + game_state.active_map.y_shift])
                game_state.screen.blit(each.green.image, [each.green.rect.x + game_state.active_map.x_shift, each.green.rect.y + game_state.active_map.y_shift])
        game_state.screen.blit(lower_left, [0, game_state.screen_height - 80])
        game_state.screen.blit(bottom_pane.image, [200, game_state.screen_height - 79])
        if bottom_pane_stamp and not debug_stats.debug:
            game_state.screen.blit(bottom_pane_stamp, [210, game_state.screen_height - 60])
        if debug_stats.debug:
            for each in game_state.active_map.entity_group["Creature"]:
                each.search_area_graphic = debug.FoodSearchRadius(game_state.active_map, each)
            debug_stats.tile_selector_graphic.update_image(mouse_pos)
            debug_stats.print_to_screen(game_state.screen)
            pygame.draw.rect(game_state.screen, (255, 255, 255), debug_stats.tile_selector_graphic.image, 1)
            if debug_stats.place:
                footprint = debug.entities[debug.string_lists[debug_stats.current_entity_group][debug_stats.current_entity_type_number]].footprint
                initial_x = int(debug_stats.tile_selector_graphic.tile_x)
                initial_y = int(debug_stats.tile_selector_graphic.tile_y - (footprint[1] - 1))
                for tile_y in range(initial_y, initial_y + (footprint[1])):
                    for tile_x in range(initial_x, initial_x + footprint[0]):
                        new_graphic = ui.TileSelectorGraphic(tile_x, tile_y, game_state.active_map)
                        new_graphic.update_image((tile_x * 20 - game_state.active_map.x_shift, tile_y * 20 - game_state.active_map.y_shift))
                        pygame.draw.rect(game_state.screen, (255, 255, 255), new_graphic.image, 1)

        if game_state.active_map.entity_group["Avatar"][0].bag.open:
            done = game_state.active_map.entity_group["Avatar"][0].bag.draw_to_screen(game_state.screen, [game_state.screen_width, game_state.screen_height])

        pygame.display.flip()
        game_state.clock.tick(60)
        game_state.time += 1

game_state = GameState(800, 500 + 80, 20)

main(game_state)
