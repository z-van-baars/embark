import pygame
import entity
import utilities
import item
import ui

pygame.init()
pygame.display.set_mode([0, 0])

guard_image = pygame.image.load("art/npc/guard.png").convert()
guard_image.set_colorkey(utilities.colors.key)
merchant_image = pygame.image.load("art/npc/merchant.png").convert()
merchant_image.set_colorkey(utilities.colors.key)
context_menu_pane = pygame.image.load("art/ui_elements/context_options_bg.png").convert()
trade_selected_image = pygame.image.load("art/ui_elements/trade_sel.png").convert()
trade_regular_image = pygame.image.load("art/ui_elements/trade_reg.png").convert()
leave_selected_image = pygame.image.load("art/ui_elements/leave_sel.png").convert()
leave_regular_image = pygame.image.load("art/ui_elements/leave_reg.png").convert()

trade_background = pygame.image.load("art/ui_elements/tradescreen/trade_window.png").convert()

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




class Npc(entity.Entity):
    occupies_tile = True
    interactable = True
    my_type = "Npc"

    def __init__(self, x, y, current_map, display_name="New NPC"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.sprite.image = pygame.Surface([20, 40])
        self.sprite.image.fill((255, 187, 0))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = self.tile_y * 20
        self.change_x = 0
        self.change_y = 0
        self.target_coordinates = None
        self.path = None
        self.speed = 1
        self.time_since_last_move = 0
        self.activated = False

        self.health = 100
        self.max_health = 100

    def tick_cycle(self):
        self.age += 1

    def use(self):
        print("%s: Hello from the kingdom of poopburg" % self.display_name)


class Guard(Npc):
    def __init__(self, x, y, current_map, display_name="Town Guard"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.sprite.image = guard_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - 1) * 20
        self.speed = 1
        self.health = 100
        self.max_health = 100

    def tick_cycle(self):
        self.age += 1

    def use(self, global_variables):
        font = pygame.font.SysFont('Calibri', 18, True, False)
        print("%s: Welcome to the town of poopybutts, in the kingdom of poopburg" % self.display_name)
        greeting_string = "Hello Adventurer!"
        greeting = font.render(greeting_string, True, utilities.colors.black)
        greeting_open = True
        while greeting_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    greeting_open = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    greeting_open = False

            global_variables.screen.blit(context_menu_pane, [self.sprite.rect.x, self.sprite.rect.y - 80])
            global_variables.screen.blit(greeting, [self.sprite.rect.x + 7, self.sprite.rect.y - 72])

            pygame.display.flip()
        self.activated = False


class Merchant(Npc):
    def __init__(self, x, y, current_map, display_name="Merchant"):
        super().__init__(x, y, current_map)
        self.display_name = display_name
        self.sprite.image = merchant_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - 1) * 20
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.gold = 100
        self.items_list = []
        for each in item.weapons:
            for iteration in range(9):
                new_item = item.Item(each[0], each[1], each[2])
                self.items_list.append(new_item)

    def tick_cycle(self):
        self.age += 1

    def use(self, global_variables):
        print("%s: Lots of quality goods for sale here." % self.display_name)
        context_menu_open = True
        trade_status = False
        while context_menu_open:
            trade_button = trade_regular_image
            leave_button = leave_regular_image
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    context_menu_open = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    context_menu_open, trade_status = self.click_handler(mouse_pos, (global_variables.screen_width, global_variables.screen_height))
            if self.sprite.rect.y - 72 < mouse_pos[1] < self.sprite.rect.y - 50:
                if self.sprite.rect.x + 7 < mouse_pos[0] < self.sprite.rect.x + 67:
                    trade_button = trade_selected_image
                elif self.sprite.rect.x + 73 < mouse_pos[0] < self.sprite.rect.x + 133:
                    leave_button = leave_selected_image

            global_variables.screen.blit(context_menu_pane, [self.sprite.rect.x, self.sprite.rect.y - 80])
            global_variables.screen.blit(trade_button, [self.sprite.rect.x + 7, self.sprite.rect.y - 72])
            global_variables.screen.blit(leave_button, [self.sprite.rect.x + 73, self.sprite.rect.y - 72])

            pygame.display.flip()
            if trade_status:
                self.trade(global_variables.screen, self.current_map.entity_group["Avatar"][0])
        self.activated = False

    def click_handler(self, pos, screen_dimensions):
        if pos[0] > screen_dimensions[0] - 80 and pos[1] > screen_dimensions[1] - 80:
            return False, False
        else:
            if self.sprite.rect.y - 72 < pos[1] < self.sprite.rect.y - 50:
                if self.sprite.rect.x + 7 < pos[0] < self.sprite.rect.x + 67:
                    return False, True
                elif self.sprite.rect.x + 73 < pos[0] < self.sprite.rect.x + 133:
                    return False, False
            else:
                return True, False

    def trade(self, screen, player):
        font = pygame.font.SysFont('Calibri', 26, True, False)
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        trading = True
        trade_window = pygame.sprite.Sprite()
        trade_window.image = trade_background
        trade_window.rect = trade_window.image.get_rect()
        trade_window.rect.x = 100
        trade_window.rect.y = 40
        x = trade_window.rect.x
        y = trade_window.rect.y

        player_list_top = 0
        merchant_list_top = 0
        player_selected = 4
        merchant_selected = 2
        player_selection_box = pygame.sprite.Sprite()
        merchant_selection_box = pygame.sprite.Sprite()

        def exit_clicked():
            global trading
            trading = False

        def buy_clicked():
            global merchant_selected
            global self
            global player
            global trade_value

            item_to_buy = self.items_list.pop(merchant_selected)
            trade_value -= item_to_sell.value
            player.bag.items_list.append(item_to_buy)
            merchant_selected = 0

        def sell_clicked():
            global player_selected
            global self
            global player
            global trade_value

            item_to_sell = player.bag.items_list.pop(player_selected)
            trade_value += item_to_sell.value
            self.items_list.append(item_to_sell)
            player_selected = 0

        def l_up_clicked():
            global merchant_list_top
            if merchant_list_top - 1 >= 0:
                merchant_list_top -= 1

        def l_down_clicked():
            global merchant_list_top
            global self
            if merchant_list_top + 14 < len(self.items_list):
                merchant_list_top += 1

        def r_up_clicked():
            global player_list_top
            if player_list_top - 1 >= 0:
                player_list_top -= 1

        def r_down_clicked():
            global player_list_top
            global player
            if player_list_top + 14 < len(player.bag.items_list):
                player_list_top += 1

        def finalize_clicked():
            pass

        exit_button = ui.Button(exit_button_regular, exit_button_selected, exit_clicked)
        buy_button = ui.Button(buy_button_regular, buy_button_selected, buy_clicked)
        sell_button = ui.Button(sell_button_regular, sell_button_selected, sell_clicked)
        finalize_button = ui.Button(finalize_button_regular, finalize_button_selected, finalize_clicked)
        l_up_arrow = ui.Button(small_up_arrow_regular, small_up_arrow_selected, l_up_clicked)
        l_down_arrow = ui.Button(small_down_arrow_regular, small_down_arrow_selected, l_down_clicked)
        r_up_arrow = ui.Button(small_up_arrow_regular, small_up_arrow_selected, r_up_clicked)
        r_down_arrow = ui.Button(small_down_arrow_regular, small_down_arrow_selected, r_down_clicked)

        exit_button.sprite.rect.x = (x + 546)
        exit_button.sprite.rect.y = (y + 10)

        buy_button.sprite.rect.x = (x + 25)
        buy_button.sprite.rect.y = (y + 350)

        sell_button.sprite.rect.x = (x + 455)
        sell_button.sprite.rect.y = (y + 350)

        finalize_button.sprite.rect.x = (x + 220)
        finalize_button.sprite.rect.y = (y + 350)

        l_up_arrow.sprite.rect.x = (x + 4)
        l_up_arrow.sprite.rect.y = (y + 46)

        l_down_arrow.sprite.rect.x = (x + 4)
        l_down_arrow.sprite.rect.y = (y + 326)

        r_up_arrow.sprite.rect.x = (x + 578)
        r_up_arrow.sprite.rect.y = (y + 46)

        r_down_arrow.sprite.rect.x = (x + 578)
        r_down_arrow.sprite.rect.y = (y + 326)

        buttons = [
            exit_button,
            buy_button,
            sell_button,
            finalize_button,
            l_up_arrow,
            l_down_arrow,
            r_up_arrow,
            r_down_arrow
            ]

        while trading:

            merchant_visible_items = self.items_list[merchant_list_top:merchant_list_top + 14]
            player_visible_items = player.bag.items_list[player_list_top:player_list_top + 14]
            trade_value = 0
            click = False

            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    trading = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    count = 0
                    spacer = 18
                    for each in player_visible_items:
                        x1 = trade_window.rect.left + 405
                        x2 = x1 + 170
                        y1 = (trade_window.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            player_selected = count + player_list_top
                        count += 1
                    count = 0
                    for each in merchant_visible_items:
                        x1 = trade_window.rect.left + 115
                        x2 = x1 + 170
                        y1 = (trade_window.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            merchant_selected = count + merchant_list_top
                        count += 1

            player_selection_box.image = pygame.Rect(trade_window.rect.left + 405, trade_window.rect.top + 84 + ((player_selected - player_list_top) * 18), 170, 19)
            merchant_selection_box.image = pygame.Rect(trade_window.rect.left + 115, trade_window.rect.top + 84 + ((merchant_selected - merchant_list_top) * 18), 170, 19)

            for button in buttons:
                if utilities.check_if_inside(button.sprite.rect.x, button.sprite.rect.right, button.sprite.rect.y, button.sprite.rect.bottom, mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            screen.blit(trade_window.image, [trade_window.rect.left, trade_window.rect.top])
            for button in buttons:
                screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            screen.blit(font.render(str(trade_value), True, utilities.colors.black), [trade_window.rect.left + 260, trade_window.rect.bottom - 42])

            spacer = 18
            count = 0
            for each in merchant_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                screen.blit(value_stamp, [trade_window.rect.left + 30, trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(weight_stamp, [trade_window.rect.left + 80, trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(name_stamp, [trade_window.rect.left + 120, trade_window.rect.top + 84 + (count * spacer)])
                count += 1
            count = 0
            for each in player_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                screen.blit(value_stamp, [trade_window.rect.left + 320, trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(weight_stamp, [trade_window.rect.left + 370, trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(name_stamp, [trade_window.rect.left + 410, trade_window.rect.top + 84 + (count * spacer)])
                count += 1
            if player_selected >= player_list_top and player_selected <= player_list_top + 14:
                pygame.draw.rect(screen, (255, 255, 255), player_selection_box.image, 1)
            if merchant_selected >= merchant_list_top and merchant_selected <= merchant_list_top + 14:
                pygame.draw.rect(screen, (255, 255, 255), merchant_selection_box.image, 1)
            pygame.display.flip()
