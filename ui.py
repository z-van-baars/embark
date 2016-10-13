import pygame
import utilities
from item import quality_colors
import game_map

pygame.init()
pygame.display.set_mode([0, 0])

trade_background = pygame.image.load("art/ui_elements/tradescreen/trade_window.png").convert()
loot_background = pygame.image.load("art/ui_elements/lootscreen/loot_screen.png").convert()

door_edit_menu_pane = pygame.image.load("art/ui_elements/door_editor/door_edit_menu_bg.png")

small_up_arrow_selected = pygame.image.load("art/ui_elements/tradescreen/small_up_arrow_selected.png").convert()
small_up_arrow_regular = pygame.image.load("art/ui_elements/tradescreen/small_up_arrow_regular.png").convert()
small_down_arrow_selected = pygame.image.load("art/ui_elements/tradescreen/small_down_arrow_selected.png").convert()
small_down_arrow_regular = pygame.image.load("art/ui_elements/tradescreen/small_down_arrow_regular.png").convert()
buy_button_selected = pygame.image.load("art/ui_elements/tradescreen/buy_selected.png").convert()
buy_button_regular = pygame.image.load("art/ui_elements/tradescreen/buy_regular.png").convert()
sell_button_selected = pygame.image.load("art/ui_elements/tradescreen/sell_selected.png").convert()
sell_button_regular = pygame.image.load("art/ui_elements/tradescreen/sell_regular.png").convert()
finalize_button_selected = pygame.image.load("art/ui_elements/tradescreen/finalize_order_selected.png").convert()
finalize_button_regular = pygame.image.load("art/ui_elements/tradescreen/finalize_order_regular.png").convert()
exit_button_selected = pygame.image.load("art/ui_elements/tradescreen/exit_selected.png").convert()
exit_button_regular = pygame.image.load("art/ui_elements/tradescreen/exit_regular.png").convert()

take_button_regular = pygame.image.load("art/ui_elements/lootscreen/take_image_regular.png").convert()
take_button_selected = pygame.image.load("art/ui_elements/lootscreen/take_image_selected.png").convert()
give_button_regular = pygame.image.load("art/ui_elements/lootscreen/give_image_regular.png").convert()
give_button_selected = pygame.image.load("art/ui_elements/lootscreen/give_image_selected.png").convert()

player_hitbox_image = pygame.image.load("art/ui_elements/player_hitbox.png")
enemy_hitbox_image = pygame.image.load("art/ui_elements/enemy_hitbox.png")


context_menu_pane = pygame.image.load("art/ui_elements/contextmenu/context_options_bg.png").convert()
talk_selected_image = pygame.image.load("art/ui_elements/contextmenu/talk_selected.png").convert()
talk_deselected_image = pygame.image.load("art/ui_elements/contextmenu/talk_deselected.png").convert()
move_selected_image = pygame.image.load("art/ui_elements/contextmenu/move_selected.png").convert()
move_deselected_image = pygame.image.load("art/ui_elements/contextmenu/move_deselected.png").convert()
cancel_selected_image = pygame.image.load("art/ui_elements/contextmenu/cancel_selected.png").convert()
cancel_deselected_image = pygame.image.load("art/ui_elements/contextmenu/cancel_deselected.png").convert()
use_selected_image = pygame.image.load("art/ui_elements/contextmenu/use_selected.png").convert()
use_deselected_image = pygame.image.load("art/ui_elements/contextmenu/use_deselected.png").convert()
attack_selected_image = pygame.image.load("art/ui_elements/contextmenu/attack_selected.png").convert()
attack_deselected_image = pygame.image.load("art/ui_elements/contextmenu/attack_deselected.png").convert()

dialogue_menu_pane = pygame.image.load("art/ui_elements/dialogue_box/dialogue_background.png").convert()
leave_selected_image = pygame.image.load("art/ui_elements/dialogue_box/leave_selected.png").convert()
leave_deselected_image = pygame.image.load("art/ui_elements/dialogue_box/leave_deselected.png").convert()
more_selected_image = pygame.image.load("art/ui_elements/dialogue_box/more_selected.png").convert()
more_deselected_image = pygame.image.load("art/ui_elements/dialogue_box/more_deselected.png").convert()
trade_selected_image = pygame.image.load("art/ui_elements/dialogue_box/trade_selected.png").convert()
trade_deselected_image = pygame.image.load("art/ui_elements/dialogue_box/trade_deselected.png").convert()
back_selected_image = pygame.image.load("art/ui_elements/dialogue_box/back_selected.png").convert()
back_deselected_image = pygame.image.load("art/ui_elements/dialogue_box/back_deselected.png").convert()


edit_deselected_image = pygame.image.load("art/ui_elements/dialogue_box/edit_deselected.png").convert()
edit_selected_image = pygame.image.load("art/ui_elements/dialogue_box/edit_selected.png").convert()

map_editor_bg = pygame.image.load("art/ui_elements/map_editor/map_editor_bg.png").convert()
new_map_bg = pygame.image.load("art/ui_elements/map_editor/new_map_bg.png").convert()

