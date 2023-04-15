import pygame
from sys import exit
import random
from Bird import Bird
from Pipe import Pipe
from Ground import Ground

from population import Population

# Importing images
from globals import *

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Segoe', 26)

# Window
window = pygame.display.set_mode((win_width, win_height))

def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

# Setup
# Instantiate Birds
population = Population(100)
pipes = pygame.sprite.Group()
score = 0

# Setup Pipes
pipe_timer = 0 # sets interval within which pipes will be spawn onto the screen

# Instantiate Initial Ground
x_pos_ground, y_pos_ground = 0, 520
ground = pygame.sprite.Group() #creating a sprite group
ground.add(Ground(x_pos_ground, y_pos_ground, ground_image)) #adding ground object to the abv grp

def reset():
    global pipes, score, pipe_timer, population
    population = Population(100)
    pipes = pygame.sprite.Group()
    score = 0

    # Setup Pipes
    pipe_timer = 0 # sets interval within which pipes will be spawn onto the screen

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group() #creating a sprite group
    ground.add(Ground(x_pos_ground, y_pos_ground, ground_image)) #adding ground object to the abv grp
    pass

def spawn_pipes():
    global pipe_timer
    # Spawn Pipes
    if pipe_timer <= 0 and not population.all_dead():
        x_top, x_bottom = 550, 550 #pt from where pipes enter
        y_top = random.randint(-600, -480)
        top_height = random.randint(90, 130)
        y_bottom = y_top + top_height + bottom_pipe_image.get_height()

        top = y_top + bottom_pipe_image.get_height()
        bottom = y_bottom

        pipes.add(Pipe(x_top, y_top, top_pipe_image, 'top', top_pipe_image, bottom_pipe_image))
        pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom', top_pipe_image, bottom_pipe_image))
        pipe_timer = random.randint(80, 120)
    pipe_timer -= 1

# Game Main Method
def main():
    global game_over

    run = True
    while run:
        # Quit Event Check
        quit_game()

        # Get User Input
        user_input = pygame.key.get_pressed()

        # Draw Background
        window.blit(skyline_image, (0, 0))

        # Game Over Management
        if game_over:
            # Draw the game over screen
            window.blit(game_over_image, (win_width // 2 - game_over_image.get_width() // 2,
                                          win_height // 2 - game_over_image.get_height() // 2))
            if user_input[pygame.K_r]:
                reset()
                game_over = False
                break

        # Spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground, ground_image))

        # Spawn Pipes
        spawn_pipes()

        # Collision detection
        population.collision(pipes, ground)

        # Update - Pipes, Ground
        if not population.all_dead(): # bird.sprite.alive:
            pipes.update()
            ground.update()
        else:
            game_over = True

        # Update Bird population
        population.update(user_input)
        
        # Draw - Pipes, Ground and Bird
        pipes.draw(window)
        ground.draw(window)
        population.draw(window)

        # Show Scorer 
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20)) 

        # Pygame Stuff
        clock.tick(60)
        pygame.display.update()

# Menu
def menu():
    while GAME_STOPPED:
        quit_game()

        # Draw Menu
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, 0))
        window.blit(ground_image, Ground(0, 520, ground_image))
        window.blit(bird_images[0], (100, 250))
        window.blit(start_image, (win_width // 2 - start_image.get_width() // 2,
                                  win_height // 2 - start_image.get_height() // 2))

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()

if __name__ == "__main__":
    menu()
