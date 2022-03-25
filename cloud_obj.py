import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Cloud(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.image = pygame.image.load(f'Cloud{num}.png').convert_alpha()
        self.rect = self.image.get_rect()
        if num == 0:
            self.rect.left = 0
            self.rect.bottom = SCREEN_HEIGHT
        else:
            self.rect.left = SCREEN_WIDTH
            self.rect.bottom = SCREEN_HEIGHT

    def update(self):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH


cloud_group = pygame.sprite.Group()
cloud_group.add(Cloud(0))
cloud_group.add(Cloud(1))
