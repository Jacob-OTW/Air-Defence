import pygame
from settings import SCREEN_HEIGHT
from bullet_obj import Bullet, bullet_group


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('plane.png.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (211, 67))
        self.rect = self.image.get_rect()
        self.rect.center = (211/2 + 10, SCREEN_HEIGHT / 2)
        self.y_force = 0
        self.missile = True
        self.missile_timer = 0

    def update(self):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_w] or keyboard[pygame.K_s]:
            if keyboard[pygame.K_w]:
                self.y_force = -5
            else:
                self.y_force = 5
        else:
            self.y_force = 0
        self.rect.y += self.y_force
        if keyboard[pygame.K_SPACE]:
            bullet_group.add(Bullet((self.rect.right / 1.1, self.rect.centery / 0.975), self.y_force / 2))
        if not self.missile:
            self.missile_timer += 1
            if self.missile_timer >= 60:
                self.missile = True
                self.missile_timer = 0


player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)
