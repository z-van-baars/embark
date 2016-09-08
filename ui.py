import pygame


class Button(object):
    def __init__(self, regular_image, selected_image, on_click):

        self.regular = regular_image
        self.selected = selected_image
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.regular
        self.sprite.rect = self.sprite.image.get_rect()
        self.click = on_click
