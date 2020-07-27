 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 27/07/2020
 #    Version   : 1.0.1
 #    Purpose   : Cheat Codes & Home Screen In Pygame
 #    Input     : none
 #    Output    : Cheat Codes & Home Screen In Pygame
 #    ------------------------------------------------------------------------------------------

import pygame   #    import pygame module
import random  #   for food location
import os  #   for file checking

pygame.mixer.init() #   for sound

pygame.init()  #   start pygame

#   screen size input
screen_width = 600
screen_height = 400

# Colors
white = (255, 255, 255)
red = (255,0,77)
black = (0, 0, 0)
gameName = (255, 0, 77)
enterToPlay = (0,181,184)
quitGame = (254, 225, 26)
scoreHighScore = (254, 225, 26)
gameOver = (255, 0, 77)
enterToContinue = (90, 39, 193)
qToQuit = (39, 159, 0)
food = (255, 0, 77)

gameWindow = pygame.display.set_mode((screen_width, screen_height))  #   set game window size to 600 x 400

#   background image
backgroundImage = pygame.image.load("images/gameImage.png")
backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game")    #   set game name to Snake Game
pygame.display.update()

#   game icon
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#   game font
font = pygame.font.SysFont(None, 30)

#   snake fps
fps = 60
clock = pygame.time.Clock()

#   display score to screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

#   determine length size
def plot_snake(gameWindow, color, snk_list, snake_size):
    #   print(snk_list)
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size]) 

#   welcome screen
def welcome():

    #   play welcome music
    pygame.mixer.music.load('sounds/background.mp3')
    pygame.mixer.music.play()

    exit_game = False
    while not exit_game:

        #   welcome image
        welcomeImage = pygame.image.load("images/welcomeImage.png")
        welcomeImage = pygame.transform.scale(welcomeImage, (screen_width, screen_height)).convert_alpha()
        
        gameWindow.blit(welcomeImage, (0, 0))
        text_screen("Snake Game By Montasim", gameName, 170, 10)
        text_screen("Press Enter To Play", enterToPlay, 200, 342)
        text_screen("Press Q to Quit", quitGame, 215, 376)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
                
                if event.key == pygame.K_Q:
                    quit()

        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():

    #   play game music
    pygame.mixer.music.load('sounds/game.mp3')
    pygame.mixer.music.play()

    # Game specific variables
    exit_game = False
    game_over = False

    #   snake property
    snake_x = 80
    snake_y = 190
    velocity_x = 0
    velocity_y = 0

    #   food property
    food_x = random.randint(80, screen_width/2)
    food_y = random.randint(80, screen_height / 2)

    #   score property
    score = 0

    #   snake size and speed
    init_velocity = 2
    snake_size = 15

    snk_list = []
    snk_length = 1

    #   check if Hi Score.txt exists
    if (not os.path.exists("Hi Score.txt")):
        with open("Hi Score.txt", "w") as f:
            f.write("0")

    #   show high score
    with open("Hi Score.txt", "r", encoding='utf-8') as f:
        hiScore = f.read()
        f.close()

    while not exit_game:

        if game_over:
            
            #   write high score
            with open("Hi Score.txt", "w", encoding='utf-8') as f:
                f.write(str(hiScore))
                f.close()

            gameWindow.fill(black)
            text_screen("Score: " + str(score) + ", High Score: " + str(hiScore), scoreHighScore, 170, 150)
            text_screen("Game Over!", gameOver, 240, 175)
            text_screen("Press Enter To Continue", enterToContinue, 180, 200)
            text_screen("Press Q To Quit", qToQuit, 225, 225)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit_game = True
                    
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameloop()
                        
                        if event.key == pygame.K_Q:
                            quit()

                
                #   print(event)  #   prints all event in the game

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10

                #   food eat music
                pygame.mixer.music.load('sounds/foodeaten.mp3')
                pygame.mixer.music.play() 

                food_x = random.randint(80, screen_width / 2)
                food_y = random.randint(80, screen_height / 2)
                snk_length += 3

                #   change hiScore
                if score > int(hiScore):
                    hiScore = score

            gameWindow.fill(white)
            gameWindow.blit(backgroundImage, (0, 0))
            text_screen("Score: " + str(score) + ", High Score: " + str(hiScore), scoreHighScore, 155, 5)
            pygame.draw.rect(gameWindow, food, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            #   delete extra snake size
            if len(snk_list) > snk_length:
                del snk_list[0]

            #   if snake touch itself game over
            if head in snk_list[:-1]:
                game_over = True

                #   play snake touch itself music
                pygame.mixer.music.load('sounds/snaketouched.mp3')
                pygame.mixer.music.play()

            #   if snake touch border game over
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                #   print("Game Over")

                #   game over music
                pygame.mixer.music.load('sounds/gameover.mp3')
                pygame.mixer.music.play()

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
            
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()