from enum import Enum


# class syntax
class Instruction(Enum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7
program = [2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0]

class Computer:
    def __init__(self, program, registers):
        self.program = program
        self.registerA = registers[0]
        self.registerB = registers[1]
        self.registerC = registers[2]
        self.ip = 0
        self.outputs = []

    def runProgram(self,regvalue):
        self.ip = 0
        self.registerC = 0
        self.registerB = 0
        self.registerA = regvalue
        self.outputs = []
        while True:
            try:
                self.runInstruction(self.program[self.ip])
            except IndexError as e:
                #print("End of program / out of bounds")
                break

    def runInstruction(self, instruction):
        #self.printInfo("start", instruction)

        match Instruction(instruction):
            case Instruction.adv:
                numerator = self.registerA
                denominator = 2**self.parseLiteral()
                self.registerA = numerator // denominator

            case Instruction.bxl:
                self.registerB = self.registerB ^ self.parseLiteral(combo=False)

            case Instruction.bst:
                self.registerB = self.parseLiteral() % 8

            case Instruction.jnz:
                if self.registerA != 0:
                    self.ip = self.parseLiteral(combo=False)
                    #self.printInfo("start", instruction)
                    return
            case Instruction.bxc:
                self.registerB = self.registerB ^ self.registerC
            case Instruction.out:
                self.outputs.append(self.parseLiteral() % 8)
            case Instruction.bdv:
                numerator = self.registerA
                denominator = 2**self.parseLiteral()
                self.registerB = numerator // denominator
            case Instruction.cdv:
                numerator = self.registerA
                denominator = 2**self.parseLiteral()
                self.registerC = numerator // denominator
                
        self.ip += 2
        #self.printInfo("end", instruction)

    def printInfo(self, whichOne, instruction):
        if whichOne == "start":
            print(f"==== Running instruction [{Instruction(instruction).name}] ====")
            print(f"Register A : {self.registerA}")
            print(f"Register B : {self.registerB}")
            print(f"Register C : {self.registerC}")
            print(f"Instruction pointer : {self.ip}")
        elif whichOne == "end":
            print(f"==== End instruction [{Instruction(instruction).name}] ====")
            print(f"Register A : {self.registerA}")
            print(f"Register B : {self.registerB}")
            print(f"Register C : {self.registerC}")
            print(f"Instruction pointer : {self.ip}")

    def parseLiteral(self, combo=True):
        lit = self.program[self.ip + 1]
        if combo:
            if lit < 0 or lit > 6:
                raise ValueError("Literal out of range")

            if lit <= 3:
                return lit
            elif lit == 4:
                return self.registerA
            elif lit == 5:
                return self.registerB
            elif lit == 6:
                return self.registerC
        else:
            return lit

from time import sleep
program = [2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0]
registers = [0, 0, 0]

binString = ''
numToCheck = 0
c = Computer(program, registers)
for out in range(1,3):
    print(out)
    res = -1
    while res != program[-out] or c.outputs != program[-out:]:
        numToCheck+=1
        registers[0] = numToCheck
        c.runProgram(numToCheck)
        
        res = c.outputs[-out]
    print(numToCheck)
    print(c.outputs)
    numToCheck*=8


265601188299675
c.runProgram(265601188299675)
print(c.outputs)
print("end")
quit()

    


# lowerBound = 0
# upperBound = 0
# swing = 10000000000000
# registerValue = 1
# programLen = len(program)
# while True:
#     if c.outputs == program:
#         print("Hallelujah")
#     elif registerValue % 1000:
#         registers[0] = registerValue
#         c = Computer(program, registers)
#         c.runProgram()
#         outputLen = len(c.outputs)
#         sleep(0.05)
#         print(f"{registerValue} - {c.outputs} - {outputLen}")
 
    
#     if(programLen - outputLen) > 0:
#         registerValue+=swing*(programLen - outputLen)
#     elif(programLen - outputLen) < 0:
#         registerValue-=swing*(outputLen - programLen)
#     else:

#         lowerBound = registers[0]
#         upperBound = registers[0]
#         upperBoundFound = False
#         step = 1000000000000
        
#         # while not upperBoundFound:
#         #     registerValue += step
#         #     registers[0] = registerValue
#         #     c = Computer(program, registers)
#         #     c.runProgram()
#         #     print(f"UB : {upperBound} , step : {step}, diff {len(c.outputs), programLen}")
#         #     if(len(c.outputs)) == programLen:
#         #         step = abs(step)
#         #         upperBound = registers[0]
#         #         if(step < 100000000):
                    
#         #             upperBoundFound = True
                
#         #     else:
#         #         step = -abs(step)
             
#         #         if(step < -10000000):
#         #             step //= 10
                
#             #281474960000001 - ub
#             #281474970000001 - up
            
#         registers[0] = lowerBound
#         step = 1000000000000
#         lowerBoundFound = False
        
#         while not lowerBoundFound:
#             registerValue -= step
#             registers[0] = registerValue
#             c = Computer(program, registers)
#             c.runProgram()
#             print(f"LB : {lowerBound} , step : {step}, diff {len(c.outputs), programLen}")
#             if(len(c.outputs)) == programLen:
#                 step = abs(step)
#                 lowerBound = registers[0]
#                 if(step < 100):
                    
#                     lowerBoundFound = True
                
#             else:
#                 step = -abs(step)
#                 registers[0] = upperBound
#                 if(step < -10000000):
#                     step //= 10
                
#             #281474960000001 - ub
                
#         print(f"LB : {lowerBound} , UB : {upperBound}")
#         break
   