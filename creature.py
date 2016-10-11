import entity
import utilities
import navigate
import random
import pygame
import ui
import art
import combat
from entity import Action

pygame.init()
pygame.display.set_mode([0, 0])


class Creature(entity.SentientEntity):
    my_type = "Creature"
    ranged = False

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.target_coordinates = None
        self.target_object = None
        self.path = None
        self.search_area_graphic = None
        self.activated = False
        self.action = Action.idle
        self.fighting = False
        self.time_since_last_move = 0
        self.equipped_weapon = None

    def pursue_player(self, player, player_coordinates):
        my_position = (self.tile_x, self.tile_y)
        if not self.target_coordinates:
            self.target_coordinates = player_coordinates
            self.target_object = player
        self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)


class Skeleton(Creature):
    occupies_tile = True
    interactable = True
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.speed = 10
        self.accuracy = 40
        self.strength = 5
        self.melee_damage = 1
        self.health = 50
        self.max_health = 50
        self.sight_range = 10

        self.time_since_last_attack = 0
        self.post = (self.tile_x, self.tile_y)
        self.fight_frame = 0
        self.display_name = "Spoopy Skellington"
        self.set_images()

    def set_images(self):
        self.healthbar = ui.HealthBar(self.current_map, self.tile_x, self.tile_y, self.health, self.max_health)
        self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        self.sprite.image = art.skeleton_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def tick_cycle(self, player, player_coordinates):
        self.age += 1
        if self.health <= 0:
            self.expire()
        else:
            self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
            self.time_since_last_move += 1
            if self.health < self.max_health:
                self.healthbar.active = True
        #if not self.fighting:
            #self.idle()

    def idle(self):
        my_position = (self.tile_x, self.tile_y)
        if not self.target_coordinates:
            action = random.randint(0, 1000)
            if action >= 100:
                self.target_coordinates = self.choose_random_target_tile(self.current_map)
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
        else:
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.change_x, self.change_y = navigate.calculate_step(my_position, self.path.tiles[0])
                if self.path.tiles[0].is_occupied():
                    print("occupado")
                    self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
                    self.change_x, self.change_y = navigate.calculate_step(my_position, self.path.tiles[0])
                self.move()

    def use(self, game_state):
        self.fighting = True
        player = game_state.player
        player.fighting = True
        player.healthbar.active = True
        self.healthbar.active = True


