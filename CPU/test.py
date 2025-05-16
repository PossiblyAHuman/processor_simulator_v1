import pygame
import numpy as np

print("test")

WIDTH, HEIGHT = 500, 500
MATRIX_WIDTH, MATRIX_HEIGHT = 100, 100

PIXEL_SIZE = WIDTH // MATRIX_WIDTH

pygame.init()
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Video Matrix Display")

clock = pygame.time.Clock()



