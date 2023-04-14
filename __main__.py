import pygame
from sys import exit
import random
from Bird import Bird
from Pipe import Pipe
from Ground import Ground

pygame.init()
clock = pygame.time.Clock()

# Window
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))

# Images
bird_images = [pygame.image.load("assets/bird_down.png"),
               pygame.image.load("assets/bird_mid.png"),
               pygame.image.load("assets/bird_up.png")]
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

# Game
scroll_speed = 1
bird_start_position = (100, 250)

font = pygame.font.SysFont('Roboto', 26)
game_stopped = True

def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

# Instantiate Bird
bird = pygame.sprite.Group()
for _ in range(100):
    bird.add(Bird(bird_images)) # adding the instance of class bird to the group

def all_dead():
    global bird
    for s in bird.sprites():
        if s.alive:
            return False
    return True

# Game Main Method
def main():
    global score  
    score = 0

    # Setup Pipes
    pipe_timer = 0 # sets interval within which pipes will be spawn onto the screen
    pipes = pygame.sprite.Group()

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group() #creating a sprite group
    ground.add(Ground(x_pos_ground, y_pos_ground, ground_image)) #adding ground object to the abv grp

    run = True
    while run:
        # Quit Event Check
        quit_game()

        # Get User Input
        user_input = pygame.key.get_pressed()

        # Draw Background
        window.blit(skyline_image, (0, 0))

        # Spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground, ground_image))

        # Draw - Pipes, Ground and Bird
        pipes.draw(window)
        ground.draw(window)
        bird.draw(window)

        # Update - Pipes, Ground and Bird
        if not all_dead(): # bird.sprite.alive:
            s = pipes.update()
            if s:
                score += 1
            ground.update()
        bird.update(user_input)
        
        # Show Scorer 
        #print('Score=',score)
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20)) 

        # Collision Detection
        for b in range(len(bird.sprites())):
            collision_pipes = pygame.sprite.spritecollide(bird.sprites()[b], pipes, False)
            collision_ground = pygame.sprite.spritecollide(bird.sprites()[b], ground, False)
            if collision_pipes or collision_ground:
                bird.sprites()[b].alive = False
                if not all_dead():
                    continue
                if collision_ground:
                    window.blit(game_over_image, (win_width // 2 - game_over_image.get_width() // 2,
                                                  win_height // 2 - game_over_image.get_height() // 2))
                    if user_input[pygame.K_r]:
                        break

        # Spawn Pipes
        if pipe_timer <= 0 and not all_dead():
            x_top, x_bottom = 550, 550 #pt from where pipes enter
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image, 'top', top_pipe_image, bottom_pipe_image))
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom', top_pipe_image, bottom_pipe_image))
            pipe_timer = random.randint(80, 120)
        pipe_timer -= 1

        clock.tick(60)
        pygame.display.update()

# Menu
def menu():
    global game_stopped
    
    while game_stopped:
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
