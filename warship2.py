import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player_size = 50
player_speed = 5
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 2 * player_size, player_size, player_size)

# Enemy
enemy_size = 50
enemy_speed = 7
enemies = []

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warship Game")
clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load('ship.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load player image
player_image = pygame.image.load('players.png')
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Load enemy image
enemy_image = pygame.image.load('enemy.png')
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

def draw_player():
    screen.blit(player_image, player)

def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_image, enemy)

def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            spawn_enemy()

def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(-HEIGHT, 0)
    enemy = pygame.Rect(x, y, enemy_size, enemy_size)
    enemies.append(enemy)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH - player_size:
            player.x += player_speed

        screen.blit(background_image, (0, 0))  # Draw background image

        move_enemies()
        draw_enemies()
        draw_player()

        # Collision detection
        for enemy in enemies:
            if player.colliderect(enemy):
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    spawn_enemy()  # Initial enemy spawn
    main()
