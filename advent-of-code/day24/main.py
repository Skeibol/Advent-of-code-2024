class Gate():
    def __init__(self,ID) -> None:
        self.ID = ID
        self.op = None
        self.inputs = []
        self.output = None
        self.value = 0
        self.done = False
        pass
    
    def calculateOutput(self,wires):
        self.done = True
        if self.op == 'OR':
            return int(wires[self.inputs[0]] or wires[self.inputs[1]])
        elif self.op == 'AND':
            return int(wires[self.inputs[0]] and wires[self.inputs[1]])
        elif self.op == 'XOR':
            return int(wires[self.inputs[0]] != wires[self.inputs[1]])
        
def getNextGate(gates,current):
    if current.ID[0] == 'z':
        return current
        
   
    for nextGate in gates.values():
        if current.output in nextGate.inputs:
            g = getNextGate(gates,nextGate)
            
    return g

def simulateCircuit(gates,wires):
    done = False

    while not done:
        done = True
        for gate in gates.values():
            if wires[gate.inputs[0]] == -1 or wires[gate.inputs[1]] == -1:
    
                done = False
            else:
                if not gate.done:
                    wires[gate.output] = gate.calculateOutput(wires)
                #print(gate.ID)
            

    bits = ''
    wires = dict(sorted(wires.items()))
    for w in wires:
        if w[0] == 'z':
            bits = str(wires[w]) + bits
            
    return bits



with open("./advent-of-code/day24/input.txt", "r") as file:
    lines = file.read().splitlines()

swappedGates = []
gates = {}
wires = {}

initialized = False
for row in lines:
    if row == '':
        initialized = True
        continue

    if not initialized:
        wire, value = row.replace(' ', '').split(':')
        wires[wire] = int(value)
        

    else:
        
        inWireA, op, inWireB, _, outputWire = row.split(' ')
        gate = Gate(outputWire)
        gate.op = op
        gate.output = outputWire
        gate.inputs = [inWireA ,inWireB]

        if inWireA not in wires:
            wires[inWireA] = -1
        
        if inWireB not in wires:
            wires[inWireB] = -1
        
        wires[outputWire] = -1
        gates[outputWire] = gate
        
circuitsToReplace = []
tempS = []        
for i in [i for i in gates.values() if i.output[0] == 'z']:
    r = []
    if i.op != 'XOR':
        if i.ID != 'z45': # Not the last one
            tempS.append(i)

circuitsToReplace.append(tempS)
tempS = []           
for i in [i for i in gates.values() if i.output[0] != 'z']:
    inpA , inpB = i.inputs
    if not ((inpA[0] == 'x' or inpA[0] == 'y') and (inpB[0] == 'x' or inpB[0] == 'y')):
        if i.op == 'XOR':
            tempS.append(i) 
                       
circuitsToReplace.append(tempS)
tempS = [] 


for zs,replacements in zip(circuitsToReplace[0],circuitsToReplace[1]): # Replace first circuits
    out = getNextGate(gates,replacements)
    foundString = 'z' + str(int(out.ID[1:]) - 1)

    temp = gates[replacements.output].output
    gates[replacements.output].output = gates[foundString].output
    gates[foundString].output = temp

    swappedGates.extend([zs,replacements])
    
tempS = []
for g in gates.values(): 
    o1,o2 = g.inputs
    if (o1 == 'x33' or o2 == 'x33') and (o1=='y33' or o2=='y33'):
        tempS.append(g)
        swappedGates.append(g)
        
        
temp = tempS[0].output # Replace final circuits
tempS[0].output = tempS[1].output
tempS[1].output = temp

simulateCircuit(gates,wires)
print(','.join(sorted([s.ID for s in swappedGates])))


