import pygame
from pygame.locals import *
import random

pygame.init()

WIDTH, HEIGHT = 1000, 500
GRID_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake
snake_radius = 10
snake_width = 2
snake_lenght = 0
snake_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
snake_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
snake_dx, snake_dy = 0, 0  # direction


# Food
food_radius = 10
food_width = 2
food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2


# Colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Score
score = 0
font = pygame.font.SysFont(None, 24)

def draw_snake():
    pygame.draw.circle(surface= screen, color= GREEN, center= (snake_x, snake_y), radius= snake_radius, width= snake_width)

def draw_food():
    pygame.draw.circle(surface= screen, color= RED, radius= food_radius, width= food_width)

def reset_game():
    global score, snake_x, snake_y, snake_dx, snake_dy, snake_lenght, food_x, food_y
    score = 0
    snake_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_dx, snake_dy = 0, 0
    food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
    food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2


def background():
    for row in range(0, HEIGHT, GRID_SIZE):
        for col in range(0, WIDTH, GRID_SIZE):
            color = GRAY if (row // GRID_SIZE + col // GRID_SIZE) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (col, row, GRID_SIZE, GRID_SIZE))


# Infinite Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                snake_y -= 20
            elif event.key == K_DOWN:
                snake_y += 20
            elif event.key == K_LEFT:
                snake_x -= 20
            elif event.key == K_RIGHT:
                snake_x += 20

                



pygame.quit()