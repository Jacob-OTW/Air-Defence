import pygame
from bullet_obj import bullet_group
from missile_obj import missile_group
from settings import change_score, change_lives

enemy_group = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(), (190, 60))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.health = 20
        self.speed = 3

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            change_lives(-1)
            self.kill()
        collided = pygame.sprite.groupcollide(enemy_group, bullet_group, False, True)
        if collided != {}:
            self.health -= 1
            if self.health <= 0:
                change_score(1)
                self.kill()
        collided = pygame.sprite.groupcollide(enemy_group, missile_group, False, True)
        if collided != {}:
            self.health = 0
            change_score(1)
            self.kill()
