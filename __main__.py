import pygame
from sys import exit
import random
from Bird import Bird
from Pipe import Pipe, PipePair
from Ground import Ground

from population import Population

from neat.genome import Genome
from neat.geneh import GeneHistory

# Importing images
from globals import *

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Segoe', 26)

# Window
window = pygame.display.set_mode((win_width, win_height))
nn = pygame.Surface((200, 200), pygame.SRCALPHA, 32)
nn = nn.convert_alpha()

def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

# Setup
# Instantiate Birds
population = Population(pop_size)
# pipes = pygame.sprite.Group()
pipes = []
x_top, x_bottom = 550, 550 #pt from where pipes enter

# Setup Pipes
pipe_timer = 0 # sets interval within which pipes will be spawn onto the screen

# Instantiate Initial Ground
x_pos_ground, y_pos_ground = 0, 520
ground = pygame.sprite.Group() #creating a sprite group
ground.add(Ground(x_pos_ground, y_pos_ground, ground_image)) #adding ground object to the abv grp

g = Genome(GeneHistory(n_inputs, n_outputs))

def reset():
    global pipes, pipe_timer, population, g
    population = Population(pop_size)
    pipes.clear()

    # Setup Pipes
    pipe_timer = 0 # sets interval within which pipes will be spawn onto the screen

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group() #creating a sprite group
    ground.add(Ground(x_pos_ground, y_pos_ground, ground_image)) #adding ground object to the abv grp
    g = Genome(GeneHistory(n_inputs, n_outputs))
    pass

def spawn_pipes():
    global pipe_timer

    if population.all_dead():
        return

    if pipe_timer > 0:
        pipe_timer -= 1
        return

    # Spawn Pipes
    y_top = random.randint(-600, -480)
    top_height = random.randint(90, 130)
    y_bottom = y_top + top_height + bottom_pipe_image.get_height()

    top = y_top + bottom_pipe_image.get_height()
    bottom = y_bottom

    # Top Pipe
    top_pipe = Pipe(x_top, y_top, top_pipe_image, 'top')
    # Bottom Pipe
    bottom_pipe = Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom')

    # pipes.add(top_pipe)
    # pipes.add(bottom_pipe)

    pipes.append(PipePair(top_pipe, bottom_pipe))

    # Random time till next pipepair spawns
    pipe_timer = random.randint(80, 120)

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
        pipes_group = pygame.sprite.Group()
        for i in range(len(pipes)):
            pipes_group.add(pipes[i].top)
            pipes_group.add(pipes[i].bottom)
        population.collision(pipes_group, ground)

        # Remove unnecessary pipes
        for i in range(len(pipes)):
            if pipes[i].xPos <= -50:
                pipes.pop(i)
                break

        print(len(pipes))

        # Update - Pipes, Ground
        if not population.all_dead(): # bird.sprite.alive:
            for i in range(len(pipes)):
                pipes[i].update()
            ground.update()
        else:
            game_over = True

        # Update Bird population
        population.update()
        
        # Draw - Pipes, Ground and Bird
        pipes_group.draw(window)

        # Draw neural Network
        if not game_over and random.random() < 0.3:
            g.mutate()
        g.show(nn)

        ground.draw(window)
        population.draw(window)

        # Show Scorer 
        score_text = font.render('Score: ' + str(population.best_fitness), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20)) 

        # Show neural network
        window.blit(nn, (win_width-200, 0))

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
