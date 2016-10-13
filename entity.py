import pygame
import utilities
from enum import Enum
import combat
import navigate


class Action(Enum):
    idle = 0
    move = 1
    attack = 2
    use = 3


class Entity(object):
    occupies_tile = False
    gateway = False

    def __init__(self, x, y, current_map):
        super().__init__()
        self.tile_x = x
        self.tile_y = y
        self.current_map = current_map
        self.current_tile = None
        self.age = 0
        self.sprite = pygame.sprite.Sprite()
        self.display_name = "-N/A-"

        self.current_map.entity_group[self.my_type].append(self)
        self.assign_tile()

    def __lt__(self, other):
        if self.tile_x < other.tile_x:
            return True
        elif self.tile_y < other.tile_y:
            return True
        else:
            return False

    def expire(self):
        self.leave_tile()
        self.current_map.entity_group[self.my_type].remove(self)
        self.current_map = None

    def assign_tile(self):
        if self.current_tile:
            self.leave_tile()

        self.current_tile = self.current_map.game_tile_rows[self.tile_y][self.tile_x]
        initial_x = self.tile_x
        initial_y = self.tile_y - (self.footprint[1] - 1)
        for tile_y in range(initial_y, initial_y + (self.footprint[1])):
            for tile_x in range(initial_x, initial_x + self.footprint[0]):
                tile = self.current_map.game_tile_rows[tile_y][tile_x]
                tile.entity_group[self.my_type].append(self)

    def leave_tile(self):
        initial_x = self.current_tile.column
        initial_y = self.current_tile.row - (self.footprint[1] - 1)
        for tile_y in range(initial_y, initial_y + (self.footprint[1])):
            for tile_x in range(initial_x, initial_x + self.footprint[0]):
                tile = self.current_map.game_tile_rows[tile_y][tile_x]
                tile.entity_group[self.my_type].remove(self)
        self.current_tile = None

    def assign_map(self, new_map):
        if self.current_map is not None:
            self.current_map.entity_group[self.my_type].remove(self)
        self.current_map = new_map
        if self.healthbar:
            self.current_map.healthbars.append(self.healthbar)

        self.current_map.entity_group[self.my_type].append(self)


class MovingEntity(Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)


class SentientEntity(MovingEntity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)

    def expire(self):
        self.leave_tile()
        self.current_map.entity_group[self.my_type].remove(self)
        if self.healthbar:
            self.current_map.healthbars.remove(self.healthbar)
        self.current_map = None

    def clear_target(self):
        self.target_coordinates = None
        self.target_object = None

    def has_ranged_attack(self):
        if self.equipped_weapon:
            return self.equipped_weapon.ranged
        return False

    def melee_attack(self, attack_timer, accuracy, speed, target):
        if attack_timer > speed * 5:
            self.time_since_last_attack = 0
            accuracy_roll_1 = utilities.roll_dice(2, accuracy)
            accuracy_roll_2 = utilities.roll_dice(2, accuracy)
            accuracy_roll = min(accuracy_roll_1, accuracy_roll_2)
            if accuracy_roll < accuracy * 0.7:
                combat.strike(self, target)
            self.fight_frame = 2

    def ranged_attack(self, my_coordinates, attack_timer, weapon, accuracy, speed, target):
        if attack_timer >= speed * 10:
            self.fight_frame = 2
            self.time_since_last_attack = 0
            weapon.fire(self.current_map, my_coordinates[0], my_coordinates[1], target)
        attack_timer += 1

    def within_range(self, my_coordinates, target_coordinates, weapon_range):
        if utilities.distance(my_coordinates[0], my_coordinates[1], target_coordinates[0], target_coordinates[1]) < weapon_range:
            return True
        else:
            return False

    def using(self, game_state, my_coordinates, target_coordinates, target):
        self.moving(my_coordinates, target, target_coordinates)
        if utilities.distance(self.target_coordinates[0],
                              self.target_coordinates[1],
                              my_coordinates[0],
                              my_coordinates[1]) < 1.5:
            self.target_object.use(game_state)
            self.action = Action.idle

    def attacking(self, my_coordinates, target_coordinates, target):
        attack_timer = self.time_since_last_attack
        accuracy = self.accuracy
        if self.equipped_weapon:
            speed = self.equipped_weapon.attack_speed
            weapon_range = 1.5
        else:
            speed = self.speed
            weapon_range = 1.5
        if self.has_ranged_attack():
            weapon_range = self.equipped_weapon.range
            if self.within_range(my_coordinates, target_coordinates, weapon_range):
                self.ranged_attack(my_coordinates, attack_timer, self.equipped_weapon, accuracy, speed, target)
            else:
                self.moving(my_coordinates, target, target_coordinates)
        else:
            if self.within_range(my_coordinates, target_coordinates, weapon_range):
                self.melee_attack(attack_timer, accuracy, speed, target)
            else:
                self.moving(my_coordinates, target, target_coordinates)

    def moving(self, my_coordinates, target, target_coordinates):
        if self.time_since_last_move >= self.speed:
            self.time_since_last_move = 0
            change_x, change_y = self.calculate_step(my_coordinates, target, target_coordinates)
            self.move(change_x, change_y)
        if utilities.distance(self.target_coordinates[0],
                              self.target_coordinates[1],
                              my_coordinates[0],
                              my_coordinates[1]) < 1:
                self.action = Action.idle

    def move(self, change_x, change_y):
        self.tile_x += change_x
        if self.tile_x < 0:
            self.tile_x = 0
        elif self.tile_x >= self.current_map.number_of_columns:
            self.tile_x = self.current_map.number_of_columns - 1
        self.tile_y += change_y
        if self.tile_y < 0:
            self.tile_y = 0
        elif self.tile_y >= self.current_map.number_of_rows:
            self.tile_y = self.current_map.number_of_rows - 1

        self.assign_tile()
        self.sprite.rect.x = self.tile_x * 20
        self.sprite.rect.y = (self.tile_y - (self.height - 1)) * 20
        self.change_x = 0
        self.change_y = 0

    def calculate_step(self, my_position, target_object, target_coordinates):
        if not self.path or not self.path.tiles or self.path.tiles[0].is_occupied():
            self.path, target_coordinates = navigate.get_path(my_position, self.current_map, target_coordinates)
        change_x, change_y = navigate.calculate_step(my_position, self.path.tiles[0])
        return change_x, change_y


class StationaryEntity(Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, current_map)




