import math

import pygame
import sys
import random


def HandleKeys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                missile_group.add(Missile())


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 10))
        self.image.fill('White')
        self.rect = self.image.get_rect()
        self.rect.center = (20, SCREEN_HEIGHT / 2)

    def update(self):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_w]:
            self.rect.center = (self.rect.center[0], self.rect.center[1] - 5)
        if keyboard[pygame.K_s]:
            self.rect.center = (self.rect.center[0], self.rect.center[1] + 5)
        if keyboard[pygame.K_SPACE]:
            bullet_group.add(Bullet())


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.true_position = (player.rect.right, player.rect.center[1])
        self.image = pygame.Surface((5, 5))
        self.image.fill('White')
        self.rect = self.image.get_rect()
        self.rect.center = self.true_position
        self.angle = random.randint(0, 360)
        self.yv = random.randint(-10, 10) / 35

    def update(self):
        self.true_position = (self.true_position[0] + 4, self.true_position[1] + self.yv)
        self.rect.center = self.true_position
        if self.rect.left > SCREEN_WIDTH:
            bullet_group.remove(self)


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

        collided = pygame.sprite.groupcollide(enemy_group, bullet_group, False, True)
        if collided != {}:
            self.health -= 1
            if self.health <= 0:
                enemy_group.remove(self)


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 2))
        self.image.fill('Red')
        self.rect = self.image.get_rect()
        self.true_position = (player.rect.right, player.rect.center[1])
        self.rect.center = self.true_position

    @classmethod
    def dir_to(cls, mp, tp):
        convert = 57.29577951
        x = tp[0] - mp[0]
        y = tp[1] - mp[1]
        if y == 0:
            return 90 if x > 0 else 270
        if y > 0:
            return math.atan(x / y)
        else:
            return math.atan(x / y) + 180 / convert

    def dis_to(self, mp, tp):
        x = tp[0] - mp[0]
        y = tp[1] - mp[1]
        return math.sqrt(x ** 2 + y ** 2)

    def closest_enemy(self):
        a = {}
        for enemy in enemy_group.sprites():
            a[self.rect.center, enemy.rect.center] = enemy
        return a[min(a.keys())]

    def update(self):
        enemy = self.closest_enemy()
        direction = Missile.dir_to(self.rect.center, enemy.rect.center)
        add_x = enemy.rect.center[0] + math.cos(direction)
        add_y = enemy.rect.center[1] + math.sin(direction)
        self.true_position = (self.true_position[0] + add_x, self.true_position[1] + add_y)
        self.rect.center = self.true_position


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20
GRID_WIDTH = int(SCREEN_HEIGHT / GRIDSIZE)
GRID_HEIGHT = int(SCREEN_WIDTH / GRIDSIZE)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

myfont = pygame.font.SysFont("monospace", 16)

# Player
player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

# Ball
bullet_group = pygame.sprite.Group()

# Missile
missile_group = pygame.sprite.Group()

# Enemy
enemy_group = pygame.sprite.Group()

enemy_spawn_timer = 0
while True:
    # Update
    HandleKeys()
    player_group.update()
    bullet_group.update()
    missile_group.update()
    enemy_group.update()

    # Spawner
    enemy_spawn_timer += 1
    if enemy_spawn_timer > 240:
        enemy_group.add(Enemy((SCREEN_WIDTH + 20, random.randint(15, SCREEN_HEIGHT - 15))))
        enemy_spawn_timer = 0

    # Visual
    screen.fill('black')
    bullet_group.draw(screen)
    missile_group.draw(screen)
    enemy_group.draw(screen)
    player_group.draw(screen)

    # Text
    text = myfont.render(f"", True, (255, 0, 0))
    screen.blit(text, (5, 10))

    # Refresh
    pygame.display.flip()
    clock.tick(60)
