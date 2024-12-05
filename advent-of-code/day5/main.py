from input import INPUTSTR
from time import perf_counter, sleep


def fillDictionary(line):
    numbersList = line.split("|")
    if numbersList[0] not in numbers_dict.keys():
        numbers_dict[numbersList[0]] = [numbersList[1]]
    else:
        numbers_dict[numbersList[0]].append(numbersList[1])


def checkLine(_line):

    for idx in range(0, len(_line)):
        if idx == len(_line) - 1:
            continue
        if _line[idx] not in numbers_dict.keys():
            continue
        for numToCheck in _line[idx + 1 :]:
            if numbers_dict[_line[idx]].count(numToCheck) > 0:
                return False, idx, _line.index(numToCheck)

    return True, 0, 0


start = perf_counter()
numbers_dict = {}
numbers_list = []
parsedOrders = False
cnt = 0
cnt2 = 0

for line in INPUTSTR.splitlines():
    if line == "":
        parsedOrders = True
        continue
    if not parsedOrders:
        fillDictionary(line)
    else:
        numbers_list.append([i for i in line.split(",")[::-1]])

for line in numbers_list:
    isValid = True
    isLineCorrect, startIdx, problemIdx = checkLine(line)

    if isLineCorrect:
        cnt2 += int(line[len(line) // 2])
    while not isLineCorrect:
        buff = line[startIdx]
        line[startIdx] = line[problemIdx]
        line[problemIdx] = buff
        isLineCorrect, startIdx, problemIdx = checkLine(line)
        cnt2
        isValid = False

    if not isValid:
        cnt += int(line[len(line) // 2])


print(cnt2)
print(cnt)
end = perf_counter() - start
print(end)
