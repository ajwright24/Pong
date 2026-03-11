import pygame
pygame.font.init()

#Ball
BALL_WIDTH, BALL_HEIGHT = 20, 20

#Computer
COMPUTER_COLOR = (0, 0, 255)
COMP_VEL = 8.5

#Player
PLAYER_COLOR = (255, 0, 0) #red
PLAYER_WIDTH, PLAYER_HEIGHT = 200, 30
VEL = 10

#Screen
FPS = 60
SCREEN_COLOR = (100,100,100) #gray
TEXT_FONT = pygame.font.Font(None, 50)
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))