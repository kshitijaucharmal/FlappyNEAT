import pygame
import random
import sys

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.r = 25
        self.shapes = ['rectangle', 'line', 'triangle', 'star']
        self.palette = ['red','blue','green','yellow']

        self.color = random.choice(self.palette)
        self.shape = random.choice(self.shapes)

    def obs_color(self):
        self.color = random.choice(self.palette)
        return self.color

    def obs_shape(self):
        self.shape = random.choice(self.shapes)
        return self.shape

    # Positions can be an array of any size according to points needed for drawing
    def draw(self, positions):
        # self.pos = (self.x, self.y)
        if self.shape == 'rectangle':
            pygame.draw.rect(self.screen, self.color, positions, width=10)
        elif self.shape == 'line':
            pygame.draw.line(self.screen, self.color, (positions[0], positions[1]), (positions[2], positions[3]))
        # elif self.shape == 'triangle':
        #     # Triangle Drawing
        #     pass
        # elif self.shape == 'star':
        #     # Star Drawing
        #     pass
        else:
            print("Not a valid shape")
            pygame.draw.circle(self.screen, self.color, (positions[0], positions[1]), 50)
        pass
