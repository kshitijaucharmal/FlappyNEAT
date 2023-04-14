import pygame
from sys import exit
import random

bird_start_position = (100, 250)
scroll_speed = 1

win_height = 720
win_width = 551

class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_images):
        pygame.sprite.Sprite.__init__(self)
        self.bird_images = bird_images
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0 #loops throught the bird images list and animates the bird
        self.vel = 0 #gravity
        self.flap = False #
        self.alive = True

    def update(self, user_input):
        #user_input is taken as an argument to check if the space bar is pressed while jump/flap
        
        # Animate Bird
        if self.alive:
            self.image_index += 1 
        if self.image_index >= 30:
            self.image_index = 0
        self.image = self.bird_images[self.image_index // 10] 
        #used to change the image of the bird for every 10 index
        #i.e. for image index between 0-9 : value = 0 - 1st image
        # 10-19 : value = 1 - 2nd image
        # 20-29 : value = 2 - 3rd image
        #and when it reaches 30 its value is reset to 0

        # Gravity and Flap
        self.vel += 0.5
        if self.vel > 7: # to prevent the bird to fall faster than 7 pixels every iteration
            self.vel = 7
        if self.rect.y < 500: 
            #to prevent collision with ground
            #to increment the value y only if it is not touching the ground
            self.rect.y += int(self.vel)
        if self.vel == 0:
            # at vel = 0 bird is at its highest pt of jump
            # setting flap = False ensures that user cannot press space bar/execute jump until the bird reaches its peak position
            self.flap = False

        # Rotate Bird
        self.image = pygame.transform.rotate(self.image, self.vel * -8)

        # User Input
        # to execute jump whenever the user presses space bar
        _input = user_input[pygame.K_SPACE]
        if random.random() < 0.05:
            _input = True
        else:
            _input = False
        if _input and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7
