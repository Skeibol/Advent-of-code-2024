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

def saveField(file,field,path,frame,pathLength,addedAt,final):
    if final:
        for p in path[0].keys():
            field[p] = 3
        
    else:
      for p in path:
            field[p] = 3
  

    for row in field:
        for el in row:
            file.write(str(el))
        file.write('\n')
    file.write(f'-.{frame}.{pathLength}.{addedAt}\n')
            

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
            return [visited]
        
        visited[currentPos] = unvisited[currentPos]
        
        if currentPos == end:
            break
        
        for dir in directions:
            nextPos, success = getNextPosition(field,currentPos,dir)
            if not success or nextPos in visited:
                continue
    
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

path = privateDickstra(field,unvisited.copy())
shortestPath = privateDickstra(field,unvisited.copy())
addedObs = []
with open("./advent-of-code/day18/visual.txt", "w") as file:
    for idx,obstacle in enumerate(extraCoords):
        field[obstacle] = 2
        del unvisited[obstacle]
        #addedObs.append(obstacle)
        if len(path) < 2: # Saving things
            #saveField(file,field.copy(),path,idx,-1,obstacle,True)
            break
        if obstacle in path:
            if obstacle == (63, 38):
                break
            path = privateDickstra(field,unvisited.copy())
            saveField(file,field.copy(),path,idx,len(path),obstacle,False)
        #print(idx)

print(len(shortestPath))
print(obstacle[::-1])