import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_sprite = pygame.image.load('Assets/Neon Rectangle.png').convert_alpha()
        player_sprite = pygame.transform.scale(player_sprite, (PLAYER_WIDTH, PLAYER_HEIGHT))
        crop_rect = player_sprite.get_bounding_rect(min_alpha=150)
        player_sprite = player_sprite.subsurface(crop_rect).copy()
        
        self.image = player_sprite
        self.rect = player_sprite.get_rect(center = (600, 700))
        self.direction = None
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left - VEL > 0:
            self.rect.x -= VEL
            self.direction = "left"
        elif keys[pygame.K_RIGHT] and self.rect.right + VEL < WIDTH:
            self.rect.x += VEL
            self.direction = "right"
        else:
            self.direction = None

    def draw(self):
        WIN.blit(self.image, self.rect)

    def update(self):
        self.player_input()