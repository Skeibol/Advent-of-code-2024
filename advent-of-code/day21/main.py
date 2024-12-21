from enum import Enum
import numpy as np

NUMBERS = {
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    -1: (3, 0),
    0: (3, 1),
    10: (3, 2),
}


class Directions(Enum):
    UP = (0, 1)
    DOWN = (1, 1)
    LEFT = (1, 0)
    RIGHT = (1, 2)
    CLICK = (0, 2)
    EMPTY = (0, 0)


class Numpad:
    def __init__(self):
        self.pos = NUMBERS[10]

    def reset(self):
        self.pos = NUMBERS[10]

    def get_path(self, target):
        if target not in NUMBERS:
            return "Target number not found"

        path = []

        if target == self.pos:
            path.append(Directions.CLICK)
            return path

        y, x = self.pos
        targetY, targetX = NUMBERS[target]
        # Move horizontally
        while x != targetX:
            if x < targetX:
                x += 1
                path.append(Directions.RIGHT)

            else:
                if targetX == 0 and y == 3:
                    while y != targetY:
                        if y < targetY:

                            y += 1
                            path.append(Directions.DOWN)

                        else:
                            y -= 1
                            path.append(Directions.UP)    
                    continue
                x -= 1
                path.append(Directions.LEFT)

        # Move vertically
        while y != targetY:
            if y < targetY:
                if targetY == 3 and x == 0:
                    while x != targetX:
                        if x < targetX:
                            x += 1
                            path.append(Directions.RIGHT)
                        else:
                            x -= 1
                            path.append(Directions.LEFT)
                            
                    continue
                y += 1
                path.append(Directions.DOWN)

            else:
                y -= 1
                path.append(Directions.UP)
        self.pos = (y, x)
        path.append(Directions.CLICK)
        return path

    def calculateMoveForInput(self, inputString):
        inp = []
        for i in inputString:
            if i == "A":
                inp.extend(self.get_path(10))
            else:
                inp.extend(self.get_path(int(i)))
        return inp


class ArrowKeys:
    def __init__(self, depth):
        self.pos = [Directions.CLICK.value] * depth
        self.depth = depth

    def reset(self):
        self.pos = [Directions.CLICK.value] * self.depth

    def get_path(self, target, depth):
        if target not in Directions:
            return "Target direction not found"
        target = target.value
        path = []
        if target == self.pos[depth]:
            path.append(Directions.CLICK)
            return path
        y, x = self.pos[depth]
        targetY, targetX = target
        # Move horizontally
        while x>targetX:
            while (targetY,targetX) == (1,0) and y != targetY:
                   
                if y < targetY:

                    y += 1
                    path.append(Directions.DOWN)

                else:
                    y -= 1
                    path.append(Directions.UP)
                continue
            x -= 1
            path.append(Directions.LEFT)
        
        while y != targetY:
            if y < targetY:

                y += 1
                path.append(Directions.DOWN)

            else:
                if (y,x) == (1,0):
                    while x != targetX:
                        if x < targetX:
                            x += 1
                            path.append(Directions.RIGHT)

                        else:
                            x -= 1
                            path.append(Directions.LEFT)
                    continue
                y -= 1
                path.append(Directions.UP)
                
        while x<targetX:
            x+=1
            path.append(Directions.RIGHT)
        # Move vertically
               

        self.pos[depth] = (y, x)
        path.append(Directions.CLICK)
        return path

    def calculateMoveForInput(self, inputs):
        moves = []
        inp = inputs
        for layer in range(0, self.depth):
            for i in inp:
                moves.extend(self.get_path(i, layer))
            inp = moves
            moves = []

        return inp




def formatDirections(dir):
    strang = ""
    for d in dir:
        if d == Directions.UP:
            strang += "^"
        elif d == Directions.DOWN:
            strang += "v"
        elif d == Directions.RIGHT:
            strang += ">"
        elif d == Directions.LEFT:
            strang += "<"
        elif d == Directions.CLICK:
            strang += "A"
    print(strang)




def splitByA(listWithA):

    split_value = Directions.CLICK

    result = []
    start = 0  # Initialize starting index for slicing

    # Iterate through list to find
    # indices of the split value
    for i, value in enumerate(listWithA):
        if value == split_value:
        
            # Add the sublist from start to the current index
            result.append(listWithA[start:i])  
            
            # Update start to next index after the split value
            start = i + 1  

    # Add the last sublist if there are remaining elements
    if start < len(listWithA):
        result.append(listWithA[start:])
    
    return result

strings = ["638A", "965A", "780A", "803A", "246A"]
strings = ["029A", "980A", "179A", "456A", "379A"]
inputs = {s: int("".join(filter(str.isdigit, s))) for s in strings}
c = 0
numpad = Numpad()
arrowKeys = ArrowKeys(1)
for numStr, value in inputs.items():
    path = numpad.calculateMoveForInput('6')
    
    #print(splitByA(path))
    numpad.reset()
    formatDirections(path)
    path = arrowKeys.calculateMoveForInput(path)
    arrowKeys.reset()
    #print(f"{numStr} : {len(path)} * {value}    ")
    formatDirections(path)
    c += len(path) * value

# v<<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

print(c)