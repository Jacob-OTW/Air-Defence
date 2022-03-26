import random

import pygame


def add_smoke(pos, m_vec=None):
    smoke_group.add(Smoke(pos, m_vec))


class Smoke(pygame.sprite.Sprite):
    def __init__(self, pos, m_vec=None):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Assets/Smoke.png').convert_alpha(), (20, 20))
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.opacity = 255
        self.fall_speed = 0.3
        self.vec = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.m_vec = m_vec

    def update(self):
        self.pos = (self.pos[0], self.pos[1] + self.fall_speed)
        self.pos += self.vec
        if self.m_vec:
            self.pos += pygame.math.Vector2(self.m_vec)
        self.rect.center = self.pos
        self.image.set_alpha(self.opacity)
        self.opacity -= 5
        if self.opacity <= 0:
            self.kill()


smoke_group = pygame.sprite.Group()
