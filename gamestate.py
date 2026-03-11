import pygame
from constants import *
from player import Player
from ball import Ball


class Gamestate():
    def __init__(self):
        self.player = Player()
        self.ball = Ball()
        self.computer = pygame.Rect((WIDTH/2 - PLAYER_WIDTH/2), 25, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.score = [0,0]
        self.score_surf = TEXT_FONT.render(f'{self.score}', 0, 'red')
        self.score_surf_rect = self.score_surf.get_rect()

    def handle_collision(self):
        if self.ball.rect.colliderect(self.player.rect):
            self.ball.vel_y *= -1
            self.ball.rect.bottom = self.player.rect.top
            
            if self.player.direction == "left":
                self.ball.vel_x = VEL * -1
            if self.player.direction == "right":
                self.ball.vel_x = VEL
            
        if self.ball.rect.colliderect(self.computer):
            self.ball.vel_y *= -1
            self.ball.rect.top = self.computer.bottom

    def handle_score(self):
        if self.ball.rect.top <= 0:
            self.score[0] +=1
            self.ball.status = "rest"
        
        if self.ball.rect.bottom >= HEIGHT:
            self.score[1] +=1
            self.ball.status = "rest"

        self.score_surf = TEXT_FONT.render(f'{self.score}', 0, 'red')

    def handle_computer(self):
        if self.ball.status == "rest":
            self.computer.centerx = WIDTH/2 
        elif self.ball.status == "moving": 
            if self.ball.rect.x < self.computer.centerx:
                self.computer.x -= COMP_VEL
            elif self.ball.rect.x > self.computer.centerx:
                self.computer.x += COMP_VEL

    def draw_window(self):
        WIN.fill((SCREEN_COLOR)) #Set the color of the screen
        self.player.draw()
        self.ball.draw()
        pygame.draw.rect(WIN, COMPUTER_COLOR, self.computer)
        WIN.blit(self.score_surf, (self.score_surf_rect))
        pygame.display.update() #Updates the display at the end of each frame

    def update(self):
        self.handle_collision()
        self.handle_score()
        self.handle_computer()

        self.player.update()
        self.ball.update(self.player)

        self.draw_window()