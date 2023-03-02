import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.surface = screen
        self.x= x
        self.y = y
        self.pos = (self.x, self.y)
        self.r = 8
        self.y_vel = 0
        self.fall_count=0
        self.jump_count=0
        self.jump_force = 6

        # color palette
        self.palette = ['red', 'blue', 'green', 'yellow']
        # Random color
        self.color = random.choice(self.palette)

        self.image = pygame.Surface((self.r*2, self.r*2), pygame.SRCALPHA)
        self.image.convert_alpha()
        self.rect = pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r)
        pass
        
    # Change ball color and return it
    def ballcolor(self):
        self.color = random.choice(self.palette)
        return self.color
    
    # jump
    def jump(self):
        self.y_vel = -self.jump_force
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
            self.jump_count = 0
  
    def move(self,dy):
        self.y += dy

    def loop(self, dt): 
        self.y_vel += min(0.7, (self.fall_count * dt) * self.jump_force)
        self.move(self.y_vel)
        self.fall_count +=1

    def draw(self, screen):
        screen.blit(self.image, (self.x-self.r/2, self.y))
