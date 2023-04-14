import pygame
from sys import exit
import random
ground_image = pygame.image.load("assets/ground.png")
scroll_speed = 1
win_height = 720
win_width = 551

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) #initialising the base class
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()
