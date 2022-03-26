import random

import pygame


def add_smoke(pos):
    smoke_group.add(Smoke(pos))


class Smoke(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Assets/Smoke.png'), (20, 20))
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.opacity = 255
        self.fall_speed = 0.3
        self.vec = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

    def update(self):
        self.pos = (self.pos[0], self.pos[1] + self.fall_speed)
        self.pos += self.vec
        self.rect.center = self.pos
        self.image.set_alpha(self.opacity)
        self.opacity -= 5
        if self.opacity <= 0:
            self.kill()


smoke_group = pygame.sprite.Group()
