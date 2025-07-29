import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot


PLAYER_RADIUS = 20
COOLDOWN_TIMER = 0

class Player(CircleShape):
    def __init__(self, x, y, COOLDOWN_TIMER):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.PLAYER_RADIUS = PLAYER_RADIUS
        self.rotation = 0
        self.COOLDOWN_TIMER = COOLDOWN_TIMER
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.PLAYER_RADIUS / 1.5
        a = pygame.Vector2(self.position) + forward * self.PLAYER_RADIUS
        b = pygame.Vector2(self.position) - forward * self.PLAYER_RADIUS - right
        c = pygame.Vector2(self.position) - forward * self.PLAYER_RADIUS + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        unit_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        self.COOLDOWN_TIMER = PLAYER_SHOOT_COOLDOWN
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS, PLAYER_SHOT_SPEED)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

    def draw(self, screen):
        triangle_points = self.triangle()
        print(f"Drawing triangle at: {triangle_points}")
        print(f"Player position: {self.position}")
        pygame.draw.polygon(screen, "white", triangle_points, 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.COOLDOWN_TIMER -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if self.COOLDOWN_TIMER < 0:
            if keys[pygame.K_SPACE]:
                self.shoot(dt)
        else:
            print("Cooldown active, cannot shoot yet.")