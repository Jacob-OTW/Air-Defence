import pygame
import sys
import random
from missile_obj import Missile, missile_group
from enemy_obj import Enemy, enemy_group
from bullet_obj import bullet_group
from player_obj import player_group
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


def HandleKeys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                missile_group.add(Missile(random.choice(enemy_group.sprites())))


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

myfont = pygame.font.SysFont("monospace", 16)

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
