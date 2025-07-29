import pygame
pygame.time.Clock()
#dt = pygame.time.Clock().tick(60) / 1000
from constants import *
from player import Player, PLAYER_RADIUS
from circleshape import * 
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    starting_asteroids()
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # Create groups
    asteroids_group = pygame.sprite.Group()
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = updatable_group, drawable_group
    Asteroid.containers = asteroids_group,updatable_group, drawable_group
    AsteroidField.containers = updatable_group
    Shot.containers = shots_group, updatable_group, drawable_group

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), 0)

    asteroid_field = AsteroidField()

    print(f"Player in drawable_group: {player in drawable_group}")
    print(f"Drawable group size: {len(drawable_group)}")

    #dt = pygame.time.Clock().tick(60)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = pygame.time.Clock().tick(60) / 1000
        screen.fill("black")
        #drawable_group.draw(screen)
        updatable_group.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collisions(player) == True:
                print(f"Game Over!")
            for shot in shots_group:
                if asteroid.collisions(shot) == True:
                    print(f"Asteroid hit by shot!")
                    asteroid.kill()
                    asteroid.split()
                    shot.kill()

        for sprite in drawable_group:
            #print("Drawing a sprite!")
            sprite.draw(screen)

        for shot in shots_group:
            shot.update(dt)

        pygame.display.flip()


def starting_asteroids():
    print("Starting Asteroids!")

if __name__ == "__main__":
    main()
