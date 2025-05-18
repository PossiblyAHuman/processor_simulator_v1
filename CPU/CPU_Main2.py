from CPU_Class import CPU
import pygame
import numpy as np
from datetime import datetime

f = open("Instruction_Test.txt")
instructions = f.read()
instructionMemory = [line for line in instructions.split('\n') if line.strip() != '']
f.close()

f = open("Data_Memory.txt")
data = f.read()
dataMemory = [int(line) for line in data.split('\n') if line.strip() != '']
f.close()

CPU1 = CPU(instructionMemory, dataMemory)

WIDTH, HEIGHT = 500, 500
MATRIX_WIDTH, MATRIX_HEIGHT = 50, 50
PIXEL_SIZE = WIDTH // MATRIX_WIDTH

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Video Matrix Display")

clock = pygame.time.Clock()

matrix = CPU1.VideoBuffer

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            CPU1.UART[0] = event.key
            CPU1.VideoBuffer = np.random.randint(0, 256, (MATRIX_HEIGHT, MATRIX_WIDTH), dtype=np.uint8)
            print(event.key)
            print("uart",CPU1.UART)

    CPU1.VideoPause[0] = True

    while CPU1.VideoPause[0]:
        instruction = CPU1.fetch()
        instruction = CPU1.decode(instruction)
        print(instruction)
        print(CPU1.registers)
        if instruction[0] == "ENDL":
            running = False
            break
        CPU1.execute(instruction)
    
    screen.fill((0, 0, 0))

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
    #now = datetime.now()
    #print("Current time:", now.strftime("%H:%M:%S"))
    clock.tick(1)  # Limit to 30 FPS

pygame.quit()
