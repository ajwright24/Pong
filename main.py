import pygame
from sys import exit
from constants import *
pygame.font.init()
pygame.display.set_caption("Pong") #Code to set caption at the top of the window

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TEXT_FONT = pygame.font.Font(None, 50)

def draw_window(player, ball, ball_color, computer, score_surf, score_surf_rect):
    WIN.fill((SCREEN_COLOR)) #Set the color of the screen
    pygame.draw.rect(WIN, PLAYER_COLOR, player)
    pygame.draw.rect(WIN, COMPUTER_COLOR, computer)
    pygame.draw.rect(WIN, ball_color, ball)
    WIN.blit(score_surf, (score_surf_rect))

    pygame.display.update() #Updates the display at the end of each frame

def move_player(pressed_keys, player):

    if pressed_keys[pygame.K_LEFT] and player.left - VEL > 0:
        player.x -= VEL
        return "left"
    if pressed_keys[pygame.K_RIGHT] and player.right + VEL < WIDTH:
        player.x += VEL
        return "right"
    
def move_comp(ball, computer, ball_status):
    if ball_status == "moving" and ball.x < computer.centerx:
        computer.x -= COMP_VEL
    if ball_status == "moving" and ball.x > computer.centerx:
        computer.x += COMP_VEL



def ball_movement(ball_status, player, ball, ball_vel_y, ball_vel_x):
    
    if ball_status == "rest":
        ball.center = player.midtop
        ball_vel_x = 0

    elif ball_status == "moving":
        ball.y += ball_vel_y
        ball.x += ball_vel_x
    

def launch_ball():
    ball_status = "moving"
    ball_color = (250, 0, 250)
    return ball_status, ball_color

def check_score(ball, ball_status, score):
    if ball.top <= 0:
            score[0] +=1
            ball_status = "rest"
        
    if ball.bottom >= HEIGHT:
            score[1] +=1
            ball_status = "rest"
    
    return ball_status, score


def main():
    pygame.init
    player = pygame.Rect((WIDTH/2 - PLAYER_WIDTH/2), HEIGHT - 50, PLAYER_WIDTH, PLAYER_HEIGHT)
    computer = pygame.Rect((WIDTH/2 - PLAYER_WIDTH/2), 25, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(player.centerx, (player.top - BALL_HEIGHT), BALL_WIDTH, BALL_HEIGHT)
    clock = pygame.time.Clock() #creates a Clock object named clock
    ball_status = "rest"
    ball_color = (0, 255, 255)
    ball_vel_y = -10
    ball_vel_x = 0
    score = [0,0]
    while True:
        clock.tick(FPS) #caps framerate at the constant FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #opposite of pygame.init #not sure if i need this if i have exit
                exit() #safest way to exit. imported from sys at the top

            if event.type == pygame.KEYDOWN:
                if ball_status == "rest" and event.key == pygame.K_SPACE:
                    ball_status, ball_color = launch_ball()
        
        if ball_status == "rest":
            ball_vel_x = 0
            computer.centerx = (WIDTH/2)

        if ball.colliderect(player):
            ball_vel_y *= -1
            ball.bottom = player.top
            if player_direction == "left":
                ball_vel_x = VEL * -1
            if player_direction == "right":
                ball_vel_x = VEL
            
        if ball.colliderect(computer):
            ball_vel_y *= -1
            ball.top = computer.bottom
        
        if ball.x + ball_vel_x < 0 or ball.x + ball_vel_x > WIDTH:
            ball_vel_x *= -1
            ball.x += ball_vel_x  

        score_surf = TEXT_FONT.render(f'{score}', 0, 'red')
        score_surf_rect = score_surf.get_rect()

        pressed_keys = pygame.key.get_pressed()

        player_direction = move_player(pressed_keys, player)
        move_comp(ball, computer, ball_status)
        ball_movement(ball_status, player, ball, ball_vel_y, ball_vel_x)
        ball_status, score = check_score(ball, ball_status, score)
        draw_window(player, ball, ball_color, computer, score_surf, score_surf_rect)
        
if __name__ == "__main__": #Makes sure the game only runes if it is called directly
    main() #runs the main function
