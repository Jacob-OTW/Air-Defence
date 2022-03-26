import pygame
import sys
import random
import settings
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock
from missile_obj import missile_group
from enemy_obj import Enemy, enemy_group
from pilot_obj import pilot_group
from bullet_obj import bullet_group
from player_obj import player_group, player
from cloud_obj import cloud_group
from UI import ui_group
from Status_UI import statusUI_group


def HandleKeys():
    if settings.LIVES <= 0:
        pygame.quit()
        print(settings.SCORE)
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if player.weapon == 'gun':
                    player.weapon = 'missile'
                else:
                    player.weapon = 'gun'


score_font = pygame.font.SysFont("arial", 32, pygame.font.Font.bold)


def main():
    enemy_spawn_timer = 0
    while True:
        # Update
        HandleKeys()
        player_group.update()
        bullet_group.update()
        missile_group.update()
        enemy_group.update()
        pilot_group.update()
        cloud_group.update()
        ui_group.update()
        statusUI_group.update()

        # Spawner
        enemy_spawn_timer += 1
        if enemy_spawn_timer > 145:
            enemy_group.add(Enemy((SCREEN_WIDTH + 20, random.randint(15, SCREEN_HEIGHT - 15))))
            enemy_spawn_timer = 0

        # Visual
        screen.fill((97, 201, 207))
        cloud_group.draw(screen)
        ui_group.draw(screen)
        statusUI_group.draw(screen)
        bullet_group.draw(screen)
        pilot_group.draw(screen)
        missile_group.draw(screen)
        enemy_group.draw(screen)
        player_group.draw(screen)

        # Text
        color = min(255, settings.SCORE)
        text = score_font.render(f"{settings.SCORE}", True, (color, color, color))
        text_rect = text.get_rect(center=(150, 90))
        screen.blit(text, text_rect)

        # Refresh
        pygame.display.flip()
        clock.tick(60)


main()
