from CPU_Class import CPU
import numpy as np

f = open("Instruction_Memory.txt")
instructions = f.read()
instructionMemory = [line for line in instructions.split('\n') if line.strip() != '']
f.close()

f = open("Data_Memory.txt")
data = f.read()
dataMemory = [int(line) for line in data.split('\n') if line.strip() != '']
f.close()

CPU1 = CPU(instructionMemory, dataMemory)

while True:

    instruction = CPU1.fetch()
    instruction = CPU1.decode(instruction)

    print(instruction)

    if instruction[0] == "ENDL":
        break
    CPU1.execute(instruction)

