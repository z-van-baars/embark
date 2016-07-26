import utilities
import random


class Herd(object):
    def __init__(self, current_map):
        self.alpha = None
        self.members = []
        self.migration_target = None
        self.current_map = current_map

    def check_food_supply(self):
        self.alpha.find_local_food()
        if len(self.alpha.local_food_supply) < (len(self.members) / 4):
            self.migration_target = self.choose_random_migration_target(self.current_map, (self.alpha.tile_x, self.alpha.tile_y))
        else:
            self.migration_target = (self.alpha.tile_x, self.alpha.tile_y)
        assert self.migration_target

    def choose_new_alpha(self):
        herd_rankings = []
        for beast in self.members:
            herd_rankings.append((beast.age, beast))
        herd_rankings = sorted(herd_rankings, reverse=True)
        self.alpha = herd_rankings[0][1]
        self.alpha.is_alpha = True
        self.alpha.image.fill(self.alpha.alpha_color)

    def choose_random_migration_target(self, game_map, alpha_coordinates):
        target_x = -1
        target_y = -1
        while alpha_coordinates != (target_x, target_y):
            target_x = random.randint(0, game_map.number_of_columns - 1)
            target_y = random.randint(0, game_map.number_of_rows - 1)
        return (target_x, target_y)

