import pygame
import random

# Import bird images
from game.globals import bird_images

# Bird class
from game.Bird import Bird

# Neat
from neat.geneh import GeneHistory
from neat.genome import Genome
from neat.species import Species


class Population:
    def __init__(self, n_inputs, n_outputs, pop_size=100):
        self.pop_size = pop_size  # Size of population
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.gh = GeneHistory(n_inputs, n_outputs)

        self.population = pygame.sprite.Group()  # Population is sprite group
        self.bird_images = bird_images  # Bird images

        # Populate with new birds
        for _ in range(self.pop_size):
            self.population.add(Bird(bird_images, self.gh))

        # Best bird ever in current generation
        self.best_fitness = 0

        self.best_index = 0
        # self.best = self.population.sprites()[self.best_index]
        self.species = []
        self.global_avg = 0
        pass

    def set_allowed_offspring(self):
        # Calculate fitness here
        ###################

        total_fitness = 0
        for i in range(len(self.species)):
            self.species[i].adjust_fitness()
            total_fitness += self.species[i].get_average_fitness()

        self.global_avg = total_fitness / len(self.species)
        for i in range(len(self.species)):
            self.species[i].allowed_offspring = round(
                self.species[i].average_fitness
                / self.global_avg
                * len(self.species[i].members)
            )

    def speciate(self):
        species_assigned = [(False) for _ in range(len(self.population))]
        self.species.clear()

        parents = self.population.sprites()

        while False in species_assigned:
            # select random indi
            p = random.randint(0, self.pop_size - 1)
            while species_assigned[p]:
                p = random.randint(0, self.pop_size - 1)

            # Set it as the rep of species
            rep = parents[p].brain
            sp = Species(rep)
            species_assigned[p] = True

            # Check against others
            for i in range(self.pop_size):
                if i == p or species_assigned[i]:
                    continue
                if sp.check(parents[i].brain):
                    sp.add(parents[i].brain)
                    species_assigned[i] = True
                pass
            self.species.append(sp)

        # l = [(len(sp.members)) for sp in self.species]
        # print(l)
        pass

    # Reset to previous state
    def reset(self):
        parents = self.population.sprites()
        # Sort parents
        parents.sort(key=lambda x: x.brain.fitness, reverse=True)

        self.speciate()
        self.set_allowed_offspring()

        self.population.empty()

        new_pop = []
        sp_lens = []
        for sp in self.species:
            sp_lens.append(len(sp.members))
            for _ in range(sp.allowed_offspring):
                new_pop.append(sp.give_offspring())

        print(len(new_pop), sp_lens)

        # Just replace the brains, nothin else
        for i in range(self.pop_size):
            if i < len(new_pop):
                bird = Bird(self.bird_images, self.gh, True)
                bird.brain = new_pop[i]
                self.population.add(bird)
            else:
                bird = Bird(self.bird_images, self.gh, True)
                bird.brain = Genome(self.gh)
                self.population.add(bird)

        # Random Population
        # for _ in range(self.pop_size):
        #     parent1 = parents[random.randint(0, len(parents) // 10)]
        #     parent2 = parents[random.randint(0, len(parents) // 10)]
        #     bird = parent1.mate(parent2)
        #     bird.brain.mutate()
        #     self.population.add(bird)

        self.best_fitness = 0
        pass

    # Update every frame
    def update(self, pipes):
        self.best_bird = None
        # Update Bird population
        for bird in self.population:
            bird.update(pipes)
            # Set the best bird
            if bird.brain.fitness > self.best_fitness:
                self.best_fitness = bird.brain.fitness
                self.best_bird = bird
        return self.best_bird

    # Draw population
    def draw(self, window, only_show_best=False):
        if only_show_best and self.best_bird:
            self.best_bird.draw(window)
            return
        for bird in self.population:
            if not bird.on_ground:
                bird.draw(window)
        pass

    # Check if all are dead
    def all_dead(self):
        for s in self.population.sprites():
            # False if even 1 is alive
            if s.alive:
                return False
        return True

    # Collision handling
    def collision(self, pipes, ground):
        bird_sprites = self.population.sprites()
        # Collision Detection
        for b in range(self.pop_size):
            # Collision with pipes
            collision_pipes = pygame.sprite.spritecollide(bird_sprites[b], pipes, False)
            # Collision with grounds
            collision_ground = pygame.sprite.spritecollide(
                bird_sprites[b], ground, False
            )
            # kill bird either way :)
            if collision_pipes or collision_ground:
                bird_sprites[b].alive = False
        pass
