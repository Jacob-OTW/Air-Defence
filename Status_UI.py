import pygame
import settings


class Status_UI(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.heart = pygame.image.load('Assets/heart.png').convert_alpha()
        self.stored = pygame.Surface((300, 80), pygame.SRCALPHA, 32)
        self.image = self.stored
        self.rect = self.image.get_rect(left=0, top=0)
        self.Heart_positions = [(0, 0), (100, 0), (200, 0)]

    def update(self):
        self.image = pygame.Surface((300, 80), pygame.SRCALPHA, 32)
        for i, position in enumerate(self.Heart_positions):
            if i+1 <= settings.LIVES:
                self.image.blit(self.heart, position)


statusUI_group = pygame.sprite.Group()
statusUI_group.add(Status_UI())