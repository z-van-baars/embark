from buffalo import Buffalo
from manure import Manure
from wheat import Wheat
from wall import Wall
from tree import Tree
from avatar import Avatar


class GameTile(object):
    def __init__(self, terrain_type, column, row):
        self.row = row
        self.column = column
        self.terrain_type = terrain_type
        self.entity_group = {
                            Buffalo: [],
                            Wheat: [],
                            Manure: [],
                            Wall: [],
                            Tree: [],
                            Avatar: []
                            }
    def __lt__(self, other):
        return False

    def is_occupied(self):
        for entity_type in self.entity_group:
            if entity_type.occupies_tile:
                if self.entity_group[entity_type]:
                    return True
        return False
