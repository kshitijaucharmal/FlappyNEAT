import pygame

# Game
win_width = 551
win_height = 720

pop_size = 100

# Images
bird_images = [
    pygame.image.load("assets/bird_down.png"),
    pygame.image.load("assets/bird_mid.png"),
    pygame.image.load("assets/bird_up.png"),
]
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

bird_start_position = (100, 250)
x_pos_ground, y_pos_ground = 0, 520
scroll_speed = 3
score = 0

GAME_STOPPED = True
game_over = False

n_inputs = 4
n_outputs = 2
