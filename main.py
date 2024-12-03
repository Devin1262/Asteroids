import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2 )
    asteroid_field = AsteroidField()
    
    
    while(True):
        screen.fill((0, 0, 0))
        for draw in drawables:
            draw.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updates in updatables:
            updates.update(dt)
            
        for asteroid in asteroids:
            if asteroid.check_collisions(player1):
                print("Game over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()
                    score += 20
        
        text_surface = font.render("             Score : " + str(score), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (10, 10)
        screen.blit(text_surface, text_rect)            
                    
        pygame.display.flip()
        
        time_passed = clock.tick(60)
        dt = time_passed / 1000
    
    
if __name__ == "__main__":
    main()
