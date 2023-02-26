import pygame
import random
import sys

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        self.screen = screen
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.r = 250
        self.line_width = 5
        self.Shapes = ['square', 'line', 'triangle', 'circle', 'cross']
        self.Palette = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow']

        self.shape = self.obs_shape()
        self.color = self.obs_color()

    def obs_color(self):
        index = random.randint(0,len(self.Palette)-1)
        if index > 3:
            index -= 4
        r = self.Palette[index]
        s = self.Palette[index+1]
        t = self.Palette[index+2]
        u = self.Palette[index+3]
        return r, s, t, u

    def draw(self, screen, case):
        parts = []
        if self.shape == 'square':
            parts.append(pygame.draw.line(screen, self.color[0], (150, 150), (250, 150), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[1], (250, 150), (250, 250), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[2], (250, 250), (150, 250), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[3], (150, 250), (150, 150), self.line_width))

        elif self.shape == 'line':
            parts.append(pygame.draw.line(screen, self.color[0], (0,200), (100, 200), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[1], (100, 200), (200, 200), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[2], (200, 200), (300, 200), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[3], (300, 200), (400, 200), self.line_width))

        elif self.shape == 'triangle':
            parts.append(pygame.draw.line(screen, self.color[0], (150, 150), (200, 200), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[1], (200, 200), (250, 150), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[2], (250, 150), (150,150), self.line_width))

        elif self.shape == 'circle':
            parts.append(pygame.draw.circle(screen, self.color[0], [200, 200], 50, 5, draw_top_right=True))
            parts.append(pygame.draw.circle(screen, self.color[1], [200, 200], 50, 5, draw_top_left=True))
            parts.append(pygame.draw.circle(screen, self.color[2], [200, 200], 50, 5, draw_bottom_left=True))
            parts.append(pygame.draw.circle(screen, self.color[3], [200, 200], 50, 5, draw_bottom_right=True))

        # else:
            # if case
            #     parts.append(pygame.draw.line(screen, self.color[0], (150, 125), (150, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[1], (225, 200), (150, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[2], (150, 275), (150, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[3], (75, 200), (150, 200), self.line_width))
            #     
            # else:
            #     parts.append(pygame.draw.line(screen, self.color[0], (250, 125), (250, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[1], (325, 200), (250, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[2], (250, 275), (250, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[3], (175, 200), (250, 200), self.line_width))
        return parts

    def obs_shape(self):
        self.shape = random.choice(self.Shapes)
        return self.shape
