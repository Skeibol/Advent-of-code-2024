import numpy as np
import re


class Machine:
    def __init__(self, parameters, ID):
        self.buttonA = parameters[0]
        self.buttonB = parameters[1]
        self.target = parameters[2]
        self.ID = ID
        self.weird = False
        pass

    def calculateButtonCost(self): # Not needed, every equation has one solution
        buttonAdist = np.sqrt(np.square(self.buttonA[0]) + np.square(self.buttonA[1]))
        buttonBdist = np.sqrt(np.square(self.buttonB[0]) + np.square(self.buttonB[1])) * 3
        if buttonAdist > buttonBdist:
            self.weird = True
            print("Damn found one")
            print(f"{buttonAdist} button A distance per 3 coin")
            print(f"{buttonBdist} button B distance per 3 coin")
            print()

    def identifyYourselfMachine(self):
        print(
            f"Im {self.ID} machine. Button A X {self.buttonA[0]} A Y {self.buttonA[1]} Button B X {self.buttonB[0]} B Y {self.buttonB[1]}. Target X {self.target[0]} Y {self.target[1]}"
        )
        
    def tryCalculateTarget(self):
        prize_x = self.target[0]
        prize_y = self.target[1] 
        AX = self.buttonA[0]
        AY = self.buttonA[1]
        BX = self.buttonB[0]
        BY = self.buttonB[1]
        A = (prize_x*BY - prize_y*BX) / (AX*BY - AY*BX)
        B = (AX*prize_y - AY*prize_x) / (AX*BY - AY*BX)
        if A.is_integer() and B.is_integer() :
            return A *3 + B
        else:
            return 0

        
        
    def tryReachTarget(self): # Doesnt work?
        targetX = self.target[0] 
        targetY = self.target[1] 
        buttonApushes = 0
        buttonBpushes = 0
        costs = []
        while targetX > 0 and targetY > 0:
            if not self.weird:
                if targetX % self.buttonB[0] == 0 and targetY % self.buttonB[1] == 0:
                    targetX -= self.buttonB[0]
                    targetY -= self.buttonB[1]
                    buttonBpushes += 1
                else:
                    targetX -= self.buttonA[0]
                    targetY -= self.buttonA[1]
                    buttonApushes += 1
            else:
                if targetX % self.buttonA[0] == 0 and targetY % self.buttonA[1] == 0:
                    targetX -= self.buttonA[0]
                    targetY -= self.buttonA[1]
                    buttonApushes += 1
                else:
                    targetX -= self.buttonB[0]
                    targetY -= self.buttonB[1]
                    buttonBpushes += 1
        if targetX == 0 and targetY == 0:
            # print(
            #     f"After {buttonApushes} A pushes, and {buttonBpushes} B pushes , target at : {targetX,targetY}"
            # )
            cost = (buttonApushes * 3) + (buttonBpushes)
            costs.append(cost)
    
        targetX = self.target[0] 
        targetY = self.target[1] 
        buttonApushes = 0
        buttonBpushes = 0
        while targetX > 0 and targetY > 0:
            if not self.weird:
                if targetX % self.buttonA[0] == 0 and targetY % self.buttonA[1] == 0:
                    targetX -= self.buttonA[0]
                    targetY -= self.buttonA[1]
                    buttonApushes += 1
                else:
                    targetX -= self.buttonB[0]
                    targetY -= self.buttonB[1]
                    buttonBpushes += 1
            else:
                if targetX % self.buttonB[0] == 0 and targetY % self.buttonB[1] == 0:
                    targetX -= self.buttonB[0]
                    targetY -= self.buttonB[1]
                    buttonBpushes += 1
                else:
                    targetX -= self.buttonA[0]
                    targetY -= self.buttonA[1]
                    buttonApushes += 1
        if targetX == 0 and targetY == 0:
            # print(
            #     f"After {buttonApushes} A pushes, and {buttonBpushes} B pushes , target at : {targetX,targetY}"
            # )
            cost = (buttonApushes * 3) + (buttonBpushes)
            costs.append(cost)
        
        if len(costs) == 0:
            return 0
        if len(costs) == 1:
            return costs[0]
        if costs[0] > costs[1]:
            return costs[0]
        else:
            return costs[1]
        


machines = []
with open("./advent-of-code/day13/input.txt", "r") as file:
    machineParameters = []
    for line in file:
        if line == "\n":
            continue

        x = re.findall("\\d+", line)
        machineParameters.append([int(x) for x in x])
        if len(machineParameters) == 3:
            machine = Machine(machineParameters, len(machines))
            machines.append(machine)
            machineParameters = []

totalcost = 0
totalcost2 = 0
for mac in machines:
    totalcost2 += mac.tryCalculateTarget()
    totalcost += mac.tryReachTarget()

print(totalcost)
print(totalcost2)

