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
            locationFences = 4
            if [Y + 1, X] in self.locations:
                locationFences -= 1

            if [Y - 1, X] in self.locations:
                locationFences -= 1

            if [Y, X + 1] in self.locations:
                locationFences -= 1

            if [Y, X - 1] in self.locations:
                locationFences -= 1

            self.fences -= locationFences

        return self.fences * len(self.locations)

    def calculateCorners(self):
        for location in self.locations:
            X = location[1]
            Y = location[0]
            diagonal = [Y + 1, X + 1]
            if diagonal not in self.locations:
                if [Y + 1, X] in self.locations and [Y, X + 1] in self.locations:
                    self.corners += 1
                if [Y + 1, X] not in self.locations and [
                    Y,
                    X + 1,
                ] not in self.locations:
                    self.corners += 1
            else:
                if [Y + 1, X] not in self.locations and [
                    Y,
                    X + 1,
                ] not in self.locations:
                    self.corners += 1

            diagonal = [Y - 1, X + 1]
            if diagonal not in self.locations:
                if [Y - 1, X] in self.locations and [Y, X + 1] in self.locations:
                    self.corners += 1
                if [Y - 1, X] not in self.locations and [
                    Y,
                    X + 1,
                ] not in self.locations:
                    self.corners += 1
            else:
                if [Y - 1, X] not in self.locations and [
                    Y,
                    X + 1,
                ] not in self.locations:
                    self.corners += 1

            diagonal = [Y - 1, X - 1]
            if diagonal not in self.locations:
                if [Y - 1, X] in self.locations and [Y, X - 1] in self.locations:
                    self.corners += 1
                if [Y - 1, X] not in self.locations and [
                    Y,
                    X - 1,
                ] not in self.locations:
                    self.corners += 1
            else:
                if [Y - 1, X] not in self.locations and [
                    Y,
                    X - 1,
                ] not in self.locations:
                    self.corners += 1
            diagonal = [Y + 1, X - 1]
            if diagonal not in self.locations:
                if [Y + 1, X] in self.locations and [Y, X - 1] in self.locations:
                    self.corners += 1
                if [Y + 1, X] not in self.locations and [
                    Y,
                    X - 1,
                ] not in self.locations:
                    self.corners += 1
            else:
                if [Y + 1, X] not in self.locations and [
                    Y,
                    X - 1,
                ] not in self.locations:
                    self.corners += 1
        print(f"{chr(self.ID)} price = {self.corners * len(self.locations)}")
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


fencesTotal = 0
cornersTotal = 0
for garden in gardens:
    fencesTotal += garden.setFences()
    cornersTotal += garden.calculateCorners()
    # print(f"{chr(garden.ID)} has {garden.corners} corners")
print(f"Total price : {cornersTotal}")
