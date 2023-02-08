import pygame
import math
import random
import sys #to enable system commands

pygame.init()

pygame.display.set_caption('Colour Switch')
screen = pygame.display.set_mode((500, 700))
FPS = 60
ball_vel = 1

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Floor, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.draw.rect(screen,(255,255,255), pygame.Rect(self.x, y, self.w, self.h))        

class Ball(pygame.sprite.Sprite):
    
    gravity = 1
    
    def ballcolor(self):
        Palette=['red','blue','green','yellow']
        x=Palette[random.randint(0,len(Palette)-1)]
        return x
    
    def __init__(self,x,y):
        self.surface=screen
        self.x= x
        self.y = y
        self.pos = (self.x, self.y)
        self.r= 25
        self.y_vel = 0
        self.fall_count=0
        self.jump_count=0
        
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
               

def main(screen):
        
    clock = pygame.time.Clock() #for speed
    
    ball = Ball(250,600)
    color = ball.ballcolor()
 
    while True:
        screen.fill((0,0,0))
        clock.tick(60)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #and ball.jump_count < 2:
                    ball.jump()
        
        ball.loop(FPS)
        
        ball.draw(color)    
        
        floor = Floor(0, 650, 500, 100)
        
        floor_collision(floor,ball)
            
           
        pygame.display.update()
        
if __name__=="__main__":
    main(screen)
  
