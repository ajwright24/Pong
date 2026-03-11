import pygame
from sys import exit
from constants import *
from gamestate import Gamestate


pygame.display.set_caption("Pong") #Code to set caption at the top of the window

def main():
    pygame.init()
    gamestate = Gamestate()
    clock = pygame.time.Clock() #creates a Clock object named clock
    
    while True:
        clock.tick(FPS) #caps framerate at the constant FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #opposite of pygame.init #not sure if i need this if i have exit
                exit() #safest way to exit. imported from sys at the top

        gamestate.update()

if __name__ == "__main__": #Makes sure the game only runes if it is called directly
    main() #runs the main function
