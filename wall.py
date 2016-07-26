from entity import Entity


class Wall(Entity):
    def __init__(self, x, y, current_map):
        super().__init__(x, y, (141, 145, 158), 10, 10, current_map, None)
