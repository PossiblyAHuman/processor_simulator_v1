from CPU_Class import CPU

f = open("Instruction_Memory.txt")
instructions = f.read()
instructionMemory = [line for line in instructions.split('\n') if line.strip() != '']
f.close()

f = open("Data_Memory.txt")
data = f.read()
dataMemory = [int(line) for line in data.split('\n') if line.strip() != '']
f.close()

CPU1 = CPU(instructionMemory, dataMemory)
print("v", CPU1.VideoBuffer)
print("Reg Start:", CPU1.registers)
print("Data start:", CPU1.DM)
print("LR Stack Start:", CPU1.LR_Stack)

while True:
    instruction = CPU1.fetch()
    instruction = CPU1.decode(instruction)
    print(instruction)
    if instruction[0] == "ENDL":
        break
    CPU1.execute(instruction)
    print("Reg:", CPU1.registers)
    print("Data:", CPU1.DM)
    print("LR Stack:", CPU1.LR_Stack)

#Task2 Graphic storage and output
#Task2.1 Double buffer to avoid screen flicker during updating
#Task3 Text
#Task4 Simple pong game