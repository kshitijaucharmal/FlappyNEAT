import pygame
import random

class Player(pygame.sprite.Sprite):
    pygame.display.init()
    PLAYER = 'INC/Flappy Bird/gallery/sprites/bird.png'
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    def __init__(self,x,y):
        self.image = GAME_SPRITES['player']
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.center = (self.x,self.y) 
        self.playerVelY = -9
        self.playerMaxVelY = 10
        self.playerMinVelY = -8
        self.playerAccY = 1

        self.playerFlapAccv = -8 # velocity while flapping
        self.playerFlapped = False # It is true only when the bird is flapping
        
    def draw(self):
        screen.blit(self.image, self.rect)  
