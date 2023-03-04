from neat.genome import Genome
from neat.geneh import GeneHistory

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
        self.members.sort(key=lambda x:x.adjusted_fitness, reverse=True)
        print(len(self.members), self.members[0].adjusted_fitness)
        pass