accept_selected_image = pygame.image.load("art/ui_elements/map_editor/accept_selected.png").convert()
accept_deselected_image = pygame.image.load("art/ui_elements/map_editor/accept_deselected.png").convert()
map_cancel_selected_image = pygame.image.load("art/ui_elements/map_editor/cancel_selected.png").convert()
map_cancel_deselected_image = pygame.image.load("art/ui_elements/map_editor/cancel_deselected.png").convert()
delete_selected_image = pygame.image.load("art/ui_elements/map_editor/delete_selected.png").convert()
delete_deselected_image = pygame.image.load("art/ui_elements/map_editor/delete_deselected.png").convert()
load_selected_image = pygame.image.load("art/ui_elements/map_editor/load_selected.png").convert()
load_deselected_image = pygame.image.load("art/ui_elements/map_editor/load_deselected.png").convert()
new_selected_image = pygame.image.load("art/ui_elements/map_editor/new_selected.png").convert()
new_deselected_image = pygame.image.load("art/ui_elements/map_editor/new_deselected.png").convert()
x_selected_image = pygame.image.load("art/ui_elements/map_editor/x_selected.png").convert()
x_deselected_image = pygame.image.load("art/ui_elements/map_editor/x_deselected.png").convert()
up_arrow_deselected_image = pygame.image.load("art/ui_elements/map_editor/up_arrow_deselected.png").convert()
up_arrow_selected_image = pygame.image.load("art/ui_elements/map_editor/up_arrow_selected.png").convert()
down_arrow_deselected_image = pygame.image.load("art/ui_elements/map_editor/down_arrow_deselected.png").convert()
down_arrow_selected_image = pygame.image.load("art/ui_elements/map_editor/down_arrow_selected.png").convert()


class HitBox(object):
    def __init__(self, current_map, x, y, damage, owner):
        self.current_map = current_map
        self.age = 0
        self.damage = damage
        self.sprite = pygame.sprite.Sprite()

        if owner == "Avatar":
            self.sprite.image = player_hitbox_image
        else:
            self.sprite.image = enemy_hitbox_image

        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y - 10

        self.current_map.hitboxes.append(self)

    def expiration_check(self):
        self.age += 1
        return self.age > 30


class HealthBar(object):
    def __init__(self, current_map, x, y, health, max_health):
        self.current_map = current_map
        self.max_health = max_health
        self.current_map.healthbars.append(self)
        self.red = pygame.sprite.Sprite()
        self.green = pygame.sprite.Sprite()
        self.red.image = pygame.Surface([18, 3])
        self.green.image = pygame.Surface([18, 3])
        self.red.image.fill(utilities.colors.red)
        self.green.image.fill(utilities.colors.bright_blue)
        self.red.rect = self.red.image.get_rect()
        self.green.rect = self.green.image.get_rect()
        self.active = False

    def get_state(self, health, tile_x, tile_y):
        health_per_pixel = self.max_health / 18
        green_pixels = health / health_per_pixel
        if green_pixels < 1:
            green_pixels = 0
        self.green.image = pygame.Surface([green_pixels, 3])
        self.green.image.fill(utilities.colors.bright_blue)
        self.green.rect = self.green.image.get_rect()
        self.green.rect.x = tile_x * 20 + 1
        self.green.rect.y = tile_y * 20 + 21
        self.red.rect.x = tile_x * 20 + 1
        self.red.rect.y = tile_y * 20 + 21

        if health <= 0:
            self.active = False


class Button(object):
    def __init__(self, regular_image, selected_image, on_click, x=0, y=0):

        self.regular = regular_image
        self.selected = selected_image
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.regular
        self.sprite.rect = self.sprite.image.get_rect()
        self.click = on_click
        self.sprite.rect.x = x
        self.sprite.rect.y = y


class TileSelectorGraphic(pygame.sprite.Sprite):
    def __init__(self, x, y, current_map):
        super().__init__()
        self.tile_x = x
        self.tile_y = y
        self.current_map = current_map

        self.update_image((0, 0))

    def update_image(self, mouse_pos):
        # print(int((mouse_pos[0] - self.current_map.x_shift) / 20), int((mouse_pos[1] - self.current_map.y_shift) / 20))
        self.tile_x = int((mouse_pos[0] + self.current_map.x_shift) / 20)
        self.tile_y = int((mouse_pos[1] + self.current_map.y_shift) / 20)

        self.image = pygame.Rect((int(mouse_pos[0] / 20) * 20), (int(mouse_pos[1] / 20) * 20), 20, 20)


