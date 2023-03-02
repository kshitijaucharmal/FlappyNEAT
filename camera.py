import pygame

class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = self.simple_camera
        self.state = pygame.Rect(0, 0, width, height)
        self.HALF_WIDTH = width/2
        self.HALF_HEIGHT = height/2
        pass

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(target.rect)

    def simple_camera(self, target_rect):
        l, t, _, _ = target_rect # l = left,  t = top
        _, _, w, h = self.state      # w = width, h = height
        return pygame.Rect(-l+self.HALF_WIDTH, -t+self.HALF_HEIGHT, w, h)
