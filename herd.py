import utilities
import random


class Herd(object):
    def __init__(self, current_map):
        self.alpha = None
        self.members = []
        self.migration_target = None
        self.current_map = current_map

    def check_food_supply(self):
        local_food_supply = self.alpha.find_local_food(self.alpha.current_map, None)
        if len(local_food_supply) < (len(self.members) / 4):
            if not self.migration_target:
                self.migration_target = self.alpha.choose_random_target(self.alpha.current_map, (self.alpha.tile_x, self.alpha.tile_y))
            else:
                self.alpha_near_target(self.alpha.current_tile, self.migration_target)
        else:
            self.migration_target = self.alpha.tile_x, self.alpha.tile_y

    def choose_new_alpha(self):
        herd_rankings = []
        for beast in self.members:
            herd_rankings.append((beast.age, beast))
        herd_rankings = sorted(herd_rankings, reverse=True)
        self.alpha = herd_rankings[0][1]
        self.alpha.is_alpha = True

    def alpha_near_target(self, alpha_tile, migration_target):
        nearby_tiles = utilities.get_nearby_tiles(self.current_map, migration_target, self.alpha.herd_radius)
        if alpha_tile in nearby_tiles:
            self.migration_target = self.alpha.choose_random_target(self.alpha.current_map, (self.alpha.tile_x, self.alpha.tile_y))

