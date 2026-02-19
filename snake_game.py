import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1000, 500))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

pygame.quit()