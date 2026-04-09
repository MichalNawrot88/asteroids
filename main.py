import pygame
from constants import *

def main():
    pygame_version = pygame.version.ver
    print(F"Starting Asteroids with pygame version: {pygame_version}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
