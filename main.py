import pygame
import sys
import random


def HandleKeys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_group.add(Bullet())


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


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill('White')
        self.rect = self.image.get_rect()
        self.rect.center = (player.rect.right, player.rect.center[1])
        self.angle = random.randint(0, 360)

    def update(self):
        self.rect.x += 1
        pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill('Blue')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.x -= 1


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

# Enemy
enemy_group = pygame.sprite.Group()

enemy_spawn_timer = 0
while True:
    # Update
    HandleKeys()
    player_group.update()
    bullet_group.update()
    enemy_group.update()

    # Spawner
    enemy_spawn_timer += 1
    if enemy_spawn_timer > 120:
        enemy_group.add(Enemy((SCREEN_WIDTH + 20, random.randint(15, SCREEN_HEIGHT - 15))))
        enemy_spawn_timer = 0

    # Visual
    screen.fill('black')
    bullet_group.draw(screen)
    enemy_group.draw(screen)
    player_group.draw(screen)

    # Text
    text = myfont.render(f"", True, (255, 0, 0))
    screen.blit(text, (5, 10))

    # Refresh
    pygame.display.flip()
    clock.tick(60)
