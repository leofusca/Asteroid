import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import Player



def main():
    #Pygame library init.
    pygame.init()
    #Screen Object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    #RGBA Color 
    BLACK = (0,0,0)  
    #Delta Time
    dt = 0
    #Clock Object
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    player1 = Player(x, y)   
    
    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

   
   #Game Loop 
    #Infinite Loop:
    while True:
        #Event in event retrieve.
        for event in pygame.event.get():
            #Quit button == loop break
            if event.type == pygame.QUIT:
                return
            
        #FPS
        dt = clock.tick(60) / 1000.0 

        #Player Movement   
        player1.update(dt)
        
            
        #Screen Filler     
        screen.fill(BLACK) 

        #Render Groups
        player1.draw(screen)
        #Screen Refresher
        pygame.display.flip()
        
        

    

if __name__ == "__main__":
    main() 
