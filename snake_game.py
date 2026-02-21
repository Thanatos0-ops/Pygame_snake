import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000, 500
GRID_SIZE = 20
BASE_FPS = 12
FPS = BASE_FPS
LEVEL = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake
snake_radius = 10
snake_length = 1
snake_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
snake_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
snake_dx, snake_dy = 0, 0  # direction
snake_body = [(snake_x, snake_y)]

# Food
food_radius = 10
food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DEEP_NAVY = (0, 0, 128)
SOFT_WHITE = (255, 255, 240)

# Score
score = 0
highscore = 0
font = pygame.font.SysFont(None, 24)


def draw_food():
    pygame.draw.circle(surface=screen, color=RED, center=(food_x, food_y), radius=food_radius)


def reset_game():
    global score, snake_x, snake_y, snake_dx, snake_dy, snake_length, food_x, food_y, snake_body, LEVEL, FPS
    score, snake_length = 0, 1
    FPS = BASE_FPS
    LEVEL = 1
    snake_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
    snake_body = [(snake_x, snake_y)]
    snake_dx, snake_dy = 0, 0
    food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
    food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2


def level():
    global FPS, LEVEL
    new_level = score // 5 + 1
    if new_level != LEVEL:
        LEVEL = new_level
        FPS = BASE_FPS + (LEVEL - 1) * 3


def background():
    screen.fill(DEEP_NAVY)
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, SOFT_WHITE, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, SOFT_WHITE, (0, y), (WIDTH, y), 1)


def move_snake():
    global snake_x, snake_y
    snake_x += snake_dx * GRID_SIZE
    snake_y += snake_dy * GRID_SIZE

    new_head = (snake_x, snake_y)
    snake_body.insert(0, new_head)

    if len(snake_body) > snake_length:
        snake_body.pop()

    if (snake_x, snake_y) in snake_body[1:]:
        return True
    return False


def check_food_collision():
    return snake_x == food_x and snake_y == food_y


def grow_snake():
    global snake_length
    snake_length += 1


def draw_snake_body():
    for segment in snake_body:
        pygame.draw.circle(screen, GREEN, segment, snake_radius)


def update_food():
    global food_x, food_y
    food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2
    food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE + GRID_SIZE // 2


def check_collision():
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        return True

    if (snake_x, snake_y) in snake_body[1:]:
        return True
    return False


def draw_hud():
    score_text = font.render(f"Score: {score}   Level: {LEVEL}   HighScore: {highscore}", True, WHITE)
    screen.blit(score_text, (10, 10))


def game_over():
    global highscore

    if score > highscore:
        highscore = score

    screen.fill(BLACK)
    game_over_text = font.render("Game Over! Press any key to restart", True, WHITE)
    score_text = font.render(f"Your Score: {score}", True, WHITE)
    highscore_text = font.render(f"HighScore: {highscore}", True, WHITE)

    # Center the text
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(highscore_text, (WIDTH // 2 - highscore_text.get_width() // 2, HEIGHT // 2 + 30))
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
            elif (event.key == K_w or event.key == K_UP) and snake_dy == 0:
                snake_dx, snake_dy = 0, -1
            elif (event.key == K_s or event.key == K_DOWN) and snake_dy == 0:
                snake_dx, snake_dy = 0, 1
            elif (event.key == K_a or event.key == K_LEFT) and snake_dx == 0:
                snake_dx, snake_dy = -1, 0
            elif (event.key == K_d or event.key == K_RIGHT) and snake_dx == 0:
                snake_dx, snake_dy = 1, 0

    self_collided = move_snake()

    boundary_hit = check_collision()

    background()
    draw_snake_body()
    draw_food()
    draw_hud()

    pygame.display.flip()
    clock.tick(FPS)

    if self_collided or boundary_hit:
        game_over()
    elif check_food_collision():
        grow_snake()
        score += 1
        update_food()
        level()

pygame.quit()
