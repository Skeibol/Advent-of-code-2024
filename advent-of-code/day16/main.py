import numpy as np

def printField(field, X, Y,path=None):
    for idxX, row in enumerate(field):
        for idxY, chr in enumerate(row):
            if ((idxY,idxX) in path):
                print("O", end="")
                continue
            if idxX == X and idxY == Y:
                print("@", end="")
                continue
            if chr == 0:
                print(".", end="")
            elif chr == 1:
                print("#", end="")
            elif chr == 2:
                print("s", end="")

        print()

def checkMoves(pos, field, startDirection, seenPositions, cost=0, depth=0):
    startX = pos[0]
    startY = pos[1]
    if field[startY, startX] == 2:
        return 0
    if depth > 900:
        return 0
    if seenPositions.count(pos) > 0:

        return 0
    else:
        seenPositions.append(pos)

    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for newDirection in directions:

        nextPosition, success = getNextPosition(startX, startY, field, newDirection)
        currCost = getMoveCost(startDirection, newDirection)
        if success and currCost < 2000:
            checkMoves(
                nextPosition, field, newDirection, seenPositions.copy(), cost + currCost, depth + 1
            )


def getNextPosition(X, Y, field, dir):
    nextPos = (X + dir[0], Y + dir[1])

    if field[nextPos[1], nextPos[0]] == 1:
        return nextPos, False
    else:
        return nextPos, True


def getMoveCost(startDirection, newDirection):
    if startDirection[0] == newDirection[0] and startDirection[1] == newDirection[1]:
        return 1

    if newDirection[0] - startDirection[0] > 1 or newDirection[1] - startDirection[1] > 1:
        return 2001
    else:
        return 1001


def dijkstra(start, target, field, unvisited):
    direction = (0, 1)
    unvisited[direction][start] = 0

    visited = {
        (0, -1): {},
        (0, 1): {},
        (-1, 0): {},
        (1, 0): {},
    }
    revPath = {
        (0, -1): {},
        (0, 1): {},
        (-1, 0): {},
        (1, 0): {},
    }

    while len(unvisited) > 1:
        currentDirection, currentPosition, _ = min(
            (
                (outer_key, inner_key, value)
                for outer_key, sub_dict in unvisited.items()
                for inner_key, value in sub_dict.items()
            ),
            key=lambda x: x[2],
        )

        visited[currentDirection][currentPosition] = unvisited[currentDirection][currentPosition]

        if currentPosition == target:
            break

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for nextDirection in directions:
            nextPosition, success = getNextPosition(
                currentPosition[0], currentPosition[1], field, nextDirection
            )

            if nextPosition in visited[nextDirection]:
                continue
            if success:
                cost = getMoveCost(currentDirection, nextDirection)
                tempDist = unvisited[currentDirection][currentPosition] + cost
                if tempDist < unvisited[nextDirection][nextPosition]:
                    unvisited[nextDirection][nextPosition] = tempDist
                    revPath[nextDirection][nextPosition] = [(currentDirection, currentPosition, cost)]
                    
                elif tempDist == unvisited[nextDirection].get(nextPosition, float('inf')):
                    revPath[nextDirection][nextPosition].append((currentDirection, currentPosition,cost))

            else:
                
                inverseDir = [(-x, -y) for x, y in directions if (x,y) == (nextDirection)][0]
                if inverseDir in unvisited and currentPosition in unvisited[inverseDir]:
                    visited[inverseDir][currentPosition] = unvisited[inverseDir][currentPosition]
                    unvisited[inverseDir].pop(currentPosition)
            

        unvisited[currentDirection].pop(currentPosition)
        if not unvisited[currentDirection]:
            unvisited.pop(currentDirection)
            
    pths = get_all_paths_iteratively(revPath,start,target,currentDirection)
    uniquePaths = []
    for pth in pths:
        for coord in pth:
            if coord not in uniquePaths:
                uniquePaths.append(coord)
    print(len(uniquePaths))
        

def get_all_paths_iteratively(revPath, start, target,dir):
    all_paths = []
    stack = [([target], target, dir)]  # Stack stores (current_path, current_position, current_direction)

    while stack:
        current_path, current_position, current_direction = stack.pop()

        if current_position == start:
            all_paths.append(current_path[::-1])  # Reverse the path to get it from start to target
            continue

        # Explore all predecessors for the current position
        if current_direction in revPath and current_position in revPath[current_direction]:
            for prev_direction, prev_position, cost in revPath[current_direction][current_position]:
                # Add the predecessor to the stack
                stack.append((current_path + [prev_position], prev_position, prev_direction))

    return all_paths
field = []
start = ()
target = ()
unvisited = {
    (0, -1): {},
    (0, 1): {},
    (-1, 0): {},
    (1, 0): {},
}
with open("./advent-of-code/day16/input.txt", "r") as file:
    for y, line in enumerate(file):
        row = []
        for x, char in enumerate(line):
            if char == "\n":
                continue

            if char == "#":
                row.append(1)

            elif char == "E":
                target = (x, y)
                row.append(2)
            else:

                row.append(0)

            if char == "S":

                start = (x, y)

            if char != "#":
                unvisited[(0, -1)][(x, y)] = float("inf")
                unvisited[(0, 1)][(x, y)] = float("inf")
                unvisited[(-1, 0)][(x, y)] = float("inf")
                unvisited[(1, 0)][(x, y)] = float("inf")

        field.append(row)

field = np.array(field)
a = dijkstra(start, target, field, unvisited)

