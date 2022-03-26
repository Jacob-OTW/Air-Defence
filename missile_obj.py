import pygame
import math
from smoke import add_smoke
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
    def __init__(self, player, target=None):
        super().__init__()
        a = pygame.image.load('Assets/missile0.png').convert_alpha()
        b = pygame.image.load('Assets/missile1.png').convert_alpha()
        self.animations = [pygame.transform.scale(a, (35, 18)), pygame.transform.scale(b, (35, 18))]
        self.animation_index = 0
        self.animation_speed = 0.5
        self.image = self.animations[self.animation_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.true_position = (player.rect.right / 1.2, player.rect.centery / 0.975)
        self.rect = self.image.get_rect(center=self.true_position)
        self.target = target
        self.angle = 90
        self.speed = 10

    def update(self):
        convert = math.pi * 2 / 360
        self.animation_index += self.animation_speed
        if self.animation_index > len(self.animations) - 1:
            self.animation_index = 0
        self.image = pygame.transform.rotate(self.animations[int(self.animation_index)], self.angle - 90)
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
        self.rect = self.image.get_rect(center=self.true_position)
        add_smoke(self.rect.center)
