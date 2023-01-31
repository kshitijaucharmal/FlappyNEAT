from genome import Genome
from geneh import GeneHistory
import pygame
from pygame.locals import *

gh = GeneHistory(4, 2)
g = Genome(gh)

# print(g)

WIDTH = 400
HEIGHT = 400

pygame.display.init()
ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test')

def mainloop():
    run = True
    while run:
        ds.fill((255, 255, 255))
        g.show(ds)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
                if event.key == pygame.K_c:
                    g.add_gene()
                    print(g.get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(g)
                if event.key == pygame.K_n:
                    g.add_node()
                    print(g.get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(g)
                if event.key == pygame.K_p:
                    print(g)
                if event.key == pygame.K_m:
                    g.mutate()
                    print(g.get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(g)
                if event.key == pygame.K_o:
                    print(g.get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(g)
        pygame.display.update()
    pygame.quit()

mainloop()
