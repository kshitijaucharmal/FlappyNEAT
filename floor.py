import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        super(Floor, self).__init__()
        # self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill('white')
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        pygame.draw.rect(self.image, (255,255,255), self.rect)
        pass

    def collide(self, ball):
        c_bottom = ball.y + ball.r
        f_top = self.y
        sep = int(f_top - c_bottom)
        if sep < 1:
            print('Below Ground level')
