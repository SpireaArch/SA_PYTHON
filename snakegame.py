import pygame
pygame.init()

#color
white =(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

# making window of a game
screen_width= 400
screen_height=800
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# adding name to the application
pygame.display.set_caption("SnakeGame")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False

# making game loops
while not exit_game:
    for event in pygame.event.get():
        print(event)
    

    gameWindow.fill


    


