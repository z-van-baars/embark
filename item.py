
class Item(object):
    def __init__(self, name, value, weight):
        super().__init__()
        self.name = name
        self.value = value
        self.weight = weight

rubbish = [("Scrap Paper", 1, 1), ("Broken Sword", 2, 5), ("Burnt Bread", 1, 2)]
weapons = [("Iron Dagger", 10, 3), ("Iron Longsword", 25, 7), ("Oak Bow", 15, 4)]
treasures = [("Gold Bar", 30, 1), ("Ye Flaske", 1000, 1)]
