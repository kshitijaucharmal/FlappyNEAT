import pygame
from sys import exit
import random

# Game Files
from game.Pipe import Pipe, PipePair
from game.Ground import Ground
from game.population import Population

# NEAT Files
from neat.genome import Genome
from neat.geneh import GeneHistory

# Importing global constants
from game.globals import *

pygame.init()
clock = pygame.time.Clock()
# Set Font
font = pygame.font.SysFont("Segoe", 26)

# Current Generation
generation = 1

# Window
window = pygame.display.set_mode((win_width, win_height))

# Display for neural network
nn = pygame.Surface((200, 200), pygame.SRCALPHA, 32)
nn = nn.convert_alpha()


def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
            if event.key == pygame.K_q:
                pygame.quit()
                exit()


# Setup
gh = GeneHistory(n_inputs, n_outputs)
# To show the best performing brain
g = Genome(gh)

# Instantiate Population of birds
population = Population(n_inputs=4, n_outputs=2, pop_size=pop_size)
pipes = []
x_top, x_bottom = 550, 550  # pt from where pipes enter

# Setup Pipes
pipe_timer = 0  # sets interval within which pipes will be spawn onto the screen

# Instantiate Initial Ground
ground = pygame.sprite.Group()  # creating a sprite group
ground.add(
    Ground(x_pos_ground, y_pos_ground, ground_image)
)  # adding ground object to the abv grp


def reset():
    global pipe_timer, g, game_over, generation
    game_over = False
    generation += 1
    population.reset()
    pipes.clear()

    # Setup Pipes
    pipe_timer = 0  # sets interval within which pipes will be spawn onto the screen

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()  # creating a sprite group
    ground.add(
        Ground(x_pos_ground, y_pos_ground, ground_image)
    )  # adding ground object to the abv grp
    g = Genome(gh)
    pass


def spawn_pipes():
    global pipe_timer

    # Return if everyone is dead
    if population.all_dead():
        return

    # While ctr > 0
    if pipe_timer > 0:
        # Count down
        pipe_timer -= 1
        return

    # Spawn Pipes
    y_top = random.randint(-600, -480)
    top_height = random.randint(90, 130)
    y_bottom = y_top + top_height + bottom_pipe_image.get_height()

    # top pos of pipe
    top = y_top + bottom_pipe_image.get_height()
    # bottom pos of pipe
    bottom = y_bottom

    # Top Pipe
    top_pipe = Pipe(x_top, y_top, top_pipe_image, "top")
    # Bottom Pipe
    bottom_pipe = Pipe(x_bottom, y_bottom, bottom_pipe_image, "bottom")

    # Add to pipes list
    pipes.append(PipePair(top_pipe, bottom_pipe, top, bottom))

    # Random time till next pipepair spawns
    pipe_timer = random.randint(50, 60)
    pass


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
        window.blit(skyline_image, (0, -400))

        # Game Over Management (Just reset)
        if game_over:
            reset()

        # Spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground, ground_image))

        # Spawn Pipes
        spawn_pipes()

        # Collision detection
        # Create pipes group
        pipes_group = pygame.sprite.Group()
        for i in range(len(pipes)):
            pipes_group.add(pipes[i].top)
            pipes_group.add(pipes[i].bottom)
        # Check Collision
        population.collision(pipes_group, ground)

        # Remove unnecessary pipes
        for i in range(len(pipes)):
            if pipes[i].xPos <= -50:
                pipes.pop(i)
                break

        # Update - Pipes, Ground
        if not population.all_dead():  # If not everyone is dead
            for i in range(len(pipes)):
                pipes[i].update()
            ground.update()
        else:
            game_over = True

        # Update Bird population
        best_bird = population.update(pipes)
        # Set showing genome to best birds' brain
        if best_bird != None:
            g = best_bird.brain

        # Draw - Pipes, Ground and Bird
        pipes_group.draw(window)

        # Draw neural Network
        g.show(nn)

        # Draw ground and birds
        ground.draw(window)
        population.draw(window)

        # Show Score
        score_text = font.render(
            "Score: " + str(population.best_fitness), True, pygame.Color(255, 255, 255)
        )
        window.blit(score_text, (20, 20))

        # Show Generation
        generation_text = font.render(
            "Generation: " + str(generation), True, pygame.Color(255, 255, 255)
        )
        window.blit(generation_text, (400, 20))

        # Show neural network
        window.blit(nn, (win_width - 200, 0))

        # Update with 60 FPS and update
        clock.tick(60)
        pygame.display.update()


# Menu
def menu():
    # Start Screen
    while GAME_STOPPED:
        quit_game()

        # Draw Menu
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, -400))
        window.blit(ground_image, Ground(0, 520, ground_image))
        window.blit(bird_images[0], (100, 250))
        window.blit(
            start_image,
            (
                win_width // 2 - start_image.get_width() // 2,
                win_height // 2 - start_image.get_height() // 2,
            ),
        )

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            # Start Game when space pressed
            main()

        pygame.display.update()


# Run only if this file is executed
if __name__ == "__main__":
    menu()
