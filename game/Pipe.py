import pygame

# Required global imports
from game.globals import win_width, scroll_speed

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.pipe_type = pipe_type # Top or bottom
        pass

    # Update every frame
    def update(self):
        # Move Pipe
        self.rect.x -= scroll_speed
        # Remove if out of screen
        if self.rect.x <= -win_width:
            self.kill()
        pass

# Class that holds two pipes, top and bottom
class PipePair:
    def __init__(self, top, bottom, topPos, bottomPos):
        self.top = top
        self.bottom = bottom
        self.xPos = self.top.rect.topleft[0]

        self.topPos = topPos
        self.bottomPos = bottomPos
        pass

    def update(self):
        self.top.update()
        self.bottom.update()
        self.xPos = self.top.rect.topleft[0]
        pass
