import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # game setup
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update logic
        for u in updatable:
            u.update(dt)
        
        for a in asteroids:
            if a.collides(player):
                print("Game over!")
                return
        
        #rendering
        screen.fill((0, 0, 0))
        
        #draw logic
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #end of loop

if __name__ == "__main__":
    main()
