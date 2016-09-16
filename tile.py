import pygame

#terrain_type = ("Name", (color_tuple))


class DisplayTile(pygame.sprite.Sprite):
    def __init__(self, terrain_type):
        super().__init__()
        self.name = terrain_type[0]
        self.color = terrain_type[1]
        self.image = pygame.Surface([20, 20])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()


class ImageTile(pygame.sprite.Sprite):
	def __init__(self, image):
		super().__init__()
		self.image = image
		self.rect = self.image.get_rect()
