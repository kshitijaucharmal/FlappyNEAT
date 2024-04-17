import random


class Species:
    def __init__(self, mem):
        self.members = []
        self.members.append(mem)
        self.rep = self.members[0]
        self.max_members = 8
        self.threshold = 3.5

        self.average_fitness = 0
        self.allowed_offspring = 0

        # No. of generations species hasn't improved
        self.staleness = 0
        pass

    def add(self, brain):
        self.members.append(brain)
        # TODO: Check fitness and set as rep
        if self.rep.fitness < brain.fitness:
            self.rep = self.members[-1]
        pass

    # Get a random parent based on roulette wheel method, to give more priority to higer fitness members
    def get_random_parent(self):
        total_priority = sum([(m.adjusted_fitness) for m in self.members])
        selection = random.uniform(0, total_priority)
        current = 0
        for i, member in enumerate(self.members):
            current += member.adjusted_fitness
            if current >= selection:
                return self.members[i]

        print("Random parent not found, returning rep")
        return self.rep

    def give_offspring(self):
        parent1 = self.get_random_parent()
        parent2 = self.get_random_parent()
        child = parent1.crossover(parent2)
        child.mutate()
        return child

    def check(self, brain):
        done = False
        cd = self.rep.calculate_compatibility(brain)
        if cd < self.threshold and len(self.members) < self.max_members:
            done = True
        return done

    def adjust_fitness(self):
        for i in range(len(self.members)):
            self.members[i].adjusted_fitness = self.members[i].fitness / len(
                self.members
            )
        pass

    def get_average_fitness(self):
        self.average_fitness = sum([(g.adjusted_fitness) for g in self.members]) / len(
            self.members
        )
        return self.average_fitness
