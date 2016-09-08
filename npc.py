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
        new_trade_window = ui.TradeScreen(screen, player, self)
        new_trade_window.trade(new_trade_window.screen, new_trade_window.player, new_trade_window.merchant)
