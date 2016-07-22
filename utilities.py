import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Embark v 0.1")


class GlobalVariables(object):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.clock = pygame.time.Clock()
        self.time = 0
        self.font = pygame.font.SysFont('Calibri', 18, True, False)


class Colors(object):
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.light_green = (0, 215, 0)
        self.dark_green = (0, 200, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.blue_grey = (180, 210, 217)
        self.purple = (255, 0, 255)
        self.wheat_gold = (220, 187, 0)
        self.key = (255, 0, 128)

colors = Colors()