import pygame
from player_obj import player
from settings import SCREEN_HEIGHT


class UI(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = {'gun': pygame.image.load('Assets/UI_gun.png').convert_alpha(),
                       'missile': pygame.image.load('Assets/UI_missile.png').convert_alpha()}
        self.img_surface = pygame.transform.scale(self.images[player.weapon], (300, 150))
        self.missile_load = pygame.Surface((150, 150))
        self.missile_load.fill('Green')
        self.image = pygame.Surface((300, 150))
        self.rect = self.image.get_rect(left=0, bottom=SCREEN_HEIGHT)

    def update(self):
        self.img_surface = pygame.transform.scale(self.images[player.weapon], (300, 150))
        loading_rect = pygame.transform.scale(self.missile_load, (150, player.missile_timer / 1.6))
        loading_rect.set_alpha(153)
        self.image.blit(self.img_surface, (0, 0))
        self.image.blit(loading_rect, (150, 0))


ui_group = pygame.sprite.Group()
ui_group.add(UI())
