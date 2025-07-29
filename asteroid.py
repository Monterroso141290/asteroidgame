import pygame
from circleshape import * 
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = x
        self.y = y
        

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)


    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            rotated_velocity = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = rotated_velocity * 1.2

            random_angle = random.uniform(20, 50)
            rotated_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = rotated_velocity * 1.2

            return [asteroid1, asteroid2]
