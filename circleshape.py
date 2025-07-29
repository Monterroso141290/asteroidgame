import pygame
PLAYER_RADIUS = 20

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, PLAYER_RADIUS):

        self.PLAYER_RADIUS = PLAYER_RADIUS
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        # sub-classes must override
        pass

    def collisions(self, circleshape):
        distance = self.position.distance_to(circleshape.position)
        if distance < self.PLAYER_RADIUS + circleshape.PLAYER_RADIUS:
            collision = True
        else:
            collision = False
        return collision

    def update(self, dt):
        # sub-classes must override
        pass