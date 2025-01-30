import pygame
from circleshape import CircleShape
from constants import WHITE, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS
import random 



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

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 

            randomangle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(-randomangle)
            new_velocity2 = self.velocity.rotate(randomangle)
            radius = self.radius - ASTEROID_MIN_RADIUS

            new_velocity1 = new_velocity1 * 1.2
            new_velocity2 = new_velocity2 * 1.2 

            asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
            asteroid_1.velocity = new_velocity1
            asteroid_2 = Asteroid(self.position.x, self.position.y, radius)
            asteroid_2.velocity = new_velocity2

            for group in self.groups():
                group.add(asteroid_1)
                group.add(asteroid_2)

        
