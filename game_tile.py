

class GameTile(object):
    def __init__(self, terrain_type, column, row):
        self.row = row
        self.column = column
        self.terrain_type = terrain_type
        self.entity_group = {
                            "Terrain": [],
                            "Structure":[],
                            "Flora": [],
                            "Creature": [],
                            "Npc": [],
                            "Avatar": []
                            }
    def __lt__(self, other):
        return False

    def is_occupied(self):
        for entity_type in self.entity_group:
            if self.entity_group[entity_type]:
                if self.entity_group[entity_type][0].occupies_tile:
                    return True
        return False
