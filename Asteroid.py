import pygame
from circleshape import CircleShape
from constants import WHITE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call CircleShape's __init__ with the parameters
        super().__init__(x, y, radius)
        
        # Create a surface for the asteroid (with transparent background)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        
        # Draw the circle onto the surface
        pygame.draw.circle(self.image, WHITE, (radius, radius), radius, 2)

    def update(self, dt):
        # Update position using parent's velocity
        self.position += self.velocity * dt
        # Update rect to match new position
        self.rect.center = (self.position.x, self.position.y)

        
