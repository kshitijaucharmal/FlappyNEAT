import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports

from Player import Player
from Pipes import Pipe

# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'INC/Flappy Bird/gallery/sprites/bird.png'
BACKGROUND = 'INC/Flappy Bird/gallery/sprites/background.png'
PIPE = 'INC/Flappy Bird/gallery/sprites/pipe.png'

pygame.display.init()
pygame.mixer.init()
pygame.display.set_caption('Flappy Bird')
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
FPSCLOCK = pygame.time.Clock()

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False

def welcomeScreen():
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame(SCREEN):
    score = 0
    basex = 0
    x = Player(int(SCREENWIDTH/5), int(SCREENWIDTH/2))
    Pipe = Pipe(SCREENHEIGHT, SCREENWIDTH)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if Player.y > 0:
                    Player.playerVelY = Player.playerFlapAccv
                    Player.playerFlapped = True
                    GAME_SOUNDS['wing'].play()


        crashTest = isCollide(Player.x, Player.y, Pipe.upperPipes, Pipe.lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            return     

        #check for score
        playerMidPos = Player.x + GAME_SPRITES['player'].get_width()/2
        for pipe in Pipe.upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                GAME_SOUNDS['point'].play()


        if Player.playerVelY <Player.playerMaxVelY and not Player.playerFlapped:
            Player.playerVelY += Player.playerAccY

        if Player.playerFlapped:
            Player.playerFlapped = False  
       
                      
        playerHeight = GAME_SPRITES['player'].get_height()
        Player.y = Player.y + min(Player.playerVelY, GROUNDY - Player.y - playerHeight)

        # move pipes to the left
        Pipe.move()
        # Add a new pipe when the first is about to cross the leftmost part of the screen
        Pipe.add()
        # if the pipe is out of the screen, remove it
        Pipe.remove()
                
        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        
        Pipe.obstacle_blit()
    
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        
        Player.draw()
        
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__ == "__main__":

    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('INC/Flappy Bird/gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('INC/Flappy Bird/gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] =pygame.image.load('INC/Flappy Bird/gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('INC/Flappy Bird/gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('INC/Flappy Bird/gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('INC/Flappy Bird/gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('INC/Flappy Bird/gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('INC/Flappy Bird/gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('INC/Flappy Bird/gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    
    welcomeScreen() # Shows welcome screen to the user until he presses a button
    mainGame(SCREEN) # This is the main game function 