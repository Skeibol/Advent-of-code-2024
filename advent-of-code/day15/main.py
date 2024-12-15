from enum import Enum
import numpy as np


class Vel(Enum):
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]


class GameObject:
    def __init__(self, X, Y, width):
        self.X = X * width
        self.Y = Y
        self.width = width

    def checkMove(self, velocity, crates, walls):
        for selfWidth in range(0, self.width):

            nextPos = [self.X + velocity[0] + selfWidth, self.Y + velocity[1]]
            for wall in walls:
                for wallWidth in range(0, wall.width):
                    if wall.X + wallWidth == nextPos[0] and wall.Y == nextPos[1]:
                        return False
         

            for crate in crates:
                if crate == self:
                    continue
                for crateWidth in range(0, crate.width):
                    if crate.X + crateWidth == nextPos[0] and crate.Y == nextPos[1]:
                        if not crate.checkMove(velocity, crates, walls):
                            return False

        return True

    def pushObjects(self, velocity, crates, walls):
        for selfWidth in range(0, self.width):

            nextPos = [self.X + velocity[0] + selfWidth, self.Y + velocity[1]]
            for crate in crates:
                if crate == self:
                    continue
                for crateWidth in range(0, crate.width):
                    if crate.X + crateWidth == nextPos[0] and crate.Y == nextPos[1]:
                        crate.pushObjects(velocity, crates, walls)

        self.X = self.X + velocity[0]
        self.Y = self.Y + velocity[1]


class Crate(GameObject):
    def __init__(self, X, Y, width):
        super().__init__(X, Y, width)

    def getGPSCoordinate(self):
        return 100 * self.Y + self.X


class Robot(GameObject):
    def __init__(self, X, Y, width):
        super().__init__(X, Y, width)


class Wall:
    def __init__(self, X, Y, width):
        self.X = X * width
        self.Y = Y
        self.width = width


def printField(crates, walls, robot):
    field = np.full((FIELD_HEIGHT, FIELD_WIDTH), ".")
    for wall in walls:
        field[wall.Y, wall.X : wall.X + wall.width] = "#"
    for crate in crates:
        field[crate.Y, crate.X + crate.width - 2] = "["
        field[crate.Y, crate.X + crate.width - 1] = "]"
    field[robot.Y, robot.X] = "@"
    print(field)


FIELD_HEIGHT = 10
FIELD_WIDTH = 10 * 2
crates = []
walls = []
robot = None
moves = []
with open("./advent-of-code/day15/input.txt", "r") as file:  # Initializing world
    recordingMoves = False
    y = 0
    for line in file:
        x = 0
        if line == "\n":
            recordingMoves = True
            print("brak")
            continue
        if recordingMoves:
            for chr in line:
                if chr == "^":
                    moves.append(Vel.UP)
                elif chr == "v":
                    moves.append(Vel.DOWN)
                elif chr == "<":
                    moves.append(Vel.LEFT)
                elif chr == ">":
                    moves.append(Vel.RIGHT)
                print(chr)
        else:
            for chr in line:
                if chr == "#":
                    obj = Wall(x, y, 2)
                    walls.append(obj)
                elif chr == "O":
                    obj = Crate(x, y, 2)
                    crates.append(obj)
                elif chr == "@":
                    robot = Robot(x * 2, y, 1)
                x += 1
        y += 1  # End initializing world


coordinateSum = 0
for move in moves:
    if robot.checkMove(move.value, crates, walls):
        robot.pushObjects(move.value, crates, walls)
        
for crate in crates:
    coordinateSum += crate.getGPSCoordinate()

print(coordinateSum)
