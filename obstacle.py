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
        index = random.randint(0,4)
        r = self.Palette[index]
        s = self.Palette[index+1]
        t = self.Palette[index+2]
        u = self.Palette[index+3]
        return r, s, t, u

    def draw(self, screen, case):
        parts = []
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        if self.shape == 'square':
            parts.append(pygame.draw.line(screen, self.color[0], (x-w, y-h), (x+w, y-h), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[1], (x+w, y-h), (x+w, y+h), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[2], (x+w, y+h), (x-w, y+h), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[3], (x-w, y+h), (x-w, y-h), self.line_width))

        elif self.shape == 'line':
            parts.append(pygame.draw.line(screen, self.color[0], (0,   y), (100, y), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[1], (100, y), (200, y), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[2], (200, y), (300, y), self.line_width))
            parts.append(pygame.draw.line(screen, self.color[3], (300, y), (400, y), self.line_width))
            # Gonna need an extra part here for looping sideways

        elif self.shape == 'triangle':
            a = (x-2*w, y-h)
            b = (x, y+(3/2)*h)
            c = (x+2*w, y-h)
            parts.append(pygame.draw.line(screen, self.color[0], a, b, self.line_width))
            parts.append(pygame.draw.line(screen, self.color[1], b, c, self.line_width))
            parts.append(pygame.draw.line(screen, self.color[2], c, a, self.line_width))

        elif self.shape == 'circle':
            pos = (x, y)
            r = 50
            parts.append(pygame.draw.circle(screen, self.color[0], pos, r, self.line_width, draw_top_right=True))
            parts.append(pygame.draw.circle(screen, self.color[1], pos, r, self.line_width, draw_top_left=True))
            parts.append(pygame.draw.circle(screen, self.color[2], pos, r, self.line_width, draw_bottom_left=True))
            parts.append(pygame.draw.circle(screen, self.color[3], pos, r, self.line_width, draw_bottom_right=True))

        # Cross
        else:
            if case:
                parts.append(pygame.draw.line(screen, self.color[0], (150, 125), (150, 200), self.line_width))
                parts.append(pygame.draw.line(screen, self.color[1], (225, 200), (150, 200), self.line_width))
                parts.append(pygame.draw.line(screen, self.color[2], (150, 275), (150, 200), self.line_width))
                parts.append(pygame.draw.line(screen, self.color[3], (75,  200), (150, 200), self.line_width))
                
            else:
                parts.append(pygame.draw.line(screen, self.color[0], (250, 125), (250, 200), self.line_width))
                parts.append(pygame.draw.line(screen, self.color[1], (325, 200), (250, 200), self.line_width))
                parts.append(pygame.draw.line(screen, self.color[2], (250, 275), (250, 200), self.line_width))
                parts.append(pygame.draw.line(screen, self.color[3], (175, 200), (250, 200), self.line_width))
        return parts

    def obs_shape(self):
        self.shape = random.choice(self.Shapes)
        return self.shape
