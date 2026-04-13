import pygame,sys
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
    
def main():
    pygame_version = pygame.version.ver
    print(F"Starting Asteroids with pygame version: {pygame_version}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    Shot.containers  = (shots,updatable,drawable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroids_field = AsteroidField()
    #game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") 
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player) :
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()

        for o in drawable :
            o.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()