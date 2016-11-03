import pygame
import item
import ui
import art
import utilities
import weapon


class InventoryMenu(ui.Menu):
    def __init__(self, game_state, pos):
        super().__init__(game_state, pos, None)
        self.player_list_top = 0
        self.player_selected = 0
        self.open = False

        def exit_clicked():
            self.open = False

        def r_up_clicked():
            if self.player_list_top - 1 >= 0:
                self.player_list_top -= 1

        def r_down_clicked():
            if self.player_list_top + 14 < len(self.player.items_list):
                self.player_list_top += 1

        def stats_clicked():
            pass

        def equip_clicked():
            selected_item = self.player.items_list[self.player_selected]
            if selected_item.equippable:
                if selected_item.is_equipped:
                    selected_item.unequip(self.player)
                else:
                    selected_item.equip(self.player)
                    self.player.action = 0
                    self.player.fight_frame = 0

        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = art.inventory_background
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = self.screen_width / 2 - 350
        self.background_pane.rect.y = self.screen_height / 2 - 200
        x = self.background_pane.rect.x
        y = self.background_pane.rect.y

        exit_button = ui.Button(ui.x_deselected_image,
                                ui.x_selected_image,
                                exit_clicked,
                                (x + 672),
                                (y + 10))

        r_up_arrow = ui.Button(ui.small_up_arrow_regular,
                               ui.small_up_arrow_selected,
                               r_up_clicked,
                               (x + 675),
                               (y + 45))
        r_down_arrow = ui.Button(ui.small_down_arrow_regular,
                                 ui.small_down_arrow_selected,
                                 r_down_clicked,
                                 (x + 675),
                                 (y + 323))

        equip_button = ui.Button(art.equip_deselected_image,
                                 art.equip_selected_image,
                                 equip_clicked,
                                 (x + 340),
                                 (y + 360))

        stats_button = ui.Button(art.stats_deselected_image,
                                 art.stats_selected_image,
                                 stats_clicked,
                                 (x + 460),
                                 (y + 360))

        self.buttons = [exit_button,
                        r_up_arrow,
                        r_down_arrow,
                        stats_button,
                        equip_button]

    def menu_onscreen(self):
        player_selection_box = pygame.sprite.Sprite()
        font = pygame.font.SysFont('Sitka', 26, True, False)
        small_font = pygame.font.SysFont('Sitka', 18, True, False)
        while self.open:
            player_visible_items = self.player.items_list[self.player_list_top:self.player_list_top + 14]
            click = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.open = False
                    pygame.display.quit()
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if self.player_list_top - 1 >= 0:
                            self.player_list_top -= 1
                    elif event.button == 5:
                        if self.player_list_top + 14 < len(self.player.items_list):
                            self.player_list_top += 1
                    else:
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

            player_selection_box.image = pygame.Rect(self.background_pane.rect.left + 396,
                                                     self.background_pane.rect.top + 84 + ((self.player_selected - self.player_list_top) * 18),
                                                     276,
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

            stat_stamps = [[str(self.player.health) + "/" + str(self.player.max_health), 74, 66],
                           [str(self.player.strength), 96, 89],
                           [str(self.player.willpower), 106, 112],
                           [str(self.player.agility), 76, 134],
                           [str(self.player.attack), 76, 166],
                           [str(self.player.archery), 86, 189],
                           [str(self.player.combat_magic), 96, 233],
                           [str(self.player.healing_magic), 96, 256],
                           [str(self.player.melee_damage), 230, 252],
                           [str(self.player.ranged_damage), 230, 275],
                           [str(self.player.block), 230, 295],
                           [str(self.player.armor), 230, 316]]

            self.screen.blit(font.render(str(self.player.gold), True, utilities.colors.border_gold),
                             [self.background_pane.rect.left + 410, self.background_pane.rect.top + 12])
            self.screen.blit(font.render(str(self.player.level), True, utilities.colors.border_gold),
                             [self.background_pane.rect.left + 90, self.background_pane.rect.top + 34])
            for each in stat_stamps:
                string = each[0]
                left_spacer = each[1]
                top_spacer = each[2]
                self.screen.blit(small_font.render(string, True, utilities.colors.border_gold),
                                 [self.background_pane.rect.left + left_spacer, self.background_pane.rect.top + top_spacer])
            x_boost = 268
            y_boost = 80
            self.screen.blit(self.player.sprite.image, [self.background_pane.rect.left + x_boost,
                                                        self.background_pane.rect.top + y_boost])

            if self.player.equipped["Helmet"]:
                self.screen.blit(self.player.equipped["Helmet"].icon,
                                 [self.background_pane.rect.left + 200, self.background_pane.rect.top + 61])
                self.screen.blit(self.player.equipped["Helmet"].sprite.image, [self.background_pane.rect.left + x_boost,
                                                                               self.background_pane.rect.top + y_boost])
            if self.player.equipped["Gloves"]:
                self.screen.blit(self.player.equipped["Gloves"].icon,
                                 [self.background_pane.rect.left + 155, self.background_pane.rect.top + 121])
                self.screen.blit(self.player.equipped["Gloves"].sprite.image, [self.background_pane.rect.left + x_boost,
                                                                               self.background_pane.rect.top + y_boost])
            if self.player.equipped["Body Armor"]:
                self.screen.blit(self.player.equipped["Body Armor"].icon,
                                 [self.background_pane.rect.left + 199, self.background_pane.rect.top + 116])
                self.screen.blit(self.player.equipped["Body Armor"].sprite.image, [self.background_pane.rect.left + x_boost,
                                                                                   self.background_pane.rect.top + y_boost])
            if self.player.equipped["Boots"]:
                self.screen.blit(self.player.equipped["Boots"].icon,
                                 [self.background_pane.rect.left + 200, self.background_pane.rect.top + 201])
                self.screen.blit(self.player.equipped["Boots"].sprite.image, [self.background_pane.rect.left + x_boost,
                                                                              self.background_pane.rect.top + y_boost])

            if self.player.equipped["Weapon"]:
                self.screen.blit(self.player.equipped["Weapon"].icon,
                                 [self.background_pane.rect.left + 155, self.background_pane.rect.top + 178])
                self.screen.blit(self.player.equipped["Weapon"].sprite.image, [self.background_pane.rect.left + x_boost - 1,
                                                                               self.background_pane.rect.top + y_boost - 42])

            spacer = 18
            count = 0
            for each in player_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.border_gold)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.border_gold)

                if each.is_equipped:
                    color = utilities.colors.equipped_item_red
                else:
                    color = utilities.colors.border_gold
                name_stamp = small_font.render(each.name, True, color)

                self.screen.blit(value_stamp, [self.background_pane.rect.left + 320,
                                               self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(weight_stamp, [self.background_pane.rect.left + 370,
                                                self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(name_stamp, [self.background_pane.rect.left + 400,
                                              self.background_pane.rect.top + 84 + (count * spacer)])
                count += 1
            if self.player_selected >= self.player_list_top and self.player_selected <= self.player_list_top + 14:
                pygame.draw.rect(self.screen, (255, 198, 13), player_selection_box.image, 1)
            pygame.display.flip()


