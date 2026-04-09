import pygame
from constants import *
from logger import log_state

    
def main():
    pygame_version = pygame.version.ver
    print(F"Starting Asteroids with pygame version: {pygame_version}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")    
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()