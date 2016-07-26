import utilities


class Herd(object):
    def __init__(self, current_map):
        self.alpha = None
        self.members = []
        self.migration_target = None
        self.current_map = current_map

    def check_food_supply(self):
        self.alpha.find_local_food()
        if len(self.alpha.local_food_supply) < (len(self.members) / 4):
            if not self.migration_target:
                self.migration_target = self.alpha.pick_migration_target(self.current_map, (self.alpha.tile_x, self.alpha.tile_y))
            else:
                if utilities.distance(self.alpha.tile_x, self.alpha.tile_y, self.migration_target[0], self.migration_target[1]) == 0:
                    self.migration_target = self.alpha.pick_migration_target(self.current_map, (self.alpha.tile_x, self.alpha.tile_y))
                else:
                    self.alpha.migration_target = self.alpha.pick_migration_target(self.current_map, (self.alpha.tile_x, self.alpha.tile_y))
        else:
            self.migration_target = (self.alpha.tile_x, self.alpha.tile_y)

    def choose_new_alpha(self):
        herd_rankings = []
        for beast in self.members:
            herd_rankings.append((beast.age, beast))
        herd_rankings = sorted(herd_rankings, reverse=True)
        self.alpha = herd_rankings[0][1]
        self.alpha.is_alpha = True
        self.alpha.image.fill(self.alpha.alpha_color)