class GrieveBeast(Creature):
    occupies_tile = True
    interactable = True
    footprint = (2, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.speed = 10
        self.accuracy = 40
        self.strength = 6
        self.melee_damage = 3
        self.health = 100
        self.max_health = 100
        self.sight_range = 14

        self.time_since_last_attack = 0
        self.post = (self.tile_x, self.tile_y)
        self.fight_frame = 0
        self.display_name = "Grievebeast"
        self.set_images()

    def set_images(self):
        self.healthbar = ui.HealthBar(self.current_map, self.tile_x, self.tile_y, self.health, self.max_health)
        self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        self.sprite.image = art.grievebeast_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def tick_cycle(self, player, player_coordinates):
        self.age += 1
        if self.health <= 0:
            self.expire()
        else:
            self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
            self.time_since_last_move += 1
            if self.health < self.max_health:
                self.healthbar.active = True

    def use(self, game_state):
        self.fighting = True
        player = game_state.player
        player.fighting = True
        player.healthbar.active = True
        self.healthbar.active = True


class ShadeBrute(Creature):
    occupies_tile = True
    interactable = True
    footprint = (1, 1)
    height = 2

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)
        self.speed = 10
        self.accuracy = 30
        self.strength = 6
        self.melee_damage = 3
        self.health = 80
        self.max_health = 80
        self.sight_range = 8

        self.time_since_last_attack = 0
        self.post = (self.tile_x, self.tile_y)
        self.fight_frame = 0
        self.display_name = "Shadebrute"
        self.walk_frame_number = 0
        self.set_images()

    def set_images(self):
        self.healthbar = ui.HealthBar(self.current_map, self.tile_x, self.tile_y, self.health, self.max_health)
        self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        self.rest_frame = art.shadebrute_spritesheet.get_image(0, 0, 20, 40)
        self.walking_frames = [art.shadebrute_spritesheet.get_image(20, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(20, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(20, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(20, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(20, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(40, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(40, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(40, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(40, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(40, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(60, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(60, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(60, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(60, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(60, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(80, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(80, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(80, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(80, 0, 20, 40),
                               art.shadebrute_spritesheet.get_image(80, 0, 20, 40)]
        self.sprite.image = self.rest_frame
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def set_frame(self, action):
        self.set_action_sprite(action)


    def set_action_sprite(self, action):
        if action == Action.move or action == Action.attack:
            self.walk_frame_number += 1
            if self.walk_frame_number > len(self.walking_frames) - 1:
                self.walk_frame_number = 0
            self.sprite.image = self.walking_frames[self.walk_frame_number]
        else:
            self.sprite.image = self.rest_frame


    def tick_cycle(self, player, player_coordinates):

        self.time_since_last_attack += 1
        self.time_since_last_move += 1
        self.age += 1
        if self.health <= 0:
            self.expire()
        self.healthbar.get_state(self.health, self.tile_x, self.tile_y)
        if self.health < self.max_health:
            self.healthbar.active = True
            self.action = Action.attack
            self.target_coordinates = player_coordinates
            self.target_object = player
        target = self.target_object
        target_coordinates = self.target_coordinates
        my_coordinates = (self.tile_x, self.tile_y)

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

        self.set_frame(self.action)

    def use(self, game_state):
        self.fighting = True
        player = self.current_map.entity_group["Avatar"][0]
        player.fighting = True
        player.healthbar.active = True
        self.healthbar.active = True
        self.activated = False


class Buffalo(Creature):
    occupies_tile = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)

        buffalo_image_1 = pygame.image.load("art/buffalo/buffalo_1.png").convert()
        buffalo_image_1.set_colorkey(utilities.colors.key)

        self.display_name = "Buffalo"
        self.speed = 10
        self.current_hunger_saturation = 20000
        self.hunger_threshold = 35000
        self.max_hunger_saturation = 40000
        self.sight_range = 10
        self.bite_size = 5
        self.ticks_without_eating = 0
        self.sprite.image = buffalo_image_1
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20

    def tick_cycle(self):
        self.age += 1
        self.current_hunger_saturation -= 1
        self.time_since_last_move += 1

        if self.current_hunger_saturation < self.hunger_threshold:
            self.change_x, self.change_y = self.solve_hunger((self.tile_x, self.tile_y))
        else:
            self.secondary_behavior()

        if not self.eating:
            if self.time_since_last_move >= self.speed:
                self.time_since_last_move = 0
                self.move()
        self.starvation_check()

    def solve_hunger(self, my_position):
        '''because of what I have in mind, it could end up doing activities that are a bit abstracted from gathering food
        but bottomline is: the end result will be different than if it started from a position of no hunger'''
        self.eating = False
        self.ticks_without_eating += 1
        if self.current_tile.entity_group["Flora"] and self.ticks_without_eating > 30:
            self.eat()
            return 0, 0
        else:
            # Runs too often - needs better conditionals
            if not self.target_coordinates:
                self.target_object, self.target_coordinates = self.choose_target(self.current_map, my_position)

            if not self.path or len(self.path.tiles) < 1:
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
                if len(self.path.tiles) < 2:
                    self.target_object, self.target_coordinates = self.choose_target(self.current_map, my_position)
                    self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)

            change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            if self.path.tiles[0].is_occupied():
                self.path, self.target_coordinates = navigate.get_path(my_position, self.current_map, self.target_coordinates)
                change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
            return change_x, change_y

    def secondary_behavior(self):
        self.idle()

    def choose_target(self, current_map, my_position):
        nearby_food = self.find_local_food(current_map)
        if nearby_food:
            target_object = random.choice(nearby_food)
            target_coordinates = (target_object.tile_x, target_object.tile_y)
        else:
            target_coordinates = self.choose_random_target(current_map, my_position)
            target_object = None
        assert my_position != target_coordinates
        return target_object, target_coordinates

    def idle(self):
        action = random.randint(0, 900)
        if action <= 10:
            self.change_x = 1
        elif 10 < action <= 20:
            self.change_x = -1
        elif 20 < action <= 30:
            self.change_y = 1
        elif 30 < action <= 40:
            self.change_y = -1
        elif action > 750:
            self.change_x = 0
            self.change_y = 0
