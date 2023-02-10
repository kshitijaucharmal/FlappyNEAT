from genome import Genome
from geneh import GeneHistory
from population import Population
import pygame
from pygame.locals import *
import random

population = Population(100, 4, 2)

WIDTH = 400
HEIGHT = 400

pygame.display.init()
ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test')

def setup():
    # brains[0].calculate_compatibility(brains[1])
    pass

def keydown_event(brain, event):
    # Set ctr to show best members of population
    if event.key == K_n:
        population.next()
    if event.key == K_b:
        population.prev()
    
    if event.key == K_c:
        brain.add_gene()
    if event.key == K_a:
        brain.add_node()
    if event.key == K_m:
        brain.mutate()
    if event.key == K_o:
        print(brain.get_outputs([0.1, 0.2, 0.3, 0.4]))

    print(brain.get_outputs([0.1, 0.2, 0.3, 0.4]))
    print(brain)

def mainloop():
    setup()
    global ctr
    run = True
    while run:
        ds.fill((255, 255, 255))
        population.best.show(ds)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                keydown_event(population.best, event)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    mainloop()
