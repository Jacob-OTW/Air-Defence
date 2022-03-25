import pygame
import sys
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock
from missile_obj import Missile, missile_group
from enemy_obj import Enemy, enemy_group
from bullet_obj import bullet_group
from player_obj import player_group, player
from cloud_obj import cloud_group


def HandleKeys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                if player.missile:
                    player.missile = False
                    if enemy_group:
                        missile_group.add(Missile(random.choice(enemy_group.sprites())))
                    else:
                        missile_group.add(Missile())


myfont = pygame.font.SysFont("monospace", 16)

enemy_spawn_timer = 0
while True:
    # Update
    HandleKeys()
    player_group.update()
    bullet_group.update()
    missile_group.update()
    enemy_group.update()
    cloud_group.update()

    # Spawner
    enemy_spawn_timer += 1
    if enemy_spawn_timer > 240:
        enemy_group.add(Enemy((SCREEN_WIDTH + 20, random.randint(15, SCREEN_HEIGHT - 15))))
        enemy_spawn_timer = 0

    # Visual
    screen.fill((97, 201, 207))
    cloud_group.draw(screen)
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
