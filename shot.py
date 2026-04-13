import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS,LINE_WIDTH,PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self,position,velocity):
        super().__init__(position.x,position.y,SHOT_RADIUS)        
        self.velocity = velocity * PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt