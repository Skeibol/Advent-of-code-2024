from functools import reduce
from operator import mul
from time import perf_counter, sleep

class Node:
    def __init__(self):
        self.result = result
        self.parent = None

    def setParent(self, parentNode):
        self.parent = parentNode
        pass

    def getInitialResult(self):
        currNode = self
        while(currNode.parent is not None):
            currNode = currNode.parent

        return currNode.result


def parseLine(line, node=None, depth=0):

    if depth > len(line) - 2:

        if node.result == line[depth]:
            #print(f"Depth exceeded on {line[depth]} result {line[depth]}")
            return 1
        else:
            return 0
    else:
       
        currentNode = Node()
        currentNode.parent = node
     
        
        numberToCheck = line[depth]
        res = 0
        if (node.result / numberToCheck) % 1 == 0:
            currentNode.result = node.result // numberToCheck 
            res += parseLine(line, currentNode, depth + 1)
        if node.result - numberToCheck > 0:
            currentNode.result = node.result - numberToCheck 
            res += parseLine(line, currentNode, depth + 1)
        numberToCheckString = str(numberToCheck)
        resultString = str(node.result)
        if len(numberToCheckString) < len(resultString) and resultString[-len(numberToCheckString) :] == numberToCheckString:
            currentNode.result = int(resultString[:-len(numberToCheckString)])
            res += parseLine(line, currentNode, depth + 1)
        
        return res

start = perf_counter()
f = open("./advent-of-code/day7/input.txt", "r")

results = []
numbers = []

cnt = 0
for line in f.readlines():
    splitLine = line.split(":")
    results.append(int(splitLine[0]))
    numbers.append([int(i) for i in splitLine[1][:-1].strip().split(" ")][::-1])

for idx, result in enumerate(results):
    initialNode = Node()
    initialNode.result = result
    if(parseLine(numbers[idx], initialNode)):
        cnt+= result

      
print(cnt)
end = perf_counter() - start
print(f"Time elapsed : {end}")