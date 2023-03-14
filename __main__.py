# libraries used
import pygame
import random

# NEAT Files
from neat.genome import Genome
from neat.geneh import GeneHistory
from neat.population import Population

WIDTH = 400
HEIGHT = 400
NNWIDTH = WIDTH
NNHEIGHT = HEIGHT
FPS = 60
BGCOLOR = (11, 11, 11)

pygame.display.init()
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))
nn = pygame.Surface((NNWIDTH, NNHEIGHT), pygame.SRCALPHA, 32)
nn.convert_alpha()
pygame.display.set_caption("Flappy Bird AI")
clock = pygame.time.Clock()

population = Population(100, 6, 1)
sample_inputs = [(random.random()) for a in range(population.n_inputs)]

def keydown_event(brain, event):
    # Set ctr to show best members of population
    if event.key == pygame.K_n:
        population.next()
    if event.key == pygame.K_b:
        population.prev()
    
    if event.key == pygame.K_c:
        brain.add_gene()
    if event.key == pygame.K_a:
        brain.add_node()
    if event.key == pygame.K_m:
        brain.mutate()
    if event.key == pygame.K_o:
        print(brain.get_outputs(sample_inputs))

    if event.key == pygame.K_t:
        global g
        g = g.clone()

    if event.key == pygame.K_s:
        # Divide population in species
        population.speciate()
        # Evaluate each species
        for s in range(len(population.species)):
            population.species[s].evaluate()
        show = False

    if event.key == pygame.K_p:
        print(brain.get_outputs(sample_inputs))
        print(brain)

g = population.best
def mainloop():
    run = True
    while run:
        # Fill with background color
        main_screen.fill(BGCOLOR)
        nn.fill(BGCOLOR)

        # Show the best one
        g.show(nn)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keydown_event(population.best, event)

        # Draw neural network
        main_screen.blit(nn, (0, 0))

        # Updating
        pygame.display.update()
        clock.tick(FPS)
    pass

if __name__ == "__main__":
    mainloop()
