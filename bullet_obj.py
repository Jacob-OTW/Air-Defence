import pygame
import random
from settings import SCREEN_WIDTH

bullet_group = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, yf):
        super().__init__()
        self.true_position = (pos[0], pos[1])
        self.image = pygame.image.load('Assets/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 4))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = self.true_position
        self.angle = random.randint(0, 360)
        self.yv = random.randint(-10, 10) / 35 + yf
        self.speed = 12

    def update(self):
        self.true_position = (self.true_position[0] + self.speed, self.true_position[1] + self.yv)
        self.rect.center = self.true_position
        if self.rect.left > SCREEN_WIDTH:
            bullet_group.remove(self)
