import pygame
from constants import *
from logger import log_state
from player import Player
    
def main():
    pygame_version = pygame.version.ver
    print(F"Starting Asteroids with pygame version: {pygame_version}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    #game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") 
        player.draw(screen)   
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()