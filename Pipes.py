import pygame
import random

class Pipe(pygame.sprite.Sprite):
    pygame.display.init()
    PIPE = 'INC/Flappy Bird/gallery/sprites/pipe.png'
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha())
    def __init__(self, SCREENHEIGHT, SCREENWIDTH):
        self.image = GAME_SPRITES['pipe']
        self.offset = SCREENHEIGHT/3
        self.pipeX = SCREENWIDTH + 10
        self.pipeVelX = -4
        self.newPipe1 = self.getRandomPipe()
        self.newPipe2 = self.getRandomPipe()

        # List of upper pipes
        self.upperPipes = [
        {'x': SCREENWIDTH+200, 'y':self.newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':self.newPipe2[0]['y']},
        ]
        # List of lower pipes
        self.lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':self.newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':self.newPipe2[1]['y']},
        ]
 
    def getRandomPipe(self):
        
        #Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        
        self.pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        
        self.y2 = self.offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        
        self.y1 = self.pipeHeight - self.y2 + self.offset
        self.pipe = [
            {'x': self.pipeX, 'y': -(self.y1)}, #upper Pipe
            {'x': self.pipeX, 'y': self.y2} #lower Pipe
        ]
        return self.pipe
        
    def move(self):
        # move pipes to the left
        for self.upperPipe , self.lowerPipe in zip(self.upperPipes, self.lowerPipes):
            self.upperPipe['x'] += self.pipeVelX
            self.lowerPipe['x'] += self.pipeVelX
            
    def add(self):
        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<self.upperPipes[0]['x']<5:
            self.newpipe = self.getRandomPipe()
            self.upperPipes.append(self.newpipe[0])
            self.lowerPipes.append(self.newpipe[1])
            
    def remove(self):
        # if the pipe is out of the screen, remove it
        if self.upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            self.upperPipes.pop(0)
            self.lowerPipes.pop(0)
              
    def obstacle_blit(self):
        
        # Lets blit our sprites now
       
        for self.upperPipe, self.lowerPipe in zip(self.upperPipes, self.lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (self.upperPipe['x'], self.upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (self.lowerPipe['x'], self.lowerPipe['y']))

         
