from ALU import ALU
class CPU:
    def __init__(self, InstructionMemory, DataMemory):
        self.IM = InstructionMemory
        self.DM = DataMemory
        self.PC = [0]
        self.registers = [0] * 32
        #instead of a traditional Link Register and a separate stack to store return addresses, I just combined them onto the stack
        self.LR_Stack = []
        self.Zflag = [0]
        self.ALU = ALU(self.PC, self.registers, self.LR_Stack, self.DM, self.Zflag)
        self.VideoBuffer = [[0 for _ in range(50)] for _ in range(50)]
    
    def fetch(self):
        return self.IM[self.PC[0]]
    
    def decode(self, instruction):
        instruction = instruction.split(',')
        instruction = [s.replace(' ', '') for s in instruction]
        return instruction
    
    def execute(self, instruction):
        self.ALU.ExecuteInstruction(instruction)

        #increment counter if its not control logic
        if instruction[0] not in ["B", "BEQ", "BX"]:
            self.PC[0] = self.PC[0] + 1