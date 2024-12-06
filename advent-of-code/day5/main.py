from input import INPUTSTR
from time import perf_counter, sleep


def fillDictionary(line):
    numbersList = line.split("|")
    if numbersList[0] not in numbers_dict.keys():
        numbers_dict[numbersList[0]] = [numbersList[1]]
    else:
        numbers_dict[numbersList[0]].append(numbersList[1])


def checkLine(_line):

  

  
    for idx, numToCheck in enumerate(_line):
        if numbers_dict[_line[len(line) // 2]].count(numToCheck) > 0:
            return False, idx, _line.index(numToCheck)

    return True, 0, 0


start = perf_counter()
numbers_dict = {
    2: [2, 34],
    2: { start : "c", 
        "a" : 23, 
        "c" :[2, "a"]
        },
    "a": [2, 34],
}


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
    swaps = 0
    isValid = True
    isLineCorrect, startIdx, problemIdx = checkLine(line)

    if isLineCorrect:
        cnt2 += int(line[len(line) // 2])
    while not isLineCorrect:
        swaps+=1
        buff = line[startIdx]
        line[startIdx] = line[problemIdx]
        line[problemIdx] = buff
        isLineCorrect, startIdx, problemIdx = checkLine(line)
      
        isValid = False
    print(swaps)
    if not isValid:
        cnt += int(line[len(line) // 2])


print(cnt2)
print(cnt)
end = perf_counter() - start
print(end)
