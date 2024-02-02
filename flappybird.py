import pygame
x = pygame.init()

# Creating a window
gameWindow = pygame.display.set_mode((500, 800))
pygame.display.set_caption("My First Game")

# Game specific variables
exit_game = False
game_over = False

# creating a game loop
while not exit_game:
    for event in pygame.event.get():
        # quiting the game
        if event.type == pygame.QUIT:
            exit_game = True


pygame.quit()
quit()

