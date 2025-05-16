registerToNumber = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "R16": 16,
    "R17": 17,
    "R18": 18,
    "R19": 19,
    "R20": 20,
    "R21": 21,
    "R22": 22,
    "R23": 23,
    "R24": 24,
    "R25": 25,
    "R26": 26,
    "R27": 27,
    "R28": 28,
    "R29": 29,
    "R30": 30,
    "R31": 31,
}

class ALU:
    def __init__(self, PC, registers, LR_Stack, Datamemory, Zflag):
        self.PC = PC
        self.registers = registers
        self.LR_Stack = LR_Stack
        self.DM = Datamemory
        self.Zflag = Zflag
        #Normally the instruction is processed by the entire ALU and the MUX chooses the output that will be forwarded
        #It made more sense to just select which function to run in Python
        self.instructionsMux = {
            "ADD": self.Add,
            "MUL": self.Multiply,       #multiply
            "DIV": self.Divide,         #divide
            "MOV": self.Move,           #move from register to register
            "IMOV": self.Move,         #Move an immediate value to register
            "LDR": self.Load,           #load from memory to register
            "ILDR": self.Load,         #load from memory with immediate address
            "STR": self.Store,          #store from register to memory
            "ISTR": self.Store,
            "CMP": self.Compare,
            "B": self.Branch,
            "BX": self.BranchReturn,
        }

    #ADD, dReg, sReg1, sReg2
    def Add(self, instruction):
        Destination = registerToNumber[instruction[1]]
        Operand1 = self.registers[registerToNumber[instruction[2]]]
        Operand2 = self.registers[registerToNumber[instruction[3]]]
        self.registers[Destination] = Operand1 + Operand2

    #MUL, dReg, sReg1, sReg2
    def Multiply(self, instruction):
        Destination = registerToNumber[instruction[1]]
        Operand1 = self.registers[registerToNumber[instruction[2]]]
        Operand2 = self.registers[registerToNumber[instruction[3]]]
        self.registers[Destination] = Operand1 * Operand2
    
    #DIV, dReg, sReg1, sReg2
    #Need logic to handle divide by 0
    def Divide(self, instruction):
        Destination = registerToNumber[instruction[1]]
        Operand1 = self.registers[registerToNumber[instruction[2]]]
        Operand2 = self.registers[registerToNumber[instruction[3]]]
        self.registers[Destination] = Operand1 / Operand2

    #MOV, dReg, sReg1
    def Move(self, instruction):
        if 'R' in instruction[2]:
            Destination = registerToNumber[instruction[1]]
            Source = registerToNumber[instruction[2]]
            self.registers[Destination] = self.registers[Source]
        else:
            Destination = registerToNumber[instruction[1]]
            ImmediateValue = int(instruction[2])
            self.registers[Destination] = ImmediateValue

    #IMOV, dReg, immediate
    #def iMove(self, instruction):
    #    Destination = registerToNumber[instruction[1]]
    #    ImmediateValue = int(instruction[2])
    #    self.registers[Destination] = ImmediateValue

    #LDR, dReg, [sReg]
    def Load(self, instruction):
        if 'R' in instruction[2]:
            Destination = registerToNumber[instruction[1]]
            SourceAddress = self.registers[registerToNumber[instruction[2]]]
            DataFetched = self.DM[SourceAddress]
            self.registers[Destination] = DataFetched
        else:
            Destination = registerToNumber[instruction[1]]
            ImmediateAddress = int(instruction[2])
            DataFetched = self.DM[ImmediateAddress]
            self.registers[Destination] = DataFetched
    
    #ILDR, dReg, [immediate]
    #def iLoad(self, instruction):
    #    Destination = registerToNumber[instruction[1]]
    #    ImmediateAddress = int(instruction[2])
    #    DataFetched = self.DM[ImmediateAddress]
    #    self.registers[Destination] = DataFetched

    #STR, sReg, [dReg]
    def Store(self, instruction):
        if 'R' in instruction[2]:
            RegisterData = self.registers[registerToNumber[instruction[1]]]
            StoreAddress = self.registers[registerToNumber[instruction[2]]]
            self.DM[StoreAddress] = RegisterData
        else:
            RegisterData = self.registers[registerToNumber[instruction[1]]]
            StoreAddress = int(instruction[2])
            self.DM[StoreAddress] = RegisterData

    #ISTR, sReg, immediate
    #def iStore(self, instruction):
    #    RegisterData = self.registers[registerToNumber[instruction[1]]]
    #    StoreAddress = int(instruction[2])
    #    self.DM[StoreAddress] = RegisterData

    #Normally Compare would set more flags, but in this simulation we only care about Zero flag
    def Compare(self, instruction):
        registerData1 = self.registers[registerToNumber[instruction[1]]]
        registerData2 = self.registers[registerToNumber[instruction[2]]]
        if registerData1 == registerData2:
            self.Zflag = 1
        else:
            self.Zflag = 0

    #B immediate
    def Branch(self, instruction):
        TargetAddress = int(instruction[1])
        self.LR_Stack.append(self.PC[0]+1)
        self.PC[0] = TargetAddress
    
    def BranchIfEqual(self, instruction):
        if self.Zflag[0] == 1: 
            TargetAddress = int(instruction[1])
            self.LR_Stack.append(self.PC[0]+1)
            self.PC[0] = TargetAddress

    #BX
    def BranchReturn(self, instruction):
        self.PC[0] = self.LR_Stack.pop()

    def ExecuteInstruction(self, instruction):
        operation = self.instructionsMux[instruction[0]]
        operation(instruction)


"""
    def Not(self, instruction):

    def ShiftLeft(self, instruction):

    def ShiftRight(self, instruction):

    def Branch(self, instruction):

    def BranchEqual(self, instruction):
"""
"""   
    "AND":      
    "ORR":       
    "XOR":      
    "NOT":      
    "SHL":      #shift left
    "SHR":      #shift right
    "BEQ":      #branch if equal
"""