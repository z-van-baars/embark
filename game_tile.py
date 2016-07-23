from buffalo import Buffalo
from manure import Manure
from wheat import Wheat


class GameTile(object):
    def __init__(self, terrain_type, column, row):
        self.row = row
        self.column = column
        self.terrain_type = terrain_type
        self.entity_group = {Buffalo: [],
        Wheat: [],
        Manure: [],
        }
