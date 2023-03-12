from neat.genome import Genome
from neat.geneh import GeneHistory

import random

class Species:
    def __init__(self, mem):
        self.members = []
        self.members.append(mem)
        self.rep = self.members[0]
        self.threshold = 3
        pass

    def add(self, brain):
        self.members.append(brain)
        if self.rep.fitness < brain.fitness:
            self.rep = self.members[-1]

    def check(self, brain):
        cd = self.rep.calculate_compatibility(brain)
        return cd < self.threshold

    def get_len(self):
        return len(self.members)

    def evaluate(self):
        self.fitness_sharing()
        self.members.sort(key=lambda x:x.adjusted_fitness, reverse=True)
        self.rep = self.members[0]
        print(len(self.members), self.members[0].fitness, self.members[0].adjusted_fitness)

        # replace each member with child of rep and a random one from the fitter half
        for i in range(len(self.members)):
            self.members[i] = self.rep.crossover(self.members[random.randint(0, len(self.members)//2)])
        pass

    def fitness_sharing(self):
        for i in range(len(self.members)):
            self.members[i].adjusted_fitness = self.members[i].fitness / len(self.members)
