import pygame
from constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ball_sprite = pygame.image.load('Assets/pokeball.png').convert_alpha()
        ball_sprite = pygame.transform.scale(ball_sprite, (BALL_WIDTH, BALL_HEIGHT))

        self.image = ball_sprite
        self.rect = ball_sprite.get_rect(center = (600, 500))
        self.vel_x = 0
        self.vel_y = -10
        self.status = "rest"

    def launch_ball(self):
        keys = pygame.key.get_pressed()
        if self.status == "rest" and keys[pygame.K_SPACE]:
            self.status = "moving"

    def ball_movement(self, player):
        if self.status == "rest":
            self.rect.center = player.rect.midtop
            self.vel_x = 0

        elif self.status == "moving":
            self.rect.y += self.vel_y
            self.rect.x += self.vel_x

    def check_bounce(self):
        if self.rect.x + self.vel_x < 0 or self.rect.x + self.vel_y > WIDTH:
            self.vel_x *= -1
            self.rect.x += self.vel_x 

    def draw(self):
        WIN.blit(self.image, self.rect)

    def update(self, player):
        self.launch_ball()
        self.check_bounce()
        self.ball_movement(player)