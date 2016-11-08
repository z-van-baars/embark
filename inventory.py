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
        self.selection_tuple = ()
        self.open = False
        self.inventory_categories = {}
        self.current_category = 0
        self.categories = ["All", "Weapons", "Armor", "Misc"]
        self.player_cache = {}

        def exit_clicked():
            self.open = False

        def r_up_clicked():
            if self.player_list_top - 1 >= 0:
                self.player_list_top -= 1

        def r_down_clicked():
            if self.player_list_top + 14 < len(self.player.items[self.categories[self.current_category]]):
                self.player_list_top += 1

        def category_r_clicked():
            if self.current_category < len(self.categories) - 1:
                self.current_category += 1
            else:
                self.current_category = 0
            self.player_selected = 0

        def category_l_clicked():
            if self.current_category > 0:
                self.current_category -= 1
            else:
                self.current_category = len(self.categories) - 1
            self.player_selected = 0

        def stats_clicked():
            pass

        def equip_clicked():
            selected_item = self.player.items[self.player_selected_tuple[1]][self.player_selected_tuple[2]]
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

        category_r_button = ui.Button(ui.small_right_arrow_regular,
                                      ui.small_right_arrow_selected,
                                      category_r_clicked,
                                      (x + 622),
                                      (y + 54))

        category_l_button = ui.Button(ui.small_left_arrow_regular,
                                      ui.small_left_arrow_selected,
                                      category_l_clicked,
                                      (x + 422),
                                      (y + 54))

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
                        category_r_button,
                        category_l_button,
                        stats_button,
                        equip_button]

    def update_player_cache(self):
        self.player_cache = {"All": [],
                             "Weapons": [],
                             "Armor": [],
                             "Misc": []}
        for each in self.player.items["Weapon"]:
            self.player_cache["Weapons"].append((each, "Weapon", self.player.items["Weapon"].index(each)))
            self.player_cache["All"].append((each, "Weapon", self.player.items["Weapon"].index(each)))
        for each in self.player.items["Armor"]:
            self.player_cache["Armor"].append((each, "Armor", self.player.items["Armor"].index(each)))
            self.player_cache["All"].append((each, "Armor", self.player.items["Armor"].index(each)))
        for each in self.player.items["Misc"]:
            self.player_cache["Misc"].append((each, "Misc", self.player.items["Misc"].index(each)))
            self.player_cache["All"].append((each, "Misc", self.player.items["Misc"].index(each)))

    def draw_buff_box(self, mouse_pos):
        tiny_font = pygame.font.SysFont('Sitka', 12, True, False)
        equipped_items = []
        for key in self.player.equipped:
            equipped_items.append(self.player.equipped[key])
        melee_buff_list = []
        for each in equipped_items:
            if hasattr(each, 'melee_damage') and each.melee_damage > 0:
                melee_buff_list.append((each.melee_damage, each.name))
        ranged_buff_list = []
        for each in equipped_items:
            if hasattr(each, 'ranged_damage') and each.ranged_damage > 0:
                ranged_buff_list.append((each.ranged_damage, each.name))
        armor_buff_list = []
        for each in equipped_items:
            if hasattr(each, 'armor_value') and each.armor_value > 0:
                armor_buff_list.append((each.armor_value, each.name))
        block_buff_list = []

        box_height = (14 * (len(melee_buff_list) + 1) +
                      14 * (len(ranged_buff_list) + 1) +
                      14 * (len(armor_buff_list) + 1) +
                      14 * (len(block_buff_list) + 1) +
                      4)
        background_fill = pygame.Rect(mouse_pos[0],
                                      mouse_pos[1] - box_height,
                                      220,
                                      box_height)
        background_stroke = pygame.Rect(mouse_pos[0],
                                        mouse_pos[1] - box_height,
                                        220,
                                        box_height)
        pygame.draw.rect(self.screen, (0, 0, 0), background_fill)
        pygame.draw.rect(self.screen, (255, 255, 255), background_stroke, 1)
        count = 0
        list_count = 0
        buff_lists = [melee_buff_list, ranged_buff_list, block_buff_list, armor_buff_list]
        buff_strings = ["Melee", "Ranged", "Block", "Armor"]
        for buff_list in buff_lists:
            buff_type_stamp = tiny_font.render("{0}".format(buff_strings[list_count]), True, utilities.colors.dark_green)
            self.screen.blit(buff_type_stamp, [mouse_pos[0] + 4, -(box_height) + mouse_pos[1] + 2 + (count + list_count) * 14])
            for each in buff_list:
                stamp = tiny_font.render("{0} (+{1})".format(each[1], each[0]), True, utilities.colors.light_green)
                self.screen.blit(stamp, [mouse_pos[0] + 20, -(box_height) + mouse_pos[1] + 2 + (count + list_count + 1) * 14])
                count += 1
            list_count += 1

    def draw_icons(self):
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

    def menu_onscreen(self):
        player_selection_box = pygame.sprite.Sprite()
        font = pygame.font.SysFont('Sitka', 26, True, False)
        small_font = pygame.font.SysFont('Sitka', 18, True, False)
        self.update_player_cache()

        while self.open:
            active_player_list = self.player_cache[self.categories[self.current_category]]
            player_visible_items = active_player_list[self.player_list_top:self.player_list_top + 14]
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
                        if self.player_list_top + 14 < len(self.player_cache[self.categories[self.current_category]]):
                            self.player_list_top += 1
                    else:
                        count = 0
                        spacer = 18
                        for each in player_visible_items:
                            x1 = self.background_pane.rect.left + 405
                            x2 = x1 + 170
                            y1 = (self.background_pane.rect.top + 84 + (count * spacer))
                            y2 = y1 + 19
                            if utilities.check_if_inside(x1, x2, y1, y2, mouse_pos):
                                if count + self.player_list_top <= len(active_player_list):
                                    self.player_selected = count + self.player_list_top
                            count += 1
                    if active_player_list:
                        self.player_selected_tuple = active_player_list[self.player_selected]
                    else:
                        print("empty list")

                    for button in self.buttons:
                        if utilities.check_if_inside(button.sprite.rect.x,
                                                     button.sprite.rect.right,
                                                     button.sprite.rect.y,
                                                     button.sprite.rect.bottom,
                                                     mouse_pos):
                            button.click()

            player_selection_box.image = pygame.Rect(self.background_pane.rect.left + 396,
                                                     self.background_pane.rect.top + 84 + ((self.player_selected - self.player_list_top) * 18),
                                                     276,
                                                     19)

            self.render_buttons(mouse_pos)

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
            self.screen.blit(font.render(self.categories[self.current_category], True, utilities.colors.border_gold),
                             [self.background_pane.rect.left + 450, self.background_pane.rect.top + 54])
            for each in stat_stamps:
                string = each[0]
                left_spacer = each[1]
                top_spacer = each[2]
                self.screen.blit(small_font.render(string, True, utilities.colors.border_gold),
                                 [self.background_pane.rect.left + left_spacer, self.background_pane.rect.top + top_spacer])

            self.draw_icons()

            spacer = 18
            count = 0
            for each in player_visible_items:
                value_stamp = small_font.render(str(each[0].value), True, utilities.colors.border_gold)
                weight_stamp = small_font.render(str(each[0].weight), True, utilities.colors.border_gold)

                if each[0].is_equipped:
                    color = utilities.colors.equipped_item_red
                else:
                    color = utilities.colors.border_gold
                name_stamp = small_font.render(each[0].name, True, color)

                self.screen.blit(value_stamp, [self.background_pane.rect.left + 320,
                                               self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(weight_stamp, [self.background_pane.rect.left + 370,
                                                self.background_pane.rect.top + 84 + (count * spacer)])
                self.screen.blit(name_stamp, [self.background_pane.rect.left + 400,
                                              self.background_pane.rect.top + 84 + (count * spacer)])
                count += 1
            if self.player_selected >= self.player_list_top and self.player_selected <= self.player_list_top + 14:
                pygame.draw.rect(self.screen, (255, 198, 13), player_selection_box.image, 1)
            if utilities.check_if_inside(self.background_pane.rect.x + 148,
                                         self.background_pane.rect.x + 307,
                                         self.background_pane.rect.y + 45,
                                         self.background_pane.rect.y + 343,
                                         mouse_pos):
                self.draw_buff_box(mouse_pos)
            pygame.display.flip()


