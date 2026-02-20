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
snake_body = []


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
TEAL = (0, 200, 200)

# Score
score = 0
font = pygame.font.SysFont(None, 24)

def draw_snake():
    pygame.draw.circle(surface= screen, color= GREEN, center= (snake_x, snake_y), radius= snake_radius, width= snake_width)

def draw_food():
    pygame.draw.circle(surface= screen, color= RED, center= (food_x, food_y), radius= food_radius, width= food_width)

def reset_game():
    global score, snake_x, snake_y, snake_dx, snake_dy, snake_lenght, food_x, food_y
    score = 0
    snake_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_dx, snake_dy = 0, 0
    food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
    food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2


def background():
    screen.fill((GRAY))

     # Draw vertical lines every GRID_SIZE pixels
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, TEAL, (x, 0), (x, HEIGHT), 2)
    
    # Draw horizontal lines every GRID_SIZE pixels
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, TEAL, (0, y), (WIDTH, y), 2)

def move_snake():
    snake_x +=(snake_dx * GRID_SIZE)
    snake_y += snake_y + (snake_dy * GRID_SIZE)

def check_food_collison():
    return (snake_x  == food_x) and (snake_y == food_y) 

def grow_snake():
    snake_body.append((snake_x, snake_y))

def draw_snake_body():
    for segment in snake_body:
        pygame.draw.circle(screen, GREEN, segment, snake_radius)

def update_score():
    global score
    if check_food_collison() == True:
        score += 1


def check_collison():
    if snake_x >= WIDTH: return True
    if snake_x <= 0: return True
    if snake_y >= HEIGHT: return True
    if snake_y <= 0: return True
    if (snake_x, snake_y) in snake_body: return True

def game_over():
    pass

# Infinite Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif K_w == event.key or event.key == K_UP:
                snake_dx, snake_dy = 0, -1
            elif K_s == event.key or event.key == K_DOWN:
                snake_dx, snake_dy = 0, 1
            elif K_a == event.key or event.key == K_LEFT:
                snake_dx, snake_dy = -1, 0
            elif K_d == event.key or event.key == K_RIGHT:
                snake_dx, snake_dy = 1, 0


    
    pygame.display.flip()



pygame.quit()