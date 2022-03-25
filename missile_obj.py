import pygame
import math
import random
from player_obj import player
from enemy_obj import enemy_group

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


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 2))
        self.image.fill('Red')
        self.true_position = (player.rect.right, player.rect.center[1])
        self.rect = self.image.get_rect(center=self.true_position)
        self.target = random.choice(enemy_group.sprites())

    def update(self):
        convert = math.pi * 2 / 360
        x = math.sin(dir_to(self.rect.center, enemy_group.sprites()[0].rect.center) * convert)
        y = math.cos(dir_to(self.rect.center, enemy_group.sprites()[0].rect.center) * convert)
        self.true_position = (self.true_position[0] + x * 2, self.true_position[1] + y * 2)
        self.rect.center = self.true_position
