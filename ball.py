import pygame
import random

class Ball(pygame.sprite.Sprite):
    def ballcolor(self):
        Palette=['red','blue','green','yellow']
        x=random.choice(Palette)
        return x
    
    def __init__(self,x,y, screen):
        self.surface=screen
        self.x= x
        self.y = y
        self.pos = (self.x, self.y)
        self.r= 25
        self.y_vel = 0
        self.fall_count=0
        self.jump_count=0
        self.gravity = 1
        
    def jump(self):
        self.y_vel = -self.gravity * 8
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
            self.jump_count = 0
  
    def move(self,dy):
        self.y += dy
        
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
        self.y = 625
        print (self.jump_count,self.y_vel,self.fall_count)
        
    def loop(self,fps): 
        self.y_vel += min(1,(self.fall_count / fps) * self.gravity)
        self.move(self.y_vel)
        self.fall_count +=1
                
    def draw(self,color):
        self.pos = (self.x,self.y)
        pygame.draw.circle(self.surface,color, self.pos, self.r)
