import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS, PLAYER_SHOT_SPEED):
        super().__init__(x, y, SHOT_RADIUS)
        self.PLAYER_SHOT_SPEED = PLAYER_SHOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS)
        # sub-classes must override
        pass

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
