import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):

        pass

    def update(self, dt):

        pass
    
    def check_collisions(self, object):
        distance = self.position.distance_to(object.position)
        if distance <= (self.radius + object.radius):
            return True #Colliding if true
        return False