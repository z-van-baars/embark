import pygame


class Inventory(object):
    def __init__(self, screen_height, screen_width):
        super().__init__()

        self.up_arrow_regular = pygame.image.load("art/ui_elements/up_arrow.png").convert()
        self.up_arrow_selected = pygame.image.load("art/ui_elements/up_arrow_highlight.png").convert()
        self.down_arrow_regular = pygame.image.load("art/ui_elements/down_arrow.png").convert()
        self.down_arrow_selected = pygame.image.load("art/ui_elements/down_arrow_highlight.png").convert()
        
        self.inventory_pane = pygame.sprite.Sprite()
        self.inventory_pane.image = pygame.image.load("art/ui_elements/inventory_pane.png").convert()
        self.inventory_pane.rect = self.inventory_pane.image.get_rect()
        
        self.inventory_pane.rect.x = screen_width / 2 - 200
        self.inventory_pane.rect.y = screen_height / 2 - 200

        self.up_arrow = pygame.sprite.Sprite()
        self.up_arrow.image = self.up_arrow_regular
        self.up_arrow.rect = self.up_arrow.image.get_rect()
        self.up_arrow.rect.x = self.inventory_pane.rect.x + 5
        self.up_arrow.rect.y = self.inventory_pane.rect.y + 43

        self.down_arrow = pygame.sprite.Sprite()
        self.down_arrow.image = self.down_arrow_regular
        self.down_arrow.rect = self.down_arrow.image.get_rect()
        self.down_arrow.rect.x = self.inventory_pane.rect.x + 5
        self.down_arrow.rect.y = self.inventory_pane.rect.y + 323

        self.scroll_marker = pygame.sprite.Sprite()
        self.scroll_marker.image = pygame.image.load("art/ui_elements/scroll_marker.png").convert()
        self.scroll_marker.rect = self.scroll_marker.image.get_rect()
        self.scroll_marker.rect.x = self.inventory_pane.rect.x + 5
        self.scroll_marker.rect.y = self.inventory_pane.rect.y + 76

        self.font = pygame.font.SysFont('Calibri', 24, True, False)

        self.items_list = [
                    "Iron Dagger", 
                    "Gold Coin", 
                    "Ye Flaske", 
                    "ye flaske 2", 
                    "ye flaske 3", 
                    "ye flaske 4", 
                    "ye flaske 5", 
                    "ye flaske 6",
                    "ye flaske 7",
                    "ye flaske 8",
                    "ye flaske 9",
                    "ye flaske 10"]
        self.open = False 


    def draw_to_screen(self, screen, screen_dimensions):
        start = 0
        quit = False
        while self.open:
            self.up_arrow.image = self.up_arrow_regular
            self.down_arrow.image = self.down_arrow_regular
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.open = False
                    quit = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.open, start = self.click_handler(mouse_pos, screen_dimensions, start)
            if self.inventory_pane.rect.x + 5 < mouse_pos[0] < self.inventory_pane.rect.x + 37:
                if self.inventory_pane.rect.y + 43 < mouse_pos[1] < self.inventory_pane.rect.y + 75:
                    self.up_arrow.image = self.up_arrow_selected
                elif self.inventory_pane.rect.y + 323 < mouse_pos[1] < self.inventory_pane.rect.y + 355:
                    self.down_arrow.image = self.down_arrow_selected
            screen.blit(self.inventory_pane.image, [self.inventory_pane.rect.x, self.inventory_pane.rect.y])
            screen.blit(self.up_arrow.image, [self.up_arrow.rect.x, self.up_arrow.rect.y])
            screen.blit(self.down_arrow.image, [self.down_arrow.rect.x, self.down_arrow.rect.y])
            screen.blit(self.scroll_marker.image, [self.scroll_marker.rect.x, self.scroll_marker.rect.y])
            slot = 10
            slot_spacer = 30
            visible_items = self.items_list[start:start + 9]
            for each in visible_items:
                screen.blit(self.font.render(each, True, (0, 0, 0)), (self.inventory_pane.rect.x + 45, self.inventory_pane.rect.y + 40 + slot))
                slot += slot_spacer

            pygame.display.flip()
        return quit

    def click_handler(self, pos, screen_dimensions, start):
        if pos[0] > screen_dimensions[0] - 80 and pos[1] > screen_dimensions[1] - 80:
            return False, start
        else:
            if self.inventory_pane.rect.x + 5 < pos[0] < self.inventory_pane.rect.x + 37:
                if self.inventory_pane.rect.y + 43 < pos[1] < self.inventory_pane.rect.y + 75:
                    start -= 1
                elif self.inventory_pane.rect.y + 323 < pos[1] < self.inventory_pane.rect.y + 355:
                    start += 1
            if start + 9 > len(self.items_list):
                start = len(self.items_list) - 9
            elif start < 0:
                start = 0
            return True, start