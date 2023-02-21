import pygame
import random

width = 400
height = 400

pygame.display.init()
screen = pygame.display.set_mode((width, height))
FPS = 60

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Floor, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.draw.rect(screen,(255,255,255), pygame.Rect(self.x, y, self.w, self.h))

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x, y):
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

    def draw(self, colour, shape):
        self.pos = (self.x, self.y)
        if shape == 'rectangle':
            pygame.draw.rect(self.surface, colour, [400, 400, 100, 50], width=10)
        elif shape == 'line':
            pygame.draw.line(self.surface, colour, (0,1250))
        else:
            pygame.draw.circle(self.surface, colour, self.pos, self.r)


def main(screen):
    clock = pygame.time.Clock()  # for speed

    obstacle = Obstacle(250, 1200)
    colour = obstacle.obs_colour()
    shape = obstacle.obs_shape()

    while True:
        screen.fill((0, 0, 0))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        obstacle.draw(colour, shape)


        pygame.display.update()

if __name__ == "__main__":
    main(screen)