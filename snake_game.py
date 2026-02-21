import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000, 500
GRID_SIZE = 20
FPS = 12

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake
snake_radius = 10
snake_width = 2
snake_length = 1
snake_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2 
snake_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
snake_dx, snake_dy = 0, 0  # direction
snake_body = [(snake_x, snake_y)]


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
DEEP_NAVY = (0, 0, 128)
SOFT_WHITE = (255, 255, 240)

# Score
score = 0
font = pygame.font.SysFont(None, 24)

def draw_food():
    pygame.draw.circle(surface= screen, color= RED, center= (food_x, food_y), radius= food_radius, width= food_width)

def reset_game():
    global score, snake_x, snake_y, snake_dx, snake_dy, snake_length, food_x, food_y, snake_body
    score, snake_length = 0, 1
    snake_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_body = [(snake_x, snake_y)]
    snake_dx, snake_dy = 0, 0
    food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
    food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2


def background():
    screen.fill((DEEP_NAVY))

     # Draw vertical lines every GRID_SIZE pixels
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, SOFT_WHITE, (x, 0), (x, HEIGHT), 2)
    
    # Draw horizontal lines every GRID_SIZE pixels
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, SOFT_WHITE, (0, y), (WIDTH, y), 2)

def move_snake():
    global snake_x, snake_y, s
    snake_x += (snake_dx * GRID_SIZE)
    snake_y += (snake_dy * GRID_SIZE)

    new_head = (snake_x, snake_y)
    snake_body.insert(0, new_head)

    if len(snake_body) > snake_length:
        snake_body.pop()

    if (snake_x, snake_y) in snake_body[1:]:
        return True
    return False

def check_food_collision():
    return (snake_x  == food_x) and (snake_y == food_y) 

def grow_snake():
    global snake_body, snake_length
    snake_length += 1
    snake_body.append((snake_x, snake_y))

def draw_snake_body():
    for segment in snake_body:
        pygame.draw.circle(screen, GREEN, segment, snake_radius)

def update_score():
    global score, food_x, food_y
    if check_food_collision() == True:
        score += 1
        food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
        food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2



def check_collision():
    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        return True
    if (snake_x, snake_y) in snake_body[1:]:
        return True
    return False

def game_over():
    game_over_text = font.render("Game Over ! Press any key to restart", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2, HEIGHT // 2))
    pygame.display.flip()
    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == KEYDOWN:  
                reset_game()  
                waiting_for_restart = False  
            elif event.type == pygame.QUIT:  
                pygame.quit()
                exit()

# Infinite Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif (K_w == event.key or event.key == K_UP) and snake_dy == 0:
                snake_dx, snake_dy = 0, -1
            elif (K_s == event.key or event.key == K_DOWN) and snake_dy == 0:
                snake_dx, snake_dy = 0, 1
            elif (K_a == event.key or event.key == K_LEFT) and snake_dx == 0:
                snake_dx, snake_dy = -1, 0
            elif (K_d == event.key or event.key == K_RIGHT) and snake_dx == 0:
                snake_dx, snake_dy = 1, 0

    background()

    draw_snake_body()
    
    draw_food()
    
    if move_snake():
        game_over()
    
    if check_collision():
        game_over()
    
    if check_food_collision():
        update_score()
        grow_snake()
        
    clock.tick(FPS)

    pygame.display.flip()

pygame.quit()