import pygame
from player_obj import player
from settings import SCREEN_HEIGHT


class UI(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = {'gun': pygame.image.load('Assets/UI_gun.png').convert_alpha(),
                       'missile': pygame.image.load('Assets/UI_missile.png').convert_alpha()}
        self.image = pygame.transform.scale(self.images[player.weapon], (300, 150))
        self.rect = self.image.get_rect(left=0, bottom=SCREEN_HEIGHT)

    def update(self):
        self.image = pygame.transform.scale(self.images[player.weapon], (300, 150))


ui_group = pygame.sprite.Group()
ui_group.add(UI())
