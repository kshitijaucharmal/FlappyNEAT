import pygame
import math
import random
import sys #to enable system commands

# files
from floor import Floor
from ball import Ball
from obstacle import Obstacle

WIDTH = 400
HEIGHT = 700
FPS = 60

pygame.display.init()
pygame.display.set_caption('Colour Switch')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Setup
ball = Ball(WIDTH/2,HEIGHT/2, screen)
ballColor = ball.ballcolor()
floor = Floor(0, 650, 500, 100, screen)
clock = pygame.time.Clock() #for speed
obstacle1 = Obstacle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, screen)
shape = obstacle1.obs_shape()

angle = 0
peach = (255, 175, 128)
green = (0, 104, 55)

# Mainloop
def main(screen):
    global angle
    run = True
    while run:
        screen.fill((0,0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #and ball.jump_count < 2:
                    ball.jump()
        
        floor.collide(ball)
        ball.loop(1/FPS)

        # Drawing
        ball.draw()
        floor.draw()
        parts = obstacle1.draw(screen, False)

        # for i in range(len(parts)):
            # rotated_part = pygame.transform.rotate(parts[i], angle)

        angle+=1

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
        
if __name__=="__main__":
    main(screen)
