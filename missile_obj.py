import pygame
import math
from player_obj import player

missile_group = pygame.sprite.Group()


def dir_to(mp, tp):
    convert = 57.29577951
    x = tp[0] - mp[0]
    y = tp[1] - mp[1]
    if y == 0:
        return 90 if x > 0 else 270
    if y > 0:
        return (math.atan(x / y)) * convert
    else:
        return math.atan(x / y) * convert + 180


def dis_to(mp, tp):
    x = tp[0] - mp[0]
    y = tp[1] - mp[1]
    return math.sqrt(x ** 2 + y ** 2)


class Missile(pygame.sprite.Sprite):
    def __init__(self, target=None):
        super().__init__()
        self.image = pygame.Surface((5, 2))
        self.image.fill('Red')
        self.true_position = (player.rect.right, player.rect.center[1])
        self.rect = self.image.get_rect(center=self.true_position)
        self.target = target
        self.angle = 90
        self.speed = 10

    def update(self):
        convert = math.pi * 2 / 360
        if self.target and self.target.health <= 0:
            self.target = None
        if self.target:
            predict = (self.target.rect.centerx - (
                        (dis_to(self.rect.center, self.target.rect.center) / self.speed) * self.target.speed / 2),
                       self.target.rect.centery)
            self.angle = dir_to(self.rect.center, predict)
        x = math.sin(self.angle * convert)
        y = math.cos(self.angle * convert)
        self.true_position = (self.true_position[0] + x * self.speed, self.true_position[1] + y * self.speed)
        self.rect.center = self.true_position
