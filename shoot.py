import pygame
from circleshape import CircleShape
from constants import SHOOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOOT_RADIUS)
        self.velocity = velocity
        
        # Create a surface for the shot
        self.image = pygame.Surface((SHOOT_RADIUS * 2, SHOOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (SHOOT_RADIUS, SHOOT_RADIUS), SHOOT_RADIUS)  # Draw white circle
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        # Update position using velocity
        self.position += self.velocity * dt
        # Update rect to match position
        self.rect.center = self.position