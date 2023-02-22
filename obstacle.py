import pygame
import random
import sys

width = 400
height = 400

pygame.display.init()
screen = pygame.display.set_mode((width, height))
FPS = 60

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        super(Floor, self).__init__()
        self.surface = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.draw.rect(self.surface,(255,255,255), pygame.Rect(self.x, self.y, self.w, self.h))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.surface = screen
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.r = 25

    def obs_colour(self):
        Palette=['red','blue','green','yellow']
        x=Palette[random.randint(0,len(Palette)-1)]
        return x

    def obs_shape(self):
        Shape=['rectangle', 'line', 'triangle', 'star']
        y=Shape[random.randint(0,len(Shape)-1)]
        return y

    def draw(self, colour, shape, screen):
        self.pos = (self.x, self.y)
        if shape == 'rectangle':
            pygame.draw.rect(screen, colour, [400, 400, 100, 50], width=10)
        elif shape == 'line':
            pygame.draw.line(screen, colour, (0,0), (400, 400))


def main(screen):
    clock = pygame.time.Clock()  # for speed

    obstacle = Obstacle(250, 200, screen)
    colour = obstacle.obs_colour()
    shape = obstacle.obs_shape()

    run = True
    while run:
        screen.fill((0, 0, 0))
        obstacle.draw(colour, shape, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main(screen)
