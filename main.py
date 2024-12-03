import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2 )
    
    
    while(True):
        screen.fill((0, 0, 0))
        for draw in drawables:
            draw.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updates in updatables:
            updates.update(dt)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000
    
    
if __name__ == "__main__":
    main()