class Menu(object):
    def __init__(self, game_state, pos, entity):
        self.open = True
        self.player = game_state.player
        self.entity = entity
        self.screen = game_state.screen
        self.active_map = game_state.active_map
        self.screen_width = game_state.screen_width
        self.screen_height = game_state.screen_height

    def menu_onscreen(self):
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class MapEditor(Menu):
    def __init__(self, game_state):
        super().__init__(game_state, None, None)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = map_editor_bg
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 200
        self.background_pane.rect.y = self.screen_height / 2 - 180
        self.editing = False
        self.maps_list = []
        for each in game_state.maps:
            self.maps_list.append(each)
        self.maps_list = sorted(self.maps_list)
        self.maps_list_top = 0
        self.selected_map = 0

        def up_arrow_click():
            if self.maps_list_top > 0:
                self.maps_list_top -= 1

        def down_arrow_click():
            if self.maps_list_top < len(self.maps_list) - 12:
                self.maps_list_top += 1

        def new_click():
            new_map_window = NewMapWindow(game_state)
            new_map_window.menu_onscreen()
            self.maps_list = []
            for each in game_state.maps:
                self.maps_list.append(each)
            self.maps_list = sorted(self.maps_list)

        def delete_click():
            map_string = self.maps_list[self.selected_map]
            del game_state.maps[map_string]
            self.maps_list = []
            for each in game_state.maps:
                self.maps_list.append(each)
            self.maps_list = sorted(self.maps_list)

        def load_click():
            map_string = self.maps_list[self.selected_map]
            game_state.active_map = game_state.maps[map_string]
            self.open = False

        def x_click():
            self.open = False

        x_button = Button(x_deselected_image,
                          x_selected_image,
                          x_click,
                          self.background_pane.rect.x + 360,
                          self.background_pane.rect.y + 5)
        up_arrow_button = Button(up_arrow_deselected_image,
                                 up_arrow_selected_image,
                                 up_arrow_click,
                                 self.background_pane.rect.x + 353,
                                 self.background_pane.rect.y + 44)
        down_arrow_button = Button(down_arrow_deselected_image,
                                   down_arrow_selected_image,
                                   down_arrow_click,
                                   self.background_pane.rect.x + 353,
                                   self.background_pane.rect.y + 266)
        new_button = Button(new_deselected_image,
                            new_selected_image,
                            new_click,
                            self.background_pane.rect.x + 20,
                            self.background_pane.rect.y + 310)
        delete_button = Button(delete_deselected_image,
                               delete_selected_image,
                               delete_click,
                               self.background_pane.rect.x + 280,
                               self.background_pane.rect.y + 310)
        load_button = Button(load_deselected_image,
                             load_selected_image,
                             load_click,
                             self.background_pane.rect.x + 150,
                             self.background_pane.rect.y + 310)

        self.buttons = [x_button, up_arrow_button, down_arrow_button, new_button, load_button, delete_button]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        cursor = small_font.render("<", True, utilities.colors.red)
        map_selection_box = pygame.sprite.Sprite()
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            visible_maps = self.maps_list[self.maps_list_top:self.maps_list_top + 12]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    count = 0
                    spacer = 20
                    for each in visible_maps:
                        x1 = self.background_pane.rect.left + 22
                        x2 = x1 + 200
                        y1 = (self.background_pane.rect.top + 44 + (count * spacer))
                        y2 = y1 + 20
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            if count + self.maps_list_top <= len(self.maps_list):
                                self.selected_map = count + self.maps_list_top
                        count += 1
            map_selection_box.image = pygame.Rect(self.background_pane.rect.left + 20,
                                                  self.background_pane.rect.top + 44 + ((self.selected_map - self.maps_list_top) * 20),
                                                  200,
                                                  20)

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])

            spacer = 20
            count = 0
            for each in visible_maps:
                name_stamp = small_font.render(each, True, utilities.colors.light_grey)
                self.screen.blit(name_stamp, [self.background_pane.rect.left + 22,
                                              self.background_pane.rect.top + 44 + (count * spacer)])
                count += 1
            if self.selected_map >= self.maps_list_top and self.selected_map <= self.maps_list_top + 44:
                pygame.draw.rect(self.screen, (255, 198, 13), map_selection_box.image, 1)

            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class NewMapWindow(Menu):
    def __init__(self, game_state):
        super().__init__(game_state, None, None)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = new_map_bg
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 170
        self.background_pane.rect.y = self.screen_height / 2 - 95
        self.editing = False
        self.new_map_name = "New Map 001"
        self.new_map_x = 10
        self.new_map_y = 10

        def map_cancel_click():
            self.open = False

        def accept_click():
            new_map = game_map.Map(self.new_map_name,
                                   (self.new_map_x, self.new_map_y),
                                   (game_state.screen_width, game_state.screen_height),
                                   False)
            new_map.map_generation()
            game_state.maps[new_map.name] = new_map
            self.open = False

        def x_up_click():
            if self.new_map_x < 100:
                self.new_map_x += 1

        def x_down_click():
            if self.new_map_x > 2:
                self.new_map_x -= 1

        def y_up_click():
            if self.new_map_y < 100:
                self.new_map_y += 1

        def y_down_click():
            if self.new_map_y > 2:
                self.new_map_y -= 1

        map_cancel_button = Button(map_cancel_deselected_image,
                                   map_cancel_selected_image,
                                   map_cancel_click,
                                   self.background_pane.rect.x + 234,
                                   self.background_pane.rect.y + 5)

        accept_button = Button(accept_deselected_image,
                               accept_selected_image,
                               accept_click,
                               self.background_pane.rect.x + 234,
                               self.background_pane.rect.y + 150)

        x_up_button = Button(up_arrow_deselected_image,
                             up_arrow_selected_image,
                             x_up_click,
                             self.background_pane.rect.x + 50,
                             self.background_pane.rect.y + 85)

        x_down_button = Button(down_arrow_deselected_image,
                               down_arrow_selected_image,
                               x_down_click,
                               self.background_pane.rect.x + 50,
                               self.background_pane.rect.y + 150)

        y_up_button = Button(up_arrow_deselected_image,
                             up_arrow_selected_image,
                             y_up_click,
                             self.background_pane.rect.x + 138,
                             self.background_pane.rect.y + 85)

        y_down_button = Button(down_arrow_deselected_image,
                               down_arrow_selected_image,
                               y_down_click,
                               self.background_pane.rect.x + 138,
                               self.background_pane.rect.y + 150)

        self.buttons = [map_cancel_button, accept_button, x_up_button, x_down_button, y_up_button, y_down_button]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        cursor = small_font.render("<", True, utilities.colors.red)
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if utilities.check_if_inside(self.background_pane.rect.x + 16,
                                                 self.background_pane.rect.right - 10,
                                                 self.background_pane.rect.y + 48,
                                                 self.background_pane.rect.y + 70,
                                                 mouse_pos):
                        self.editing = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.new_map_name = self.new_map_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.editing = False
                    else:
                        self.new_map_name += event.unicode

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])

            name_stamp = small_font.render(self.new_map_name, True, utilities.colors.light_grey)
            self.screen.blit(name_stamp, [self.background_pane.rect.x + 20, self.background_pane.rect.y + 48])
            self.screen.blit(small_font.render(str(self.new_map_x), True, utilities.colors.light_grey),
                             [self.background_pane.rect.x + 50, self.background_pane.rect.y + 122])
            self.screen.blit(small_font.render(str(self.new_map_y), True, utilities.colors.light_grey),
                             [self.background_pane.rect.x + 138, self.background_pane.rect.y + 122])
            if self.editing:
                self.screen.blit(cursor, [name_stamp.get_width() + self.background_pane.rect.left + 20,
                                          self.background_pane.rect.y + 48])

            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class DialogueEditor(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = dialogue_menu_pane
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 200
        self.background_pane.rect.y = self.screen_height / 2 - 80
        self.dialogue_page = 0
        self.dialogue_line = 0
        self.editing = False

        def leave_click():
            self.open = False

        def more_click():
            self.dialogue_page += 1
            self.dialogue_line = 0
            if self.dialogue_page > len(self.entity.dialogue_pages) - 1:
                self.dialogue_page = 0

        def back_click():
            self.dialogue_page -= 1
            self.dialogue_line = 0
            if self.dialogue_page < 0:
                self.dialogue_page = len(self.entity.dialogue_pages) - 1

        def edit_click():
            self.editing = not self.editing

        leave_button = Button(leave_deselected_image,
                              leave_selected_image,
                              leave_click,
                              self.background_pane.rect.x + 324,
                              self.background_pane.rect.y + 130)

        back_button = Button(back_deselected_image,
                             back_selected_image,
                             back_click,
                             self.background_pane.rect.x + 205,
                             self.background_pane.rect.y + 130)

        more_button = Button(more_deselected_image,
                             more_selected_image,
                             more_click,
                             self.background_pane.rect.x + 145,
                             self.background_pane.rect.y + 130)

        edit_button = Button(edit_deselected_image,
                             edit_selected_image,
                             edit_click,
                             self.background_pane.rect.x + 20,
                             self.background_pane.rect.y + 130)

        self.buttons = [leave_button, back_button, more_button, edit_button]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        cursor = small_font.render("<", True, utilities.colors.red)
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                if self.editing:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            line = self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line]
                            line = line[:-1]
                            self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line] = line
                        elif event.key == pygame.K_RETURN:
                            self.entity.dialogue_pages.append([''])
                        elif event.key == pygame.K_UP:
                            if self.dialogue_line > 0:
                                self.dialogue_line -= 1
                        elif event.key == pygame.K_DOWN:
                            if self.dialogue_line < 2:
                                self.dialogue_line += 1
                        elif event.key == pygame.K_TAB:
                            if len(self.entity.dialogue_pages[self.dialogue_page]) < 2:
                                self.entity.dialogue_pages[self.dialogue_page].append("")
                        else:
                            self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line] += event.unicode

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            if self.editing:
                self.screen.blit(small_font.render("Editing Dialogue", True, utilities.colors.black),
                                 [self.background_pane.rect.x, self.background_pane.rect.y + 4])
            self.screen.blit(small_font.render(self.entity.display_name, True, utilities.colors.black),
                             [self.background_pane.rect.x + 180, self.background_pane.rect.y + 4])
            counter = 0
            for dialogue_line in self.entity.dialogue_pages[self.dialogue_page]:
                counter += 1
                self.screen.blit(small_font.render(dialogue_line, True, utilities.colors.black),
                                 [self.background_pane.rect.left + 25, self.background_pane.rect.top + counter * 20 + 20])
            active_dialogue_line = small_font.render(self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line], True, utilities.colors.black)
            if self.editing:
                self.screen.blit(cursor, [active_dialogue_line.get_width() + self.background_pane.rect.left + 27,
                                          self.background_pane.rect.top + (self.dialogue_line + 1) * 20 + 20])

            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class DialogueMenu(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = dialogue_menu_pane
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 200
        self.background_pane.rect.y = self.screen_height / 2 - 80
        self.dialogue_page = 0

        def leave_click():
            self.open = False

        def more_click():
            self.dialogue_page += 1
            if self.dialogue_page > len(self.entity.dialogue_pages) - 1:
                self.dialogue_page = 0

        def back_click():
            if self.dialogue_page > 0:
                self.dialogue_page -= 1

        def trade_click():
            self.open = False
            new_trade_window = TradeMenu(game_state, (pos), self.entity)
            new_trade_window.menu_onscreen()

        leave_button = Button(leave_deselected_image,
                              leave_selected_image,
                              leave_click,
                              self.background_pane.rect.x + 324,
                              self.background_pane.rect.y + 130)

        back_button = Button(back_deselected_image,
                             back_selected_image,
                             back_click,
                             self.background_pane.rect.x + 205,
                             self.background_pane.rect.y + 130)

        more_button = Button(more_deselected_image,
                             more_selected_image,
                             more_click,
                             self.background_pane.rect.x + 145,
                             self.background_pane.rect.y + 130)

        trade_button = Button(trade_deselected_image,
                              trade_selected_image,
                              trade_click,
                              self.background_pane.rect.x + 20,
                              self.background_pane.rect.y + 130)

        if entity.items_list:
            self.buttons = [leave_button, back_button, more_button, trade_button]
        else:
            self.buttons = [leave_button, back_button, more_button]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            self.screen.blit(small_font.render(self.entity.display_name, True, utilities.colors.black),
                             [self.background_pane.rect.x + 180, self.background_pane.rect.y + 4])
            counter = 0
            for dialogue_line in self.entity.dialogue_pages[self.dialogue_page]:
                counter += 1
                self.screen.blit(small_font.render(dialogue_line, True, utilities.colors.black),
                                 [self.background_pane.rect.left + 25, self.background_pane.rect.top + counter * 20 + 20])

            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class SignpostMenu(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = dialogue_menu_pane
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 200
        self.background_pane.rect.y = self.screen_height / 2 - 80
        self.dialogue_page = 0

        def leave_click():
            self.open = False

        def more_click():
            self.dialogue_page += 1
            if self.dialogue_page > len(self.entity.dialogue_pages) - 1:
                self.dialogue_page = 0

        def back_click():
            if self.dialogue_page > 0:
                self.dialogue_page -= 1

        def trade_click():
            self.open = False
            new_trade_window = TradeMenu(game_state, (pos), self.entity)
            new_trade_window.menu_onscreen()

        leave_button = Button(leave_deselected_image,
                              leave_selected_image,
                              leave_click,
                              self.background_pane.rect.x + 324,
                              self.background_pane.rect.y + 130)

        self.buttons = [leave_button]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular
            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            self.screen.blit(small_font.render(self.entity.display_name, True, utilities.colors.black),
                             [self.background_pane.rect.x + 180, self.background_pane.rect.y + 4])
            counter = 0
            for dialogue_line in self.entity.dialogue_pages[self.dialogue_page]:
                counter += 1
                self.screen.blit(small_font.render(dialogue_line, True, utilities.colors.black),
                                 [self.background_pane.rect.left + 25, self.background_pane.rect.top + counter * 20 + 20])

            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class SignpostEditor(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = dialogue_menu_pane
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 200
        self.background_pane.rect.y = self.screen_height / 2 - 80
        self.dialogue_page = 0
        self.dialogue_line = 0
        self.editing = False

        def leave_click():
            self.open = False

        def more_click():
            self.dialogue_page += 1
            self.dialogue_line = 0
            if self.dialogue_page > len(self.entity.dialogue_pages) - 1:
                self.dialogue_page = 0

        def back_click():
            self.dialogue_page -= 1
            self.dialogue_line = 0
            if self.dialogue_page < 0:
                self.dialogue_page = len(self.entity.dialogue_pages) - 1

        def edit_click():
            self.editing = not self.editing

        leave_button = Button(leave_deselected_image,
                              leave_selected_image,
                              leave_click,
                              self.background_pane.rect.x + 324,
                              self.background_pane.rect.y + 130)

        back_button = Button(back_deselected_image,
                             back_selected_image,
                             back_click,
                             self.background_pane.rect.x + 205,
                             self.background_pane.rect.y + 130)

        more_button = Button(more_deselected_image,
                             more_selected_image,
                             more_click,
                             self.background_pane.rect.x + 145,
                             self.background_pane.rect.y + 130)

        edit_button = Button(edit_deselected_image,
                             edit_selected_image,
                             edit_click,
                             self.background_pane.rect.x + 20,
                             self.background_pane.rect.y + 130)

        self.buttons = [leave_button, back_button, more_button, edit_button]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        cursor = small_font.render("<", True, utilities.colors.red)
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                if self.editing:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            line = self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line]
                            line = line[:-1]
                            self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line] = line
                        elif event.key == pygame.K_RETURN:
                            self.entity.dialogue_pages.append([''])
                        elif event.key == pygame.K_UP:
                            if self.dialogue_line > 0:
                                self.dialogue_line -= 1
                        elif event.key == pygame.K_DOWN:
                            if self.dialogue_line < 2:
                                self.dialogue_line += 1
                        elif event.key == pygame.K_TAB:
                            if len(self.entity.dialogue_pages[self.dialogue_page]) < 2:
                                self.entity.dialogue_pages[self.dialogue_page].append("")
                        else:
                            self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line] += event.unicode

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            if self.editing:
                self.screen.blit(small_font.render("Editing Signpost", True, utilities.colors.black),
                                 [self.background_pane.rect.x, self.background_pane.rect.y + 4])
            self.screen.blit(small_font.render(self.entity.display_name, True, utilities.colors.black),
                             [self.background_pane.rect.x + 180, self.background_pane.rect.y + 4])
            counter = 0
            for dialogue_line in self.entity.dialogue_pages[self.dialogue_page]:
                counter += 1
                self.screen.blit(small_font.render(dialogue_line, True, utilities.colors.black),
                                 [self.background_pane.rect.left + 25, self.background_pane.rect.top + counter * 20 + 20])
            active_dialogue_line = small_font.render(self.entity.dialogue_pages[self.dialogue_page][self.dialogue_line], True, utilities.colors.black)
            if self.editing:
                self.screen.blit(cursor, [active_dialogue_line.get_width() + self.background_pane.rect.left + 27,
                                          self.background_pane.rect.top + (self.dialogue_line + 1) * 20 + 20])

            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class ContextMenu(Menu):
    def __init__(self, game_state, pos, entity, entity_string):
        super().__init__(game_state, pos, entity)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = context_menu_pane
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.tile_selector_graphic = TileSelectorGraphic(0, 0, self.active_map)
        self.tile_selector_graphic.update_image(pos)
        if pos[0] < self.screen_width - 140:
            self.background_pane.rect.x = pos[0]
        else:
            self.background_pane.rect.right = pos[0]
        if pos[1] < self.screen_height - 100:
            self.background_pane.rect.y = pos[1]
        else:
            self.background_pane.rect.bottom = pos[1]

        def cancel_click():
            self.open = False

        def talk_click():
            self.open = False
            self.player.target_object = entity
            self.player.target_coordinates = (entity.tile_x, entity.tile_y)
            self.player.target_type = 2

        def attack_click():
            self.open = False
            self.player.target_object = entity
            self.player.target_coordinates = (entity.tile_x, entity.tile_y)
            self.player.target_type = 3

        def use_click():
            self.open = False
            self.player.target_object = entity
            self.player.target_coordinates = (entity.tile_x, entity.tile_y)
            self.player.target_type = 2

        def move_click():
            self.open = False
            self.player.target_type = 1

        cancel_button = Button(cancel_deselected_image,
                               cancel_selected_image,
                               cancel_click,
                               self.background_pane.rect.x + 74,
                               self.background_pane.rect.y + 10)

        talk_button = Button(talk_deselected_image,
                             talk_selected_image,
                             talk_click,
                             self.background_pane.rect.x + 8,
                             self.background_pane.rect.y + 10)
        use_button = Button(use_deselected_image,
                            use_selected_image,
                            use_click,
                            self.background_pane.rect.x + 8,
                            self.background_pane.rect.y + 10)
        attack_button = Button(attack_deselected_image,
                               attack_selected_image,
                               attack_click,
                               self.background_pane.rect.x + 8,
                               self.background_pane.rect.y + 10)

        move_button = Button(move_deselected_image,
                             move_selected_image,
                             move_click,
                             self.background_pane.rect.x + 8,
                             self.background_pane.rect.y + 10)

        button_sets = {"Npc": [cancel_button, talk_button],
                       "Creature": [cancel_button, attack_button],
                       "Structure": [cancel_button, use_button],
                       "Open": [cancel_button, move_button]}

        self.buttons = button_sets[entity_string]


