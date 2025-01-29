import pygame
from circleshape import (CircleShape, )
from constants import(PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_TURN_SPEED,PLAYER_SPEED, PLAYER_SHOOT_SPEED)
from shoot import Shot



#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)
        #sub-classes must override
        
    #Rotate update Pressing Keys
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
            #?
        if keys[pygame.K_d]:
            self.rotate(dt)
            #?
        if keys[pygame.K_w]:
            self.move(dt) 
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            new_shot = self.shoot()
            self.shots_group.add(new_shot) 

    #Rotation Function 
    def rotate(self, dt): 
        self.rotation += PLAYER_TURN_SPEED * dt

    #UP and Down Movement
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    
    def shoot(self):
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        
        # Calculate the spawn position at the tip of the triangle
        spawn_offset = direction * (self.radius)  # Offset by the radius
        spawn_position = self.position + spawn_offset
        
        velocity = direction * PLAYER_SHOOT_SPEED
        shot = Shot(spawn_position.x, spawn_position.y, velocity)
        return shot

