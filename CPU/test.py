import pygame
import numpy as np

# --- Initialization ---
print("test")

WIDTH, HEIGHT = 500, 500
MATRIX_WIDTH, MATRIX_HEIGHT = 50, 50
PIXEL_SIZE = WIDTH // MATRIX_WIDTH

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Video Matrix Display")

clock = pygame.time.Clock()

# --- Create a test matrix ---
# Values between 0 and 255 (grayscale)
matrix = np.zeros((MATRIX_HEIGHT, MATRIX_WIDTH))
matrix[0,0] = 255
matrix[1,1] = 100
matrix[2,2] = 160
# --- Main loop ---
held_key = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.KEYDOWN:
        #    matrix = np.random.randint(0, 256, (MATRIX_HEIGHT, MATRIX_WIDTH), dtype=np.uint8)
        #    key_value = event.key
        #    print(key_value)
        #    print(type(key_value))
    held_key = 0
    keys = pygame.key.get_pressed()
    for key_code, is_pressed in enumerate(keys):
        if is_pressed:
            #print(f"Held key:", key_code)
            held_key = key_code
    
    print(held_key)
    # Clear screen
    screen.fill((0, 0, 0))

    # Draw matrix
    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            value = matrix[y, x]
            color = (value, value, value)  # Grayscale
            pygame.draw.rect(
                screen,
                color,
                (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
            )

    pygame.display.flip()
    clock.tick(30)  # Limit to 30 FPS

pygame.quit()
