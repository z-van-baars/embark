import utilities
import random


class Herd(object):
    def __init__(self, current_map):
        self.alpha = None
        self.members = []
        self.migration_target = None
        self.current_map = current_map

    def check_food_supply(self):
        local_food_supply = self.alpha.find_local_food()
        if len(local_food_supply) < (len(self.members) / 4):
            if not self.migration_target or self.migration_target == (self.alpha.tile_x, self.alpha.tile_y):
                self.migration_target = self.choose_random_migration_target(self.current_map, (self.alpha.tile_x, self.alpha.tile_y))
            print(self.migration_target)
        else:
            self.migration_target = (self.alpha.tile_x, self.alpha.tile_y)
        assert self.migration_target
        assert self.migration_target != (self.alpha.tile_x, self.alpha.tile_y)

    def choose_new_alpha(self):
        herd_rankings = []
        for beast in self.members:
            herd_rankings.append((beast.age, beast))
        herd_rankings = sorted(herd_rankings, reverse=True)
        self.alpha = herd_rankings[0][1]
        self.alpha.is_alpha = True
        self.alpha.image.fill(self.alpha.alpha_color)

    def choose_random_migration_target(self, game_map, alpha_coordinates):
        target_x, target_y = alpha_coordinates
        while alpha_coordinates == (target_x, target_y):
            target_x = random.randint(0, game_map.number_of_columns - 1)
            target_y = random.randint(0, game_map.number_of_rows - 1)
        return (target_x, target_y)

