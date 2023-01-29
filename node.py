import pygame
import math

class Node:
    def __init__(self, n, l):
        self.number = n
        self.layer = l
        self.output = 0
        self.in_genes = []
        self.sigmoid = lambda x : 1 / (1 + math.exp(-x))

        # For Showing
        self.color = (255, 255, 255)
        self.bcolor = (0, 0, 0)

        self.radius = 15
        self.border_radius = 2

        self.pos = [0, 0]
        self.font_size = 15
        pygame.font.init()
        self.font = pygame.font.SysFont('convergence', self.font_size)

        pass

    def clone(self):
        n = Node(self.number, self.layer)
        n.output = self.output
        return n

    def calculate(self):
        if self.layer == 0:
            print('No calculations for first layer')
            return

        s = 0
        for g in self.in_genes:
            if g.enabled:
                s += g.in_node * g.weight
        
        self.output = self.sigmoid(s)
        pass

    def show(self, ds):
        pygame.draw.circle(ds, self.bcolor, self.pos, self.radius + self.border_radius)
        pygame.draw.circle(ds, self.color, self.pos, self.radius)
        text = self.font.render(f'{self.number}({self.layer})', True, self.bcolor)
        textRect = text.get_rect()
        textRect.center = tuple(self.pos)
        ds.blit(text, textRect)
        pass
