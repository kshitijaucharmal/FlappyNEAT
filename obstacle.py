import pygame
import random
import sys

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        self.screen = screen
        self.screen_width = screen.get_rect().w
        self.screen_height = screen.get_rect().h
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.r = 250
        self.line_width = 6
        self.Shapes = ['square', 'line', 'cross']
        self.Palette = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow']

        self.shape = self.obs_shape()
        self.color = self.obs_color()
        
        self.draw_obstacle(screen, random.choice([True, False]))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        pass

    def obs_color(self):
        index = random.randint(0,4)
        r = self.Palette[index]
        s = self.Palette[index+1]
        t = self.Palette[index+2]
        u = self.Palette[index+3]
        return r, s, t, u

    def draw(self):
        self.screen.blit(self.image, self.pos)
        # Debuggin circle
        # pygame.draw.circle(self.image, (0, 0, 0), self.image.get_rect().center, 10)

    def draw_obstacle(self, screen, case):
        w = self.w
        h = self.h
        parts = []
        if self.shape == 'square':
            self.image = pygame.Surface((2*w+self.line_width, 2*h+self.line_width), pygame.SRCALPHA)
            x, y = self.image.get_rect().center
            parts.append(pygame.draw.line(self.image, self.color[0], (x-w, y-h), (x+w, y-h), self.line_width))
            parts.append(pygame.draw.line(self.image, self.color[1], (x+w, y-h), (x+w, y+h), self.line_width))
            parts.append(pygame.draw.line(self.image, self.color[2], (x+w, y+h), (x-w, y+h), self.line_width))
            parts.append(pygame.draw.line(self.image, self.color[3], (x-w, y+h), (x-w, y-h), self.line_width))
            self.pos = (self.x - w, self.y)

        elif self.shape == 'line':
            self.image = pygame.Surface((self.screen_width, self.line_width))
            x = 0
            y = self.y
            parts.append(pygame.draw.line(self.image, self.color[0], (x,   0), (100+x, 0), self.line_width))
            parts.append(pygame.draw.line(self.image, self.color[1], (100+x, 0), (200+x, 0), self.line_width))
            parts.append(pygame.draw.line(self.image, self.color[2], (200+x, 0), (300+x, 0), self.line_width))
            parts.append(pygame.draw.line(self.image, self.color[3], (300+x, 0), (400+x, 0), self.line_width))
            # Gonna need an extra part here for looping sideways
            self.pos = (0, y-h/2)

        # Cross
        else:
            self.image = pygame.Surface((10, 10))
            print('later')
            # if case:
            #     parts.append(pygame.draw.line(screen, self.color[0], (150, 125), (150, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[1], (225, 200), (150, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[2], (150, 275), (150, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[3], (75,  200), (150, 200), self.line_width))
            #     
            # else:
            #     parts.append(pygame.draw.line(screen, self.color[0], (250, 125), (250, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[1], (325, 200), (250, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[2], (250, 275), (250, 200), self.line_width))
            #     parts.append(pygame.draw.line(screen, self.color[3], (175, 200), (250, 200), self.line_width))


    def obs_shape(self):
        self.shape = random.choice(self.Shapes)
        return self.shape
