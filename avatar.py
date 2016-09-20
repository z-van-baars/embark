import pygame
import entity
import utilities
import navigate
import ui
import spritesheet

pygame.init()
pygame.display.set_mode([0, 0])


class Avatar(entity.Entity):
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

        self.speed = 10
        self.bag = None
        self.accuracy = 60
        self.attack = 10
        self.health = 100
        self.max_health = 100
        self.gold = 100
        self.actions = ["None",
                        "Move",
                        "Shooting an interactible",
                        "Moving to interactible"]
        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_helmet = None
        self.action = 0
        self.target_type = 0
        self.fighting = False
        self.walk_frame_number = 0
        self.fight_frame = 0

        self.set_images()

    def expire(self):
        self.current_tile.entity_group["Avatar"].remove(self)
        self.current_map.entity_group["Avatar"].remove(self)

    def set_frame(self, action):
        if action == 0:
            if self.fighting:
                if self.fight_frame > 0:
                    self.fight_frame += 1
                if self.fight_frame > 21:
                    self.fight_frame = 0
                self.sprite.image = self.melee_fight_frames[self.fight_frame]
                if self.equipped_weapon:
                    if not self.equipped_weapon.ranged:
                        self.equipped_weapon.set_frame(self.fight_frame)
                        self.sprite.image.blit(self.equipped_weapon.sprite.image, [0, -40])
                    else:
                        self.sprite.image.blit(self.equipped_weapon.sprite.image, [0, 0])
            else:
                self.walk_frame_number = 0
                self.sprite.image = self.rest_frame
                if self.equipped_weapon:
                    if not self.equipped_weapon.ranged:
                        self.equipped_weapon.set_frame(0)
                        self.sprite.image.blit(self.equipped_weapon.sprite.image, [0, -40])
                    else:
                        self.sprite.image.blit(self.equipped_weapon.sprite.image, [0, 0])
        elif action == 1 or action == 3:
            self.walk_frame_number += 1
            if self.walk_frame_number > len(self.walking_frames) - 1:
                self.walk_frame_number = 0
            self.sprite.image = self.walking_frames[self.walk_frame_number]
            if self.equipped_weapon:
                if not self.equipped_weapon.ranged:
                    self.equipped_weapon.set_frame(0)
                    self.sprite.image.blit(self.equipped_weapon.sprite.image, [0, -40])
                else:
                    self.sprite.image.blit(self.equipped_weapon.sprite.image, [0, 0])

        elif action == 2:
            if self.fight_frame > 0:
                self.fight_frame += 1
            if self.fight_frame > 21:
                self.fight_frame = 0
            self.sprite.image = self.ranged_fight_frames[self.fight_frame]

    def set_images(self):
        self.healthbar = ui.HealthBar(self.current_map, self.tile_x, self.tile_y, self.health, self.max_health)
        self.current_map.healthbars.append(self.healthbar)
        self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        avatar_spritesheet = spritesheet.Spritesheet("art/avatar/avatar.png")
        self.rest_frame = avatar_spritesheet.get_image(0, 0, 20, 40)
        self.walking_frames = [avatar_spritesheet.get_image(20, 0, 20, 40),
                               avatar_spritesheet.get_image(20, 0, 20, 40),
                               avatar_spritesheet.get_image(20, 0, 20, 40),
                               avatar_spritesheet.get_image(20, 0, 20, 40),
                               avatar_spritesheet.get_image(20, 0, 20, 40),
                               avatar_spritesheet.get_image(40, 0, 20, 40),
                               avatar_spritesheet.get_image(40, 0, 20, 40),
                               avatar_spritesheet.get_image(40, 0, 20, 40),
                               avatar_spritesheet.get_image(40, 0, 20, 40),
                               avatar_spritesheet.get_image(40, 0, 20, 40),
                               avatar_spritesheet.get_image(60, 0, 20, 40),
                               avatar_spritesheet.get_image(60, 0, 20, 40),
                               avatar_spritesheet.get_image(60, 0, 20, 40),
                               avatar_spritesheet.get_image(60, 0, 20, 40),
                               avatar_spritesheet.get_image(60, 0, 20, 40),
                               avatar_spritesheet.get_image(80, 0, 20, 40),
                               avatar_spritesheet.get_image(80, 0, 20, 40),
                               avatar_spritesheet.get_image(80, 0, 20, 40),
                               avatar_spritesheet.get_image(80, 0, 20, 40),
                               avatar_spritesheet.get_image(80, 0, 20, 40)]
        self.melee_fight_frames = []
        for x in range(3):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(0, 80, 20, 40))
        for x in range(3):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(20, 80, 20, 40))
        for x in range(3):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(40, 80, 20, 40))
        for x in range(4):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(60, 80, 20, 40))
        for x in range(4):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(80, 80, 40, 40))
        for x in range(5):
            self.melee_fight_frames.append(avatar_spritesheet.get_image(120, 80, 40, 40))

        self.ranged_fight_frames = []
        for x in range(3):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(0, 160, 40, 40))
        for x in range(4):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(40, 160, 40, 40))
        for x in range(5):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(80, 160, 40, 40))
        for x in range(3):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(120, 160, 40, 40))
        for x in range(3):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(160, 160, 40, 40))
        for x in range(4):
            self.ranged_fight_frames.append(avatar_spritesheet.get_image(0, 160, 40, 40))

        self.sprite.image = avatar_spritesheet.get_image(0, 0, 20, 40)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def tick_cycle(self):
        self.set_frame(self.action)
        my_position = (self.tile_x, self.tile_y)
        self.age += 1
        self.time_since_last_move += 1
        health_roll_1 = utilities.roll_dice(1, 10)
        health_roll_2 = utilities.roll_dice(1, 10)
        health_roll_2 = utilities.roll_dice(1, 10)
        health_roll = min(health_roll_1, health_roll_2, health_roll_2)
        if self.healthbar.active:
            self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        if health_roll > 9:
            self.health += 1
        if self.health > self.max_health:
            self.health = self.max_health
        if self.action == 0:
            pass
        elif self.action == 1:
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.change_x, self.change_y = self.calculate_step(my_position, self.target_object, self.target_coordinates)
                self.move()
        elif self.action == 2:
            if self.time_since_last_attack >= self.speed * 10:
                self.fight_frame = 1
                self.time_since_last_attack = 0
                target_tile = self.current_map.game_tile_rows[self.target_coordinates[1]][self.target_coordinates[0]]
                self.equipped_weapon.fire(self.current_map, self.tile_x, self.tile_y, self.target_object)
            self.time_since_last_attack += 1
        elif self.action == 3:
            if not self.target_object.tile_x == self.target_coordinates[0] or not self.target_object.tile_y == self.target_coordinates[1]:
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.change_x, self.change_y = self.calculate_step(my_position, self.target_object, self.target_coordinates)
                self.move()
            if not self.path:
                # is the target still there?
                statement = "used " + self.target_object.display_name
                print(statement)
                self.target_object.activated = True

    def assign_target(self, game_state, current_map, mouse_pos):
        my_position = (self.tile_x, self.tile_y)
        tile_x = int((mouse_pos[0] - current_map.x_shift) / 20)
        tile_y = int((mouse_pos[1] - current_map.y_shift) / 20)
        # 0 == invalid (cant move there and wont process the click)
        # 1 == empty space, will move to this spot
        # 2 == interactible thing, door, chest, creature, npc - will path to this object and then interact
        self.target_type = 0
        if utilities.within_map(tile_x, tile_y, current_map):
            if current_map.game_tile_rows[tile_y][tile_x].is_occupied():
                for group in current_map.game_tile_rows[tile_y][tile_x].entity_group:
                    if current_map.game_tile_rows[tile_y][tile_x].entity_group[group]:
                        for each in current_map.game_tile_rows[tile_y][tile_x].entity_group[group]:
                            if each.interactable:
                                new_context_menu = ui.ContextMenu(game_state, mouse_pos, each)
                                pygame.draw.rect(new_context_menu.screen, (255, 255, 255), new_context_menu.tile_selector_graphic.image, 1)
                                new_context_menu.menu_onscreen()

            else:
                new_context_menu = ui.ContextMenu(game_state, mouse_pos)
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
            self.action = 1
        elif target_type == 2:
            if self.equipped_weapon and self.equipped_weapon.ranged:
                self.target_coordinates = tile_x, tile_y
                self.fighting = True
                self.action = 2
            else:
                self.target_coordinates = tile_x, tile_y
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
                self.target_coordinates = tile_x, tile_y
                self.action = 3

    def calculate_step(self, my_position, target_object, target_coordinates):
        change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
        if self.path.tiles[0].is_occupied():
            self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
            change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
        return change_x, change_y

    def check_tile(self, x_change, y_change):
        x = self.tile_x
        y = self.tile_y
        x = x + x_change
        y = y + y_change
        if x < 0 or x > len(self.current_map.game_tile_rows[0]):
            return False
        if y < 0 or y > len(self.current_map.game_tile_rows):
            return False

        tile = self.current_map.game_tile_rows[y][x]
        if tile.is_occupied():
            return False
        else:
            return True

    def move(self):
        self.tile_x += self.change_x
        if self.tile_x < 0:
            self.tile_x = 0
        elif self.tile_x >= self.current_map.number_of_columns:
            self.tile_x = self.current_map.number_of_columns - 1
        self.tile_y += self.change_y
        if self.tile_y < 0:
            self.tile_y = 0
        elif self.tile_y >= self.current_map.number_of_rows:
            self.tile_y = self.current_map.number_of_rows - 1

        self.assign_tile()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20
        self.change_x = 0
        self.change_y = 0

        # am I at my target?
        if len(self.path.tiles) == 2 and self.action == 3:
           self.target_coordinates = None
           self.path = None
           self.action = 0
        elif len(self.path.tiles) < 2 and self.action == 1:
            self.target_coordinates = None
            self.path = None
            self.action = 0
        else:
            self.path.tiles.pop(0)

        self.current_map.scroll_check(self.sprite.rect.x, self.sprite.rect.y)
