import re
import numpy as np
class Color:
    NLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'

def drawField(obstacles,path,addedObs):
    field = np.full((FIELD_SIZE, FIELD_SIZE), ".", dtype=str)
    for o in obstacles:
        field[o] = "#"
    for p in path:
        field[p] = "O"

    field[0,0] = '@'
    for added in addedObs:
        field[added] = 'X'
    for j in range(0, FIELD_SIZE):
        for i in range(0, FIELD_SIZE):
            if field[j,i] == 'O':
                pr = f"{Color.GREEN}{field[j, i]}{Color.ENDC}"
                print(field[j, i], end="")
            elif field[j,i] == '@':
                pr = f"{Color.GREEN}{field[j, i]}{Color.ENDC}"
                print(pr, end="")
            elif field[j,i] == '#':
                pr = f"{Color.RED}{field[j, i]}{Color.ENDC}"
                print(pr, end="")
            elif field[j,i] == 'X':
                pr = f"{Color.CYAN}{field[j, i]}{Color.ENDC}"
                print(pr, end="")
            else:
                pr = f"{Color.CYAN}{field[j, i]}{Color.ENDC}"
                print(pr, end="")
        print()

def saveField(field):
    with open("./advent-of-code/day18/visual.txt", "w") as file:

        for row in field:
            for el in row:
                file.write(el)
            file.write('\n')
            

def getNextPosition(field,pos,dir):
    nextY = pos[0] + dir[0]
    nextX = pos[1] + dir[1]

    if nextY < 0 or nextY >= FIELD_SIZE or nextX < 0 or nextX >= FIELD_SIZE:
        return (-1,-1), False
    
    if field[nextY,nextX] != 0:
        return (-1,-1), False
    
    return (nextY,nextX), True 

    
def privateDickstra(field, unvisited):
    visited = {}
    directions = [(-1, 0), (1,0), (0,-1), (0,1)] # U D L R
    start = (0,0) 
    unvisited[start] = 0
    end = (FIELD_SIZE - 1, FIELD_SIZE - 1)
    backtrackingPath = {}
    while unvisited:
        currentPos = min(unvisited, key=unvisited.get)
        if currentPos != start and unvisited[currentPos] == float('inf'):
            return []
        
        visited[currentPos] = unvisited[currentPos]
        
        if currentPos == end:
            break
        
        for dir in directions:
            nextPos, success = getNextPosition(field,currentPos,dir)
            if nextPos in visited:
                continue
            if success:
                tempDist = unvisited[currentPos] + 1
                if tempDist < unvisited[nextPos]:
                    unvisited[nextPos] = tempDist
                    backtrackingPath[nextPos] = currentPos

        unvisited.pop(currentPos)
        
    currentPos = end
    path = []

    while currentPos != start:
        path.append(currentPos)
        currentPos = backtrackingPath[currentPos]

    return path

coords = []
extraCoords = []
FIELD_SIZE = 71

field = np.zeros((FIELD_SIZE, FIELD_SIZE), dtype=int)
firstCoordinatesBatch = 1024
reachedEndBatch = False
with open("./advent-of-code/day18/input.txt", "r") as file:
    for idx, line in enumerate(file):
        if idx == firstCoordinatesBatch:
            reachedEndBatch = True
        
        line = line.strip()
        cord = tuple([int(x) for x in line.split(",")][::-1])
        if not reachedEndBatch:
            coords.append(cord)
        else:
            extraCoords.append(cord)

unvisited = {}
for c in coords:
    field[c] = 1
for indec in zip(*np.where(field == 0)):
    unvisited[int(indec[0]),int(indec[1])] = float('inf')

addedObs = []
for idx,obs in enumerate(extraCoords):
    field[obs] = 2
    del unvisited[obs]
    addedObs.append(obs)
    path = privateDickstra(field,unvisited.copy())
    
    if not path:
        print(f"No path at coordinate {obs}")
        break
        
    if idx % 200 == 0:
        drawField(coords,path,addedObs)
        print(f"Added # at {obs}")

print(len(path))