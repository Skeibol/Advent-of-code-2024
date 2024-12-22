from enum import Enum
import numpy as np
from collections import deque

ROBOT_MOVE_MAP = {
    "A": {"A": ["A"], "^": ["<A"], "<": ["v<<A"], ">": ["vA"], "v": ["v<A", "<vA"]},
    "^": {"A": [">A"], "^": ["A"], "<": ["v<A"], ">": [">vA", "v>A"], "v": ["vA"]},
    "<": {"A": [">>^A"], "^": [">^A"], "<": ["A"], ">": [">>A"], "v": [">A"]},
    "v": {"A": [">^A", "^>A"], "^": ["^A"], "<": ["<A"], ">": [">A"], "v": ["A"]},
    ">": {"A": ["^A"], "^": ["^<A", "<^A"], "<": ["<<A"], ">": ["A"], "v": ["<A"]},
}


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
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
    CLICK = "A"
    EMPTY = ""

from functools import cache
@cache
def getNextSequence(sequence, maxDepth, depth=0):
    if depth == maxDepth:  #'vA<<A>^A>AA>A'
        final = 0
        currentChr = "A"
        for ch in sequence:
            final += len(ROBOT_MOVE_MAP[currentChr][ch][0])
            currentChr = ch

        return final
    currentChr = "A"
    maxLen = 0

    for nextChar in sequence:
        seq = ROBOT_MOVE_MAP[currentChr][nextChar]
        if len(seq) == 2:
            maxLen += min(
                getNextSequence(seq[0], maxDepth, depth + 1),
                getNextSequence(seq[1], maxDepth, depth + 1),
            )

        else:
            maxLen += getNextSequence(seq[0], maxDepth, depth + 1)

        currentChr = nextChar

    return maxLen


def getManhattanDistance(start_pos, end_pos):
    if end_pos == "A":
        end_pos = 10
    if start_pos == "A":
        start_pos = 10
    start = NUMBERS[int(start_pos)]
    end = NUMBERS[int(end_pos)]
    # Calculate horizontal and vertical distances
    dx = end[1] - start[1]
    dy = end[0] - start[0]

    # Generate primary path (horizontal first, then vertical)
    path1 = (
        (Directions.RIGHT.value * dx if dx > 0 else Directions.LEFT.value * abs(dx))
        + (Directions.DOWN.value * dy if dy > 0 else Directions.UP.value * abs(dy))
        + Directions.CLICK.value
    )

    # Generate secondary path (vertical first, then horizontal)
    path2 = (
        (Directions.DOWN.value * dy if dy > 0 else Directions.UP.value * abs(dy))
        + (Directions.RIGHT.value * dx if dx > 0 else Directions.LEFT.value * abs(dx))
        + Directions.CLICK.value
    )

    if start[0] == 3 and end[1] == 0: # Handle paths going through forbidden square
        return [path2]
    if start[1] == 0 and end[0] == 3:
        return [path1]
    return [path1, path2]

dirs = ["638A", "965A", "780A", "803A", "246A"]
c = 0
MAX_DEP = 100
total = 0
for num in dirs:
    c = 0
    numValueInt = int(''.join([char for char in num if char.isdigit()]))
    startDigit = "A"
    for digit in num:
        dists = getManhattanDistance(startDigit, digit)
        if len(dists) == 2:
            c += min(getNextSequence(dists[0], MAX_DEP), getNextSequence(dists[1], MAX_DEP))
        else:
            c += getNextSequence(dists[0], MAX_DEP)

        startDigit = digit
    total+= c*numValueInt
print(total)

