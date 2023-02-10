import pygame
from genome import Genome
from geneh import GeneHistory
import random

class Population:
    def __init__(self, pop_len, n_inputs, n_outputs):
        self.pop_len = pop_len
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.population = []
        self.gh = GeneHistory(n_inputs, n_outputs)

        for _ in range(pop_len):
            self.population.append(Genome(self.gh))
            # temp 
            for _ in range(random.randint(10, 50)):
                self.population[-1].mutate()

        self.best_index = 0
        self.best = self.population[self.best_index]
        pass
    
    # Heuristic for testing
    def next(self):
        self.best_index = self.best_index + 1 if self.best_index <= self.pop_len - 2 else 0
        self.best = self.population[self.best_index]
        print(self.best_index)
        pass

    def prev(self):
        self.best_index = self.best_index - 1 if self.best_index > 0 else self.best_index - 1
        self.best = self.population[self.best_index]
        print(self.best_index)
        pass
