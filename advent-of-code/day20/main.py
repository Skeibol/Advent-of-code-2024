import numpy as np

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def printField(field, start, end):
    fieldToPrint = np.array(field, dtype=str)
    for idxRow, row in enumerate(field):
        for idxCol, col in enumerate(row):
            if col == 0:
                fieldToPrint[idxRow, idxCol] = "."
            elif col == 1:
                fieldToPrint[idxRow, idxCol] = "#"

    fieldToPrint[start] = "S"
    fieldToPrint[end] = "E"
    print(fieldToPrint)


def getAllDistances(field, position, end, distances):
    moves = 0
    while position != end:
        for dir in DIRECTIONS:
            nextPos = (dir[0] + position[0], dir[1] + position[1])
            if nextPos in distances:
                continue
            if field[nextPos] == 0:
                distances[position] = moves
                position = nextPos
                moves += 1

    distances[end] = moves
    distances = dict(sorted(distances.items(), key=lambda item: item[1], reverse=False))
    return distances


def tryToCheat(field, positions):
    scores = {}
    for posToTry in positions:
        for dir in DIRECTIONS:
            nextPos = (dir[0] + posToTry[0], dir[1] + posToTry[1])
            if field[nextPos] == 1:
                for dir in DIRECTIONS:
                    finalPos = (dir[0] + nextPos[0], dir[1] + nextPos[1])
                    if (
                        finalPos == posToTry
                        or finalPos[0] < 0
                        or finalPos[0] >= field.shape[0]
                        or finalPos[1] < 0
                        or finalPos[1] >= field.shape[1]
                    ):
                        continue
                    if field[finalPos] == 0:
                        score = (
                            positions[finalPos] - positions[posToTry] - 2
                        )  # Jer 2 koraka napravis
                        if score >= 100:
                            scores[(posToTry, finalPos)] = score
    return scores


def tryToCheatRecursively(
    field, currentPosition, distanceToeEndStartPos, distanceToEndDict, depth=0
):
    if depth == 7:
        return 0

    score = 0
    for dir in DIRECTIONS:
        nextPos = (dir[0] + currentPosition[0], dir[1] + currentPosition[1])
        if (
            nextPos[0] < 0
            or nextPos[0] >= field.shape[0]
            or nextPos[1] < 0
            or nextPos[1] >= field.shape[1]
        ):
            continue
        score += tryToCheatRecursively(
            field, nextPos, distanceToeEndStartPos, distanceToEndDict, depth + 1, memo={}
        )

    if currentPosition in distanceToEndDict:
        if distanceToEndDict[currentPosition] + depth - distanceToeEndStartPos >= 74:
            return score + 1

    return score


def diamondHands(positionsToCheck, startPos, allowedMoves, bound):
    possiblePaths = 0

    startX = -allowedMoves
    startY = -allowedMoves

    for row in range(startY, allowedMoves + 1):
        for col in range(startX, allowedMoves + 1):
            nextPos = (startPos[0] + row, startPos[1] + col)
            distanceTraveled = abs(row) + abs(col)
        
            if distanceTraveled > allowedMoves or nextPos == startPos or nextPos[0] < 0 or nextPos[0] >= bound[0] or nextPos[1] < 0 or nextPos[1] >= bound[1]:
                continue
            if nextPos in positionsToCheck:
                if positionsToCheck[nextPos] - positionsToCheck[startPos] - distanceTraveled >= 100 :
                    possiblePaths+=1
                pass
    
    return possiblePaths
    # arr[startPos] = 2
    # print(arr)


with open("./advent-of-code/day20/input.txt", "r") as file:
    lines = file.read().splitlines()

start = (0, 0)
end = (0, 0)
field = []
for idxRow, line in enumerate(lines):
    row = []
    for idxCol, char in enumerate(line):
        if char == "#":
            row.append(1)
        else:
            row.append(0)

        if char == "S":
            start = (idxRow, idxCol)
        if char == "E":
            end = (idxRow, idxCol)
    field.append(row)
field = np.array(field)
distances = {}

distances = getAllDistances(field, start, end, distances)
shortcutScores = tryToCheat(field, distances)
score = 0
for startPos, distToEnd in distances.items():
    score += diamondHands(distances, startPos, 20, field.shape)
    # print("yo")

print(score)
