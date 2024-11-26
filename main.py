import pygame
from constants import *
from player import Player

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # game setup
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # game loop
    while True:
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        
        #rendering
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #end of loop

if __name__ == "__main__":
    main()
