import pygame
import random
# Import bird images
from game.globals import bird_images

# Bird class
from game.Bird import Bird

class Population:
    def __init__(self, gh, pop_size=100):
        self.pop_size = pop_size # Size of population
        self.population = pygame.sprite.Group() # Population is sprite group
        self.bird_images = bird_images # Bird images

        # Populate with new birds
        for _ in range(self.pop_size):
            self.population.add(Bird(bird_images, gh))
        
        # Gene History
        self.gh = gh
        # Best bird ever in current generation
        self.best_fitness = 0
        pass

    # Reset to previous state
    def reset(self):
        parents = self.population.sprites()
        # Sort parents
        parents.sort(key=lambda x : x.fitness, reverse=True)

        self.population.empty()

        # Random Population
        for i in range(self.pop_size):
            # Don't understand what is happening here, but converting this to int 
            # breaks the whole algorithm, and the birds don't learn
            bird = parents[random.randint(0, len(parents)/10)].clone()
            bird.brain.mutate()
            self.population.add(bird)

        self.best_fitness = 0
        pass

    # Update every frame
    def update(self, pipes):
        best_bird = None
        # Update Bird population
        for bird in self.population:
            bird.update(pipes)
            # Set the best bird
            if bird.fitness > self.best_fitness:
                self.best_fitness = bird.fitness
                best_bird = bird
        return best_bird

    # Draw population
    def draw(self, window):
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
            collision_ground = pygame.sprite.spritecollide(bird_sprites[b], ground, False)
            # kill bird either way :)
            if collision_pipes or collision_ground:
                bird_sprites[b].alive = False
        pass
