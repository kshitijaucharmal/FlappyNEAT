import pygame
from globals import bird_images

from Bird import Bird

class Population:
    def __init__(self, pop_size=100):
        self.pop_size = pop_size
        self.population = pygame.sprite.Group()
        for _ in range(self.pop_size):
            self.population.add(Bird(bird_images))
        pass

    def update(self, user_input):
        # Update Bird population
        for bird in self.population:
            bird.update(user_input)
        pass

    def draw(self, window):
        self.population.draw(window)
        pass

    def all_dead(self):
        for s in self.population.sprites():
            if s.alive:
                return False
        return True

    def collision(self, pipes, ground):
        bird_sprites = self.population.sprites()
        # Collision Detection
        for b in range(self.pop_size):
            collision_pipes = pygame.sprite.spritecollide(bird_sprites[b], pipes, False)
            collision_ground = pygame.sprite.spritecollide(bird_sprites[b], ground, False)
            if collision_pipes or collision_ground:
                bird_sprites[b].alive = False
        pass
