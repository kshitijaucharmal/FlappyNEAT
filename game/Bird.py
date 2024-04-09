import pygame

from neat.genome import Genome

from game.globals import win_width, win_height, bird_start_position, y_pos_ground


class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_images, gh, clone=False):
        pygame.sprite.Sprite.__init__(self)
        self.bird_images = bird_images
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = (
            0  # loops throughout the bird images list and animates the bird
        )
        self.vel = 0  # gravity
        self.flap = False  # Jump / Flap
        self.alive = True
        self.on_ground = False  # Collided with ground

        self.fitness = 0  # Fitness function
        self.gh = gh  # The genome history

        # Make brain and clone if not a clone
        if not clone:
            self.brain = Genome(gh)  # The genome that acts as a brain
            # Random mutations for brain at start
            for _ in range(10):
                self.brain.mutate()
        pass

    # Draw to screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pass

    def clone(self):
        child = Bird(self.bird_images, self.gh, True)
        child.brain = self.brain.clone()
        return child

    # Update each frame
    def update(self, pipes):
        # don't update if on ground
        if self.on_ground:
            return

        # Animate Bird
        if self.alive:
            self.image_index += 1
            self.fitness += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = self.bird_images[self.image_index // 10]
        # used to change the image of the bird for every 10 index
        # i.e. for image index between 0-9 : value = 0 - 1st image
        # 10-19 : value = 1 - 2nd image
        # 20-29 : value = 2 - 3rd image
        # and when it reaches 30 its value is reset to 0

        # Gravity and Flap
        self.vel += 0.5
        if (
            self.vel > 7
        ):  # to prevent the bird to fall faster than 7 pixels every iteration
            self.vel = 7
        if self.rect.y < 500:
            # to prevent collision with ground
            # to increment the value y only if it is not touching the ground
            self.rect.y += int(self.vel)
        else:
            self.on_ground = True
        if self.vel == 0:
            # at vel = 0 bird is at its highest pt of jump
            # setting flap = False ensures that user cannot press space bar/execute jump until the bird reaches its peak position
            self.flap = False

        # Rotate Bird
        self.image = pygame.transform.rotate(self.image, self.vel * -8)

        # Think
        closest = self.get_closest_pipe(pipes)  # Get Closest pipe
        inputs = self.get_inputs(closest)  # Get input w.r.t. closest pipe
        _input = self.think(inputs)  # Should flap or not

        # flap
        if _input and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7
        pass

    # if in a range, its the closest
    def get_closest_pipe(self, pipes):
        for p in pipes:
            if p.xPos < win_width / 2 and p.xPos > 80:
                return p
        return pipes[0]

    # Inputs
    def get_inputs(self, closest):
        inputs = []
        inputs.append((y_pos_ground - self.rect.y) / win_height)  # bird height
        inputs.append((closest.xPos - self.rect.x) / win_width)  # Dist from pipe
        inputs.append(
            (closest.topPos - self.rect.y) / win_height
        )  # Dist from bird to top Pipe
        inputs.append(
            (self.rect.y - closest.bottomPos) / win_height
        )  # Dist from bird to bottom Pipe
        return inputs

    def think(self, inputs):
        should_flap = False

        # Get outputs from brain
        outs = self.brain.get_outputs(inputs)
        # use outputs to flap or not
        if outs[1] > outs[0]:
            should_flap = True

        return should_flap