class TradeMenu(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.player_list_top = 0
        self.merchant_list_top = 0
        self.player_selected = 0
        self.merchant_selected = 0
        self.trade_value = 0
        self.items_to_sell = []
        self.items_to_buy = []

        def exit_clicked():
            self.open = False
            self.player.items_list.extend(self.items_to_sell)
            self.entity.items_list.extend(self.items_to_buy)

        def buy_clicked():
            if self.entity.items_list:
                item_to_buy = self.entity.items_list.pop(self.merchant_selected)
                self.trade_value -= item_to_buy.value
                self.items_to_buy.append(item_to_buy)
                self.merchant_selected = 0

        def sell_clicked():
            if self.player.items_list:
                item_to_sell = self.player.items_list.pop(self.player_selected)
                self.trade_value += item_to_sell.value
                self.items_to_sell.append(item_to_sell)
                self.player_selected = 0

        def l_up_clicked():
            if self.merchant_list_top - 1 >= 0:
                self.merchant_list_top -= 1

        def l_down_clicked():
            if self.merchant_list_top + 14 < len(self.entity.items_list):
                self.merchant_list_top += 1

        def r_up_clicked():
            if self.player_list_top - 1 >= 0:
                self.player_list_top -= 1

        def r_down_clicked():
            if self.player_list_top + 14 < len(self.player.items_list):
                self.player_list_top += 1

        def finalize_clicked():
            if 0 <= self.player.gold + self.trade_value and 0 <= self.entity.gold - self.trade_value:
                self.player.gold += self.trade_value
                self.entity.gold -= self.trade_value
                self.player.items_list.extend(self.items_to_buy)
                self.entity.items_list.extend(self.items_to_sell)
                self.items_to_sell = []
                self.items_to_buy = []
                self.trade_value = 0
            elif 0 > self.player.gold + self.trade_value and 0 <= self.entity.gold - self.trade_value:
                print("player does not have enough gold!")
            elif 0 <= self.player.gold + self.trade_value and 0 > self.entity.gold - self.trade_value:
                print("merchant does not have enough gold!")
            else:
                print("Nobody has enough gold!")

        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = trade_background
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = 100
        self.background_pane.rect.y = 40
        x = self.background_pane.rect.x
        y = self.background_pane.rect.y

        exit_button = Button(exit_button_regular,
                             exit_button_selected,
                             exit_clicked,
                             (x + 546),
                             (y + 10))
        buy_button = Button(buy_button_regular,
                            buy_button_selected,
                            buy_clicked,
                            (x + 25),
                            (y + 350))
        sell_button = Button(sell_button_regular,
                             sell_button_selected,
                             sell_clicked,
                             (x + 455),
                             (y + 350))
        finalize_button = Button(finalize_button_regular,
                                 finalize_button_selected,
                                 finalize_clicked,
                                 (x + 220),
                                 (y + 350))
        l_up_arrow = Button(small_up_arrow_regular,
                            small_up_arrow_selected,
                            l_up_clicked,
                            (x + 4),
                            (y + 46))
        l_down_arrow = Button(small_down_arrow_regular,
                              small_down_arrow_selected,
                              l_down_clicked,
                              (x + 4),
                              (y + 326))
        r_up_arrow = Button(small_up_arrow_regular,
                            small_up_arrow_selected,
                            r_up_clicked,
                            (x + 578),
                            (y + 46))
        r_down_arrow = Button(small_down_arrow_regular,
                              small_down_arrow_selected,
                              r_down_clicked,
                              (x + 578),
                              (y + 326))

        self.buttons = [exit_button,
                        buy_button,
                        sell_button,
                        finalize_button,
                        l_up_arrow,
                        l_down_arrow,
                        r_up_arrow,
                        r_down_arrow]

    def menu_onscreen(self):
        player_selection_box = pygame.sprite.Sprite()
        merchant_selection_box = pygame.sprite.Sprite()
        font = pygame.font.SysFont('Sitka', 26, True, False)
        small_font = pygame.font.SysFont('Sitka', 18, True, False)
        while self.open:
            merchant_visible_items = self.entity.items_list[self.merchant_list_top:self.merchant_list_top + 14]
            player_visible_items = self.player.items_list[self.player_list_top:self.player_list_top + 14]
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    count = 0
                    spacer = 18
                    for each in player_visible_items:
                        x1 = self.background_pane.rect.left + 405
                        x2 = x1 + 170
                        y1 = (self.background_pane.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            if count + self.player_list_top <= len(self.player.items_list):
                                self.player_selected = count + self.player_list_top
                        count += 1
                    count = 0
                    for each in merchant_visible_items:
                        x1 = self.background_pane.rect.left + 115
                        x2 = x1 + 170
                        y1 = (self.background_pane.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            if count + self.merchant_list_top <= len(self.entity.items_list):
                                self.merchant_selected = count + self.merchant_list_top
                        count += 1

            player_selection_box.image = pygame.Rect(self.background_pane.rect.left + 395,
                                                     self.background_pane.rect.top + 84 + ((self.player_selected - self.player_list_top) * 18),
                                                     180,
                                                     19)
            merchant_selection_box.image = pygame.Rect(self.background_pane.rect.left + 105,
                                                       self.background_pane.rect.top + 84 + ((self.merchant_selected - self.merchant_list_top) * 18),
                                                       180,
                                                       19)

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y, button.sprite.rect.bottom, mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            self.screen.blit(font.render(str(self.trade_value), True, utilities.colors.black),
                             [self.background_pane.rect.left + 260, self.background_pane.rect.bottom - 42])
            self.screen.blit(font.render(str(self.entity.gold), True, utilities.colors.black),
                             [self.background_pane.rect.left + 135, self.background_pane.rect.top + 12])
            self.screen.blit(font.render(str(self.player.gold), True, utilities.colors.black),
                             [self.background_pane.rect.left + 410, self.background_pane.rect.top + 12])

            spacer = 18
            count = 0
            for each in merchant_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                self.screen.blit(value_stamp, [self.background_pane.rect.left + 30,
                                               self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(weight_stamp, [self.background_pane.rect.left + 80,
                                                self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(name_stamp, [self.background_pane.rect.left + 110,
                                              self.background_pane.rect.top + 84 + (count * spacer)])
                count += 1
            count = 0
            for each in player_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)

                self.screen.blit(value_stamp, [self.background_pane.rect.left + 320,
                                               self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(weight_stamp, [self.background_pane.rect.left + 370,
                                                self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(name_stamp, [self.background_pane.rect.left + 400,
                                              self.background_pane.rect.top + 84 + (count * spacer)])
                count += 1
            if self.player_selected >= self.player_list_top and self.player_selected <= self.player_list_top + 14:
                pygame.draw.rect(self.screen, (255, 198, 13), player_selection_box.image, 1)
            if self.merchant_selected >= self.merchant_list_top and self.merchant_selected <= self.merchant_list_top + 14:
                pygame.draw.rect(self.screen, (255, 198, 13), merchant_selection_box.image, 1)
            pygame.display.flip()


class LootMenu(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.player_list_top = 0
        self.container_list_top = 0
        self.player_selected = 0
        self.container_selected = 0
        self.items_to_give = []
        self.items_to_take = []

        def exit_clicked():
            self.open = False

        def take_clicked():
            if self.entity.items_list:
                item_to_take = entity.items_list.pop(self.container_selected)
                self.player.items_list.append(item_to_take)
                self.container_selected = 0

        def give_clicked():
            if self.player.items_list:
                item_to_give = self.player.items_list.pop(self.player_selected)
                self.entity.items_list.append(item_to_give)
                self.player_selected = 0

        def l_up_clicked():
            if self.container_list_top - 1 >= 0:
                self.container_list_top -= 1

        def l_down_clicked():
            if self.container_list_top + 14 < len(self.entity.items_list):
                self.container_list_top += 1

        def r_up_clicked():
            if self.player_list_top - 1 >= 0:
                self.player_list_top -= 1

        def r_down_clicked():
            if self.player_list_top + 14 < len(self.player.items_list):
                self.player_list_top += 1

        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = loot_background
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = 100
        self.background_pane.rect.y = 40
        x = self.background_pane.rect.x
        y = self.background_pane.rect.y

        exit_button = Button(exit_button_regular,
                             exit_button_selected,
                             exit_clicked,
                             (x + 546),
                             (y + 10))
        take_button = Button(take_button_regular,
                             take_button_selected,
                             take_clicked,
                             (x + 25),
                             (y + 350))
        give_button = Button(give_button_regular,
                             give_button_selected,
                             give_clicked,
                             (x + 455),
                             (y + 350))
        l_up_arrow = Button(small_up_arrow_regular,
                            small_up_arrow_selected,
                            l_up_clicked,
                            (x + 4),
                            (y + 46))
        l_down_arrow = Button(small_down_arrow_regular,
                              small_down_arrow_selected,
                              l_down_clicked,
                              (x + 4),
                              (y + 326))
        r_up_arrow = Button(small_up_arrow_regular,
                            small_up_arrow_selected,
                            r_up_clicked,
                            (x + 578),
                            (y + 46))
        r_down_arrow = Button(small_down_arrow_regular,
                              small_down_arrow_selected,
                              r_down_clicked,
                              (x + 578),
                              (y + 326))

        self.buttons = [exit_button,
                        take_button,
                        give_button,
                        l_up_arrow,
                        l_down_arrow,
                        r_up_arrow,
                        r_down_arrow]

    def menu_onscreen(self):
        player_selection_box = pygame.sprite.Sprite()
        container_selection_box = pygame.sprite.Sprite()
        font = pygame.font.SysFont('Calibri', 26, True, False)
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        while self.open:
            container_visible_items = self.entity.items_list[self.container_list_top:self.container_list_top + 14]
            player_visible_items = self.player.items_list[self.player_list_top:self.player_list_top + 14]
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.looting = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    count = 0
                    spacer = 18
                    for each in player_visible_items:
                        x1 = self.background_pane.rect.left + 405
                        x2 = x1 + 170
                        y1 = (self.background_pane.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            if count + self.player_list_top <= len(self.player.items_list):
                                self.player_selected = count + self.player_list_top
                        count += 1
                    count = 0
                    for each in container_visible_items:
                        x1 = self.background_pane.rect.left + 115
                        x2 = x1 + 170
                        y1 = (self.background_pane.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            if count + self.container_list_top <= len(self.entity.items_list):
                                self.container_selected = count + self.container_list_top
                        count += 1

            player_selection_box.image = pygame.Rect(self.background_pane.rect.left + 405,
                                                     self.background_pane.rect.top + 84 + ((self.player_selected - self.player_list_top) * 18),
                                                     170,
                                                     19)
            container_selection_box.image = pygame.Rect(self.background_pane.rect.left + 115,
                                                        self.background_pane.rect.top + 84 +
                                                        ((self.container_selected - self.container_list_top) * 18),
                                                        170,
                                                        19)

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])
            self.screen.blit(font.render(str(self.player.gold), True, utilities.colors.black),
                             [self.background_pane.rect.left + 410, self.background_pane.rect.top + 12])
            spacer = 18
            count = 0
            for each in container_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                self.screen.blit(value_stamp,
                                 [self.background_pane.rect.left + 30, self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(weight_stamp,
                                 [self.background_pane.rect.left + 80, self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(name_stamp,
                                 [self.background_pane.rect.left + 120, self.background_pane.rect.top + 84 + (count * spacer)])
                count += 1
            count = 0
            for each in player_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                self.screen.blit(value_stamp,
                                 [self.background_pane.rect.left + 320, self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(weight_stamp,
                                 [self.background_pane.rect.left + 370, self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(name_stamp,
                                 [self.background_pane.rect.left + 410, self.background_pane.rect.top + 84 + (count * spacer)])
                count += 1
            if self.player_selected >= self.player_list_top and self.player_selected <= self.player_list_top + 14:
                pygame.draw.rect(self.screen, (255, 198, 13), player_selection_box.image, 1)
            if self.container_selected >= self.container_list_top and self.container_selected <= self.container_list_top + 14:
                pygame.draw.rect(self.screen, (255, 198, 13), container_selection_box.image, 1)
            pygame.display.flip()


class ChestEditMenu(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = context_menu_pane
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 100
        self.background_pane.rect.y = self.screen_height / 2 - 80
        self.dialogue_page = 0

        def leave_click():
            entity.opened = False
            self.open = False

        def up_click():
            if self.entity.value < 100:
                self.entity.value += 5

        def down_click():
            if self.entity.value > 0:
                self.entity.value -= 5

        leave_button = Button(leave_deselected_image,
                              leave_selected_image,
                              leave_click,
                              self.background_pane.rect.x + 80,
                              self.background_pane.rect.y + 10)
        up_arrow = Button(small_up_arrow_regular,
                          small_up_arrow_selected,
                          up_click,
                          (self.background_pane.rect.x + 5),
                          (self.background_pane.rect.y + 10))
        down_arrow = Button(small_down_arrow_regular,
                            small_down_arrow_selected,
                            down_click,
                            (self.background_pane.rect.x + 55),
                            (self.background_pane.rect.y + 10))

        self.buttons = [leave_button, up_arrow, down_arrow]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            self.screen.blit(small_font.render(str(self.entity.value), True, utilities.colors.black),
                             [self.background_pane.rect.x + 30, self.background_pane.rect.y + 10])
            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()


class DoorEditMenu(Menu):
    def __init__(self, game_state, pos, entity):
        super().__init__(game_state, pos, entity)
        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = door_edit_menu_pane
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 100
        self.background_pane.rect.y = self.screen_height / 2 - 80
        self.dialogue_page = 0

        self.maps_list = []

        for each in game_state.maps:
            self.maps_list.append(each)
        self.maps_list = sorted(self.maps_list)
        if entity.twin_map is not None and entity.twin_map in game_state.maps:
            self.selected_map = self.maps_list.index(entity.twin_map)
        else:
            self.selected_map = 0

        def leave_click():
            self.open = False
            entity.twin_map = self.maps_list[self.selected_map]

        def x_up_click():
            entity.destination_x += 1

        def x_down_click():
            if not entity.destination_x == 0:
                entity.destination_x -= 1

        def y_up_click():
            entity.destination_y += 1

        def y_down_click():
            if not entity.destination_y == 0:
                entity.destination_y -= 1

        def map_up_click():
            self.selected_map -= 1
            if self.selected_map < 0:
                self.selected_map = len(self.maps_list) - 1

        def map_down_click():
            self.selected_map += 1
            if self.selected_map > len(self.maps_list) - 1:
                self.selected_map = 0

        leave_button = Button(leave_deselected_image,
                              leave_selected_image,
                              leave_click,
                              self.background_pane.rect.x + 135,
                              self.background_pane.rect.y + 170)
        map_up_arrow = Button(small_up_arrow_regular,
                              small_up_arrow_selected,
                              map_up_click,
                              (self.background_pane.rect.x + 20),
                              (self.background_pane.rect.y + 35))
        map_down_arrow = Button(small_down_arrow_regular,
                                small_down_arrow_selected,
                                map_down_click,
                                (self.background_pane.rect.x + 150),
                                (self.background_pane.rect.y + 35))

        x_up_arrow = Button(small_up_arrow_regular,
                            small_up_arrow_selected,
                            x_up_click,
                            (self.background_pane.rect.x + 60),
                            (self.background_pane.rect.y + 100))
        x_down_arrow = Button(small_down_arrow_regular,
                              small_down_arrow_selected,
                              x_down_click,
                              (self.background_pane.rect.x + 110),
                              (self.background_pane.rect.y + 100))
        y_up_arrow = Button(small_up_arrow_regular,
                            small_up_arrow_selected,
                            y_up_click,
                            (self.background_pane.rect.x + 60),
                            (self.background_pane.rect.y + 170))
        y_down_arrow = Button(small_down_arrow_regular,
                              small_down_arrow_selected,
                              y_down_click,
                              (self.background_pane.rect.x + 110),
                              (self.background_pane.rect.y + 170))

        self.buttons = [leave_button, map_up_arrow, map_down_arrow, x_up_arrow, x_down_arrow, y_up_arrow, y_down_arrow]

    def menu_onscreen(self):
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        while self.open:
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x,
                                             button.sprite.rect.right,
                                             button.sprite.rect.y,
                                             button.sprite.rect.bottom,
                                             mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            self.screen.blit(self.background_pane.image, [self.background_pane.rect.left, self.background_pane.rect.top])
            self.screen.blit(small_font.render(str(self.maps_list[self.selected_map]), True, utilities.colors.black),
                             [self.background_pane.rect.x + 70, self.background_pane.rect.y + 35])
            self.screen.blit(small_font.render(str(self.entity.destination_x), True, utilities.colors.black),
                             [self.background_pane.rect.x + 80, self.background_pane.rect.y + 100])
            self.screen.blit(small_font.render(str(self.entity.destination_y), True, utilities.colors.black),
                             [self.background_pane.rect.x + 80, self.background_pane.rect.y + 170])
            self.screen.blit(small_font.render("{0}, {1}".format(self.entity.tile_x, self.entity.tile_y), True, utilities.colors.black),
                             [self.background_pane.rect.x + 2, self.background_pane.rect.y + 176])
            for button in self.buttons:
                self.screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            pygame.display.flip()