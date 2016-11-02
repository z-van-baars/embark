import structure
import art
import random
import weapon


class Corpse(structure.Container):
    interactable = True
    footprint = (1, 1)
    height = 1

    def __init__(self, x, y, current_map, creature, player_level):
        self.corpse_type = creature.display_name
        super().__init__(x, y, current_map)
        self.display_name = creature.display_name + " Corpse"
        self.image_key = self.display_name
        self.set_images(self.image_key)
        self.fill(player_level, self.corpse_type)

    def fill(self, player_level, creature):
        for x in range(random.randint(2, 10)):
            self.items_list.append(random.choice(weapon.weapon_functions)(self.value, player_level))
        self.opened = True

    def tick_cycle(self):
        self.age += 1
        if self.age > 10000:
            self.expire(1, True)
