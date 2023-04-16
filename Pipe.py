import pygame
from sys import exit
import random

from globals import win_width, win_height, bird_start_position, scroll_speed

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type
        pass

    def update(self):
        # Move Pipe
        self.rect.x -= scroll_speed
        # Remove if out of screen
        if self.rect.x <= -win_width:
            self.kill()

        # Score
        # if self.pipe_type == 'bottom': # checking wrt bottom pipes
            # if bird_start_position[0] > self.rect.topleft[0] and not self.passed:
                # self.enter = True
            # if bird_start_position[0] > self.rect.topright[0] and not self.passed:
                # self.exit = True
            # if self.enter and self.exit and not self.passed:
                # self.passed = True
                # score += 1
        pass

class PipePair:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
        self.xPos = self.top.rect.topleft[0]
        pass

    def update(self):
        self.top.update()
        self.bottom.update()
        self.xPos = self.top.rect.topleft[0]
        pass
