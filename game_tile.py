

class GameTile(object):
    def __init__(self, terrain_type, column, row):
        self.row = row
        self.column = column
        self.terrain_type = terrain_type
        self.buffalo_list = []
        self.wheat_list = []
