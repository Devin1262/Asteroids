import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.score = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position ,self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.score += 10
            return
        elif self.radius > (2 * ASTEROID_MIN_RADIUS):
            self.score += 50
        else:
            self.score += 20
        
        random_angle = random.uniform(20, 50)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
        
        