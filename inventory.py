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
            if selected_item.equipable:
                self.player.equipped_weapon.unequip(self.player)
                selected_item.equip(self.player)
                self.player.action = 0
                self.player.fight_frame = 0

        self.background_pane = pygame.sprite.Sprite()
        self.background_pane.image = art.inventory_background
        self.background_pane.rect = self.background_pane.image.get_rect()
        self.background_pane.rect.x = 100
        self.background_pane.rect.y = 40
        x = self.background_pane.rect.x
        y = self.background_pane.rect.y

        exit_button = ui.Button(ui.exit_button_regular,
                                ui.exit_button_selected,
                                exit_clicked,
                                (x + 546),
                                (y + 10))

        r_up_arrow = ui.Button(ui.small_up_arrow_regular,
                               ui.small_up_arrow_selected,
                               r_up_clicked,
                               (x + 578),
                               (y + 46))
        r_down_arrow = ui.Button(ui.small_down_arrow_regular,
                                 ui.small_down_arrow_selected,
                                 r_down_clicked,
                                 (x + 578),
                                 (y + 326))

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

            player_selection_box.image = pygame.Rect(self.background_pane.rect.left + 390,
                                                     self.background_pane.rect.top + 84 + ((self.player_selected - self.player_list_top) * 18),
                                                     184,
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
                           [str(self.player.melee_damage), 250, 248],
                           [str(self.player.ranged_damage), 260, 271],
                           [str(self.player.block), 215, 291],
                           [str(self.player.armor), 215, 312]]

            self.screen.blit(font.render(str(self.player.gold), True, utilities.colors.black),
                             [self.background_pane.rect.left + 410, self.background_pane.rect.top + 12])
            self.screen.blit(font.render(str(self.player.level), True, utilities.colors.black),
                             [self.background_pane.rect.left + 90, self.background_pane.rect.top + 34])
            for each in stat_stamps:
                string = each[0]
                left_spacer = each[1]
                top_spacer = each[2]
                self.screen.blit(small_font.render(string, True, utilities.colors.black),
                                 [self.background_pane.rect.left + left_spacer, self.background_pane.rect.top + top_spacer])

            if self.player.equipped_weapon:
                self.screen.blit(self.player.equipped_weapon.icon,
                                 [self.background_pane.rect.left + 151, self.background_pane.rect.top + 111])

            spacer = 18
            count = 0
            for each in player_visible_items:
                value_stamp = small_font.render(str(each.value), True, utilities.colors.black)
                weight_stamp = small_font.render(str(each.weight), True, utilities.colors.black)
                material_stamp = small_font.render(each.material, True, utilities.colors.black)
                name_stamp = small_font.render(each.name, True, utilities.colors.black)
                quality_stamp = small_font.render(each.quality[0], True, item.quality_colors[each.quality])

                self.screen.blit(value_stamp, [self.background_pane.rect.left + 320,
                                               self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(weight_stamp, [self.background_pane.rect.left + 370,
                                                self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(quality_stamp, [self.background_pane.rect.left + 395,
                                                 self.background_pane.rect.top + 85 + (count * spacer)])
                self.screen.blit(material_stamp, [self.background_pane.rect.left + 410,
                                                  self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(name_stamp, [self.background_pane.rect.left + 410 + material_stamp.get_width(),
                                              self.background_pane.rect.top + 84 + (count * spacer)])
                count += 1
            if self.player_selected >= self.player_list_top and self.player_selected <= self.player_list_top + 14:
                pygame.draw.rect(self.screen, (255, 198, 13), player_selection_box.image, 1)
            pygame.display.flip()


