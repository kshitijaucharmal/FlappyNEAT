import pygame
import math
import random
import sys #to enable system commands

# files
from floor import Floor
from ball import Ball

WIDTH = 500
HEIGHT = 700

pygame.display.init()
pygame.display.set_caption('Colour Switch')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
ball_vel = 1

def floor_collision(floor, ball):
    c_bottom = ball.y + ball.r
    f_top = floor.rect.y
    sep = int(f_top - c_bottom)
    print('c_bottom=',c_bottom)
    print('f_top=',f_top)
    print('sep', sep)
    if sep == 0 or sep < 0:
        ball.landed()
        print('landed')
    else:
        print('no')

# def handle_collision(ball,floor):
#     # collided_objects = []
#     # for obj in objects:
#     if pygame.sprite.collide_rect(ball,floor): #instead of floor obj
#         if dy > 0:
#             #ball.rect.bottom = floor.rect.top
#             ball.landed()
        # elif dy < 0:
        #     ball.rect.top = floor.rect.bottom 
        #     ball.hit()   
        
        #collided_objects.append(obj)    
    
    #return collided_objects 
               
# Mainloop
def main(screen):
    clock = pygame.time.Clock() #for speed
    ball = Ball(250,600, screen)
    color = ball.ballcolor()
 
    run = True
    while run:
        screen.fill((0,0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #and ball.jump_count < 2:
                    ball.jump()
        
        ball.loop(FPS)
        ball.draw(color)    
        floor = Floor(0, 650, 500, 100, screen)
        
        floor_collision(floor,ball)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
        
if __name__=="__main__":
    main(screen)
