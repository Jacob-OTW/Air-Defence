import pygame
from bullet_obj import bullet_group
from missile_obj import missile_group
from settings import change_score, change_lives
from pilot_obj import pilot_group, Pilot

enemy_group = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Assets/enemy.png').convert_alpha(), (190, 60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.health = 20
        self.speed = 3

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            change_lives(-1)
            self.kill()
        for bullet in bullet_group:
            temp = self.mask.overlap(bullet.mask, (bullet.rect.x - self.rect.x, bullet.rect.y - self.rect.y))
            if temp:
                self.health -= 1
                bullet.kill()
                if self.health <= 0:
                    change_score(1)
                    pilot_group.add(Pilot(self.rect.center))
                    self.kill()
        for missile in missile_group:
            temp = self.mask.overlap(missile.mask, (missile.rect.x - self.rect.x, missile.rect.y - self.rect.y))
            if temp:
                missile.kill()
                self.health = 0
                change_score(1)
                pilot_group.add(Pilot(self.rect.center))
                self.kill()
