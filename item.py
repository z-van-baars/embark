
class Item(object):
    equipable = False

    def __init__(self, name, value, weight):
        super().__init__()
        self.name = name
        self.value = value
        self.weight = weight

rubbish = [("Scrap Paper", 1, 1), ("Broken Sword", 2, 5), ("Burnt Bread", 1, 2)]
treasures = [("Gold Bar", 30, 1), ("Ye Flaske", 1000, 1)]
