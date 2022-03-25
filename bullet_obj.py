import pygame
import random
from settings import SCREEN_WIDTH

bullet_group = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.true_position = (pos[0], pos[1])
        self.image = pygame.Surface((5, 5))
        self.image.fill('White')
        self.rect = self.image.get_rect()
        self.rect.center = self.true_position
        self.angle = random.randint(0, 360)
        self.yv = random.randint(-10, 10) / 35

    def update(self):
        self.true_position = (self.true_position[0] + 4, self.true_position[1] + self.yv)
        self.rect.center = self.true_position
        if self.rect.left > SCREEN_WIDTH:
            bullet_group.remove(self)
