import numpy as np
import re
from input import INPUTSTR





def checkMatrix(input, horizontal=True, vertical=True):
    inputList = input

    buffer = [0] * 32
    vertBuffer = [0] * 32
    diagBuffer = [0] * 16
    checkString = ""
    for j in range(len(inputList)):
        for i in range(len(inputList[j])):
            if horizontal: # Scan horizontal lines
                buffer[4 * j + i] = inputList[j, i]
                buffer[31 - (4 * j + i)] = inputList[j, i]
            if vertical: # Scan vertical lines
                vertBuffer[i * 4 + j] = inputList[j, i]
                vertBuffer[31 - (4 * i + j)] = inputList[j, i]

            if i == j:
                diagBuffer[i] = inputList[j, i]
                diagBuffer[7 - i] = inputList[j, i]
            if i == len(inputList) - j - 1:
                diagBuffer[8 + i] = inputList[j, i]
                diagBuffer[8 + 7 - i] = inputList[j, i]

    for x in range(4, 41, 5):
        try:
            buffer.insert(x, " ")
            vertBuffer.insert(x, " ")
            diagBuffer.insert(x, " ")
        except:
            pass
    checkString = "".join([str(c) for c in buffer])
    checkString += "".join([str(c) for c in vertBuffer])
    checkString += "".join([str(c) for c in diagBuffer])


    founds = re.findall("XMAS", checkString)
    return len(founds)


result = np.array([[c for c in line] for line in INPUTSTR.splitlines()])
counts = 0
horizontal = True
vertical = False

for i in range(0, len(result) - 3):
    for j in range(0, len(result[0]) - 3):
        matrix = result[i : i + 4, j : j + 4]
        if j % 4 == 0:
            vertical = True
        else:
            vertical = False
        if i % 4 == 0:
            horizontal = True
        else:
            horizontal = False

        res = checkMatrix(matrix, horizontal, vertical)
        counts += res
print(counts)
