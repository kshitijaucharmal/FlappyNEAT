import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        super(Floor, self).__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # self.rect = pygame.draw.rect(screen,(255,255,255), pygame.Rect(self.x, y, self.w, self.h))        

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.x, self.y, self.w, self.h))        
        pass

    def collide(self, ball):
        c_bottom = ball.y + ball.r
        f_top = self.y
        sep = int(f_top - c_bottom)
        if sep < 1:
            print('Below Ground level')
