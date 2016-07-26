from entity import Entity


class Wall(Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, (0, 0, 255), 10, 10, current_map, None)
