from genome import Genome
from geneh import GeneHistory
import pygame
from pygame.locals import *
import random

gh = GeneHistory(4, 2)
brains = []

WIDTH = 400
HEIGHT = 400

pygame.display.init()
ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test')

ctr = 0
for i in range(2):
    brains.append(Genome(gh))
    for _ in range(random.randint(1, 50)):
        brains[i].mutate()

#def specieate():
    #pass

def setup():
    brains[0].calculate_compatibility(brains[1])
    pass

def mainloop():
    setup()
    global ctr
    run = True
    while run:
        ds.fill((255, 255, 255))
        brains[ctr].show(ds)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:

                if event.key == K_n:
                    ctr = ctr + 1 if ctr <= len(brains) - 2 else 0
                if event.key == K_b:
                    ctr = ctr - 1 if ctr > 0 else len(brains) - 1
                if event.key == K_c:
                    brains[ctr].add_gene()
                    print(brains[ctr].get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(brains[ctr])
                if event.key == K_a:
                    brains[ctr].add_node()
                    print(brains[ctr].get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(brains[ctr])
                if event.key == K_p:
                    print(brains[ctr])
                if event.key == K_m:
                    brains[ctr].mutate()
                    print(brains[ctr].get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(brains[ctr])
                if event.key == K_o:
                    print(brains[ctr].get_outputs([0.1, 0.2, 0.3, 0.4]))
                    print(brains[ctr])

                if event.key == K_s:
                    specieate()
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    mainloop()
