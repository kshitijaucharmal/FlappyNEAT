import pygame

WIDTH = 600
HEIGHT = 600
FPS = 60

pygame.display.init()
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird AI")
clock = pygame.time.Clock()

def mainloop():
    run = True
    while run:
        main_screen.fill((11, 11, 11))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        clock.tick(FPS)
    pass

if __name__ == "__main__":
    mainloop()
