import pygame
from bullet_obj import bullet_group

enemy_group = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill('Blue')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.health = 20

    def update(self):
        self.rect.x -= 1
        if self.rect.right < 0:
            enemy_group.remove(self)
        collided = pygame.sprite.groupcollide(enemy_group, bullet_group, False, True)
        if collided != {}:
            self.health -= 1
            if self.health <= 0:
                enemy_group.remove(self)
