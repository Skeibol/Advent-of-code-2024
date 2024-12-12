import numpy as np


class Garden:
    def __init__(self, ID):
        self.ID = ID
        self.locations = []
        self.fences = 0
        self.corners = 0

    def addGardenLocation(self, Y, X):
        self.fences += 4
        self.locations.append([Y, X])

    def setFences(self):
        for location in self.locations:
            Y = location[0]
            X = location[1]

            crossLocations = [[Y + 1, X], [Y - 1, X], [Y, X + 1], [Y, X - 1]]
            for crossY, crossX in crossLocations:
                if [crossY, crossX] in self.locations:
                    self.fences -= 1

        return self.fences * len(self.locations)

    def calculateCorners(self):
        for location in self.locations:
            X = location[1]
            Y = location[0]
            diagonals = [[Y + 1, X + 1], [Y - 1, X + 1], [Y - 1, X - 1], [Y + 1, X - 1]]
            for diagY, diagX in diagonals:
                if [diagY, X] not in self.locations and [Y, diagX] not in self.locations:
                    self.corners += 1

                if [diagY, X] in self.locations and [Y, diagX] in self.locations:
                    if [diagY, diagX] not in self.locations:
                        self.corners += 1

        return self.corners * len(self.locations)


def visitAdjacentSquares(Y, X, terrain, visitedArray, gardenObject):
    height, width = terrain.shape
    if (
        X < 0
        or X >= width
        or Y < 0
        or Y >= height
        or terrain[Y, X] != gardenObject.ID
        or visitedArray[Y, X] == 1
    ):
        return

    gardenObject.addGardenLocation(Y, X)

    visitedArray[Y, X] = 1
    visitAdjacentSquares(Y + 1, X, terrain, visitedArray, gardenObject)
    visitAdjacentSquares(Y - 1, X, terrain, visitedArray, gardenObject)
    visitAdjacentSquares(Y, X + 1, terrain, visitedArray, gardenObject)
    visitAdjacentSquares(Y, X - 1, terrain, visitedArray, gardenObject)


row = []
terrain = []
with open("./advent-of-code/day12/input.txt", "r") as file:
    # Read each line in the file
    for line in file:
        for char in line:
            if char == "\n":
                continue
            if char == ".":
                row.append(-1)
                continue
            row.append(ord(char))
        terrain.append(row)
        row = []

terrainArray = np.array(terrain)
visitedArray = np.zeros_like(terrainArray)

gardens = []
for Y in range(0, len(terrainArray)):
    for X in range(0, len(terrainArray[0])):

        gardenObj = Garden(terrainArray[Y, X])

        visitAdjacentSquares(Y, X, terrainArray, visitedArray, gardenObj)
        if len(gardenObj.locations) > 0:
            gardens.append(gardenObj)


fencePriceTotal = 0
cornerPriceTotal = 0
for garden in gardens:
    fencePriceTotal += garden.setFences()
    cornerPriceTotal += garden.calculateCorners()
    # print(f"{chr(garden.ID)} has {garden.corners} corners")
print(f"Total price fences : {fencePriceTotal}")
print(f"Total price corners : {cornerPriceTotal}")
