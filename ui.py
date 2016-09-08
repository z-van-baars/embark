import pygame
import utilities

pygame.init()
pygame.display.set_mode([0, 0])

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


class Button(object):
    def __init__(self, regular_image, selected_image, on_click):

        self.regular = regular_image
        self.selected = selected_image
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.regular
        self.sprite.rect = self.sprite.image.get_rect()
        self.click = on_click


class TradeScreen(object):
    def __init__(self, screen, player, merchant):
        self.player = player
        self.screen = screen
        self.merchant = merchant
        self.trading = True
        self.trade_window = pygame.sprite.Sprite()
        self.trade_window.image = trade_background
        self.trade_window.rect = self.trade_window.image.get_rect()
        self.trade_window.rect.x = 100
        self.trade_window.rect.y = 40
        x = self.trade_window.rect.x
        y = self.trade_window.rect.y

        self.player_list_top = 0
        self.merchant_list_top = 0
        self.player_selected = 4
        self.merchant_selected = 2


        def exit_clicked():
            global trading
            trading = False

        def buy_clicked():
            global merchant
            global player
            global merchant_selected
            global trade_value

            item_to_buy = merchant.items_list.pop(merchant_selected)
            trade_value -= item_to_buy.value
            self.player.bag.items_list.append(item_to_buy)
            merchant_selected = 0

        def sell_clicked():
            global merchant
            global player
            global player_selected
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
            global merchant
            global merchant_list_top

            if merchant_list_top + 14 < len(self.items_list):
                merchant_list_top += 1

        def r_up_clicked():
            global player_list_top

            if player_list_top - 1 >= 0:
                player_list_top -= 1

        def r_down_clicked():
            global player
            global player_list_top

            if player_list_top + 14 < len(player.bag.items_list):
                player_list_top += 1

        def finalize_clicked():
            pass

        exit_button = Button(exit_button_regular, exit_button_selected, exit_clicked)
        buy_button = Button(buy_button_regular, buy_button_selected, buy_clicked)
        sell_button = Button(sell_button_regular, sell_button_selected, sell_clicked)
        finalize_button = Button(finalize_button_regular, finalize_button_selected, finalize_clicked)
        l_up_arrow = Button(small_up_arrow_regular, small_up_arrow_selected, l_up_clicked)
        l_down_arrow = Button(small_down_arrow_regular, small_down_arrow_selected, l_down_clicked)
        r_up_arrow = Button(small_up_arrow_regular, small_up_arrow_selected, r_up_clicked)
        r_down_arrow = Button(small_down_arrow_regular, small_down_arrow_selected, r_down_clicked)

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

        self.buttons = [
            exit_button,
            buy_button,
            sell_button,
            finalize_button,
            l_up_arrow,
            l_down_arrow,
            r_up_arrow,
            r_down_arrow
            ]

    def trade(self, screen, player, merchant):
        player_selection_box = pygame.sprite.Sprite()
        merchant_selection_box = pygame.sprite.Sprite()
        trade_value = 0
        font = pygame.font.SysFont('Calibri', 26, True, False)
        small_font = pygame.font.SysFont('Calibri', 18, True, False)
        while self.trading:
            merchant_visible_items = merchant.items_list[self.merchant_list_top:self.merchant_list_top + 14]
            player_visible_items = player.bag.items_list[self.player_list_top:self.player_list_top + 14]
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.trading = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    count = 0
                    spacer = 18
                    for each in player_visible_items:
                        x1 = self.trade_window.rect.left + 405
                        x2 = x1 + 170
                        y1 = (self.trade_window.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            self.player_selected = count + self.player_list_top
                        count += 1
                    count = 0
                    for each in merchant_visible_items:
                        x1 = self.trade_window.rect.left + 115
                        x2 = x1 + 170
                        y1 = (self.trade_window.rect.top + 84 + (count * spacer))
                        y2 = y1 + 19
                        if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                            self.merchant_selected = count + self.merchant_list_top
                        count += 1

            player_selection_box.image = pygame.Rect(self.trade_window.rect.left + 405, self.trade_window.rect.top + 84 + ((self.player_selected - self.player_list_top) * 18), 170, 19)
            merchant_selection_box.image = pygame.Rect(self.trade_window.rect.left + 115, self.trade_window.rect.top + 84 + ((self.merchant_selected - self.merchant_list_top) * 18), 170, 19)

            for button in self.buttons:
                if utilities.check_if_inside(button.sprite.rect.x, button.sprite.rect.right, button.sprite.rect.y, button.sprite.rect.bottom, mouse_pos):
                    button.sprite.image = button.selected
                    if click:
                        button.click()
                else:
                    button.sprite.image = button.regular

            screen.blit(self.trade_window.image, [self.trade_window.rect.left, self.trade_window.rect.top])
            for button in self.buttons:
                screen.blit(button.sprite.image, [button.sprite.rect.x, button.sprite.rect.y])

            screen.blit(font.render(str(trade_value), True, utilities.colors.black), [self.trade_window.rect.left + 260, self.trade_window.rect.bottom - 42])

            spacer = 18
            count = 0
            for each in merchant_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                screen.blit(value_stamp, [self.trade_window.rect.left + 30, self.trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(weight_stamp, [self.trade_window.rect.left + 80, self.trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(name_stamp, [self.trade_window.rect.left + 120, self.trade_window.rect.top + 84 + (count * spacer)])
                count += 1
            count = 0
            for each in player_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                screen.blit(value_stamp, [self.trade_window.rect.left + 320, self.trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(weight_stamp, [self.trade_window.rect.left + 370, self.trade_window.rect.top + 84 + (count * spacer)])
                screen.blit(name_stamp, [self.trade_window.rect.left + 410, self.trade_window.rect.top + 84 + (count * spacer)])
                count += 1
            if self.player_selected >= self.player_list_top and self.player_selected <= self.player_list_top + 14:
                pygame.draw.rect(screen, (255, 255, 255), player_selection_box.image, 1)
            if self.merchant_selected >= self.merchant_list_top and self.merchant_selected <= self.merchant_list_top + 14:
                pygame.draw.rect(screen, (255, 255, 255), merchant_selection_box.image, 1)
            pygame.display.flip()


class LootScreen(object):
    def __init__(self, screen, player, container):
        pass