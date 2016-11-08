import pygame
import entity
import utilities
import navigate
import ui
import spritesheet
import combat
from entity import Action

pygame.init()
pygame.display.set_mode([0, 0])


class Avatar(entity.SentientEntity):
    occupies_tile = True
    interactable = False
    my_type = "Avatar"
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y + 1, current_map)
        self.display_name = "PLAYER"

        self.change_x = 0
        self.change_y = 0
        self.target_coordinates = None
        self.target_object = None
        self.path = None
        self.time_since_last_move = 0
        self.time_since_last_attack = 0

        self.speed = 5
        self.accuracy = 60
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.strength = 10
        self.willpower = 10
        self.agility = 10

        self.archery = 1
        self.attack = 1
        self.combat_magic = 1
        self.healing_magic = 1

        self.sell_multiplier = 0.7
        self.buy_multiplier = 1.3

        self.armor = 0
        self.melee_damage = 0
        self.ranged_damage = 0
        self.block = 0

        self.items = {"Weapon": [],
                      "Armor": [],
                      "Misc": []}
        self.gold = 100
        self.action = Action.idle
        self.target_type = 0
        self.fighting = False
        self.walk_frame_number = 0
        self.fight_frame = 0

        self.set_images(self.image_key)

    def set_frame(self, action):
        self.set_action_sprite(action)
        if self.equipped["Weapon"]:
            self.set_weapon_sprite(action)
        if self.equipped["Body Armor"]:
            self.set_armor_sprite(action, self.equipped["Body Armor"])
        if self.equipped["Boots"]:
            self.set_armor_sprite(action, self.equipped["Boots"])
        if self.equipped["Helmet"]:
            self.set_armor_sprite(action, self.equipped["Helmet"])
        if self.equipped["Gloves"]:
            self.set_armor_sprite(action, self.equipped["Gloves"])

    def set_action_sprite(self, action):
        if self.equipped["Weapon"]:
            weapon_range = self.equipped["Weapon"].range
        else:
            weapon_range = 1.5
        if action == Action.idle:
            if self.fighting:
                if self.fight_frame > 0:
                    self.fight_frame += 1
                if self.fight_frame > 21:
                    self.fight_frame = 0
                self.sprite.image = self.melee_fight_frames[self.fight_frame]
            else:
                self.walk_frame_number = 0
                self.sprite.image = self.rest_frame
        elif action == Action.move or action == Action.use:
            self.walk_frame_number += 1
            if self.walk_frame_number > len(self.walk_frames) - 1:
                self.walk_frame_number = 0
            self.sprite.image = self.walk_frames[self.walk_frame_number]
        elif action == Action.attack:
            if self.fight_frame > 1:
                self.fight_frame += 1
                if self.fight_frame > 21:
                    self.fight_frame = 1
                if self.equipped["Weapon"].ranged:
                    self.sprite.image = self.ranged_fight_frames[self.fight_frame]
                else:
                    self.sprite.image = self.melee_fight_frames[self.fight_frame]
            else:
                if self.within_range((self.tile_x, self.tile_y), self.target_coordinates, weapon_range):
                    self.walk_frame_number = 0
                else:
                    self.walk_frame_number += 1
                if self.walk_frame_number > len(self.walk_frames) - 1:
                    self.walk_frame_number = 0
                self.sprite.image = self.walk_frames[self.walk_frame_number]

    def set_weapon_sprite(self, action):
        if action == Action.idle:
            self.equipped["Weapon"].set_frame(0)
        elif action == Action.move or action == Action.use:
            self.equipped["Weapon"].set_frame(0)
        elif action == Action.attack:
            self.equipped["Weapon"].set_frame(self.fight_frame - 1)

    def set_armor_sprite(self, action, armor):
        if action == Action.idle:
            self.equipped[armor.armor_type].set_frame(0, 0)
        elif action == Action.move or action == Action.use:
            self.equipped[armor.armor_type].set_frame(self.walk_frame_number, 0)
        elif action == Action.attack:
            if self.has_ranged_attack():
                self.equipped[armor.armor_type].set_frame(self.fight_frame - 1, 2)
            else:
                self.equipped[armor.armor_type].set_frame(self.fight_frame - 1, 1)

    def set_images(self, image_key):
        self.healthbar = ui.HealthBar(self.current_map, self.tile_x, self.tile_y, self.health, self.max_health)
        self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        avatar_spritesheet = spritesheet.Spritesheet("art/avatar/avatar.png")
        self.rest_frame = avatar_spritesheet.get_image(0, 0, 20, 40).convert_alpha()
        self.walk_frames = [avatar_spritesheet.get_image(0, 0, 20, 40).convert_alpha()]
        for x in range(5):
            self.walk_frames.append(avatar_spritesheet.get_image(20, 0, 20, 40).convert_alpha())
        for x in range(5):
            self.walk_frames.append(avatar_spritesheet.get_image(60, 0, 20, 40).convert_alpha())
        for x in range(5):
            self.walk_frames.append(avatar_spritesheet.get_image(80, 0, 20, 40).convert_alpha())
        for x in range(5):
            self.walk_frames.append(avatar_spritesheet.get_image(100, 0, 20, 40).convert_alpha())
        for x in range(5):
            self.walk_frames.append(avatar_spritesheet.get_image(120, 0, 20, 40).convert_alpha())
        for x in range(5):
            self.walk_frames.append(avatar_spritesheet.get_image(140, 0, 20, 40).convert_alpha())
        self.melee_fight_frames = []
        for x in range(3):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(0, 80, 20, 40).convert_alpha())
        for x in range(3):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(20, 80, 20, 40).convert_alpha())
        for x in range(3):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(40, 80, 20, 40).convert_alpha())
        for x in range(4):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(60, 80, 20, 40).convert_alpha())
        for x in range(4):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(80, 80, 40, 40).convert_alpha())
        for x in range(5):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(120, 80, 40, 40).convert_alpha())

        self.ranged_fight_frames = []
        for x in range(1):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(0, 160, 40, 40).convert_alpha())
        for x in range(6):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(40, 160, 40, 40).convert_alpha())
        for x in range(6):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(80, 160, 40, 40).convert_alpha())
        for x in range(4):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(120, 160, 40, 40).convert_alpha())
        for x in range(3):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(160, 160, 40, 40).convert_alpha())
        for x in range(4):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(0, 160, 40, 40).convert_alpha())

        self.sprite.image = avatar_spritesheet.get_image(0, 0, 20, 40).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def recover_health(self):
        health_roll_1 = utilities.roll_dice(1, 10)
        health_roll_2 = utilities.roll_dice(1, 10)
        health_roll_2 = utilities.roll_dice(1, 10)
        health_roll = min(health_roll_1, health_roll_2, health_roll_2)
        self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        if health_roll > 9:
            self.health += 1
        if self.health >= self.max_health:
            self.health = self.max_health
            self.healthbar.active = False
        else:
            self.healthbar.active = True

    def tick_cycle(self, game_state):
        my_coordinates = (self.tile_x, self.tile_y)
        target = self.target_object
        target_coordinates = self.target_coordinates
        self.age += 1
        self.time_since_last_move += 1
        self.time_since_last_attack += 1
        self.recover_health()

        if self.action == Action.idle:
            pass
        elif self.action == Action.move:
            self.moving(my_coordinates, target, target_coordinates)
        elif self.action == Action.attack:
            if target.health > 0:
                self.attacking(my_coordinates, target_coordinates, target)
            else:
                self.clear_target()
                self.action = Action.idle
        elif self.action == Action.use:
            self.using(game_state, my_coordinates, target_coordinates, target)

        self.current_map.scroll_check(self.sprite.rect.x, self.sprite.rect.y)
        self.set_frame(self.action)

    def assign_target(self, game_state, current_map, mouse_pos):
        my_position = (self.tile_x, self.tile_y)
        tile_x = int((mouse_pos[0] - current_map.x_shift) / 20)
        tile_y = int((mouse_pos[1] - current_map.y_shift) / 20)
        # 0 == invalid (cant move there and wont process the click)
        # 1 == empty space, will move to this spot
        # 2 == interactible thing, door, chest, npc - will path to this object and then interact
        # 3 == attackable creature, will attempt to attack or path to move within range
        self.target_type = 0
        if utilities.within_map(tile_x, tile_y, current_map):
            if current_map.game_tile_rows[tile_y][tile_x].is_occupied():
                for group in current_map.game_tile_rows[tile_y][tile_x].entity_group:
                    if current_map.game_tile_rows[tile_y][tile_x].entity_group[group]:
                        for each in current_map.game_tile_rows[tile_y][tile_x].entity_group[group]:
                            if each.interactable:
                                new_context_menu = ui.ContextMenu(game_state, mouse_pos, each, each.my_type)
                                pygame.draw.rect(new_context_menu.screen, (255, 255, 255), new_context_menu.tile_selector_graphic.image, 1)
                                new_context_menu.menu_onscreen()

            else:
                new_context_menu = ui.ContextMenu(game_state, mouse_pos, None, "Open")
                pygame.draw.rect(new_context_menu.screen, (255, 255, 255), new_context_menu.tile_selector_graphic.image, 1)
                new_context_menu.menu_onscreen()

        self.get_path_behavior(current_map, my_position, tile_x, tile_y, self.target_type)

    def get_path_behavior(self, current_map, my_position, tile_x, tile_y, target_type):
        ## target_type can be (0) blocked tile (1) empty tile and (2) interactible tile

        if target_type == 0:
            pass
        elif target_type == 1:
            self.target_coordinates = tile_x, tile_y
            self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
            self.action = Action.move
        elif target_type == 2:
            self.target_coordinates = tile_x, tile_y
            self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
            self.target_coordinates = tile_x, tile_y
            self.action = Action.use
        elif target_type == 3:
            self.target_coordinates = tile_x, tile_y
            self.fighting = True
            self.action = Action.attack
            self.fight_frame = 1
