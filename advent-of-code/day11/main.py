from time import perf_counter, sleep
start = perf_counter()

def createList(list, depth = 0):
    if depth == 25:
        return list
    newList = []

            
    for el in list:
        elementString = str(el)
        if el == 0:
            newList.append(1)
        elif len(elementString) % 2 == 0:
            newElement = elementString[0:len(elementString) // 2]
            newList.append(int(newElement))
            newElement = elementString[len(elementString) // 2:]
            newList.append(int(newElement))
        else:
            newList.append(el*2024) 
    
    return createList(newList,depth+1)

def checkNumberRecursive(number,memoList,depth = 0):
    if depth == 75:
        return 1
    if number in memoList[depth]:
        return memoList[depth][number]

    numberString = str(number)
    if number == 0:
        memoList[depth][number] = checkNumberRecursive(1,memoList,depth+1)
        return memoList[depth][number]
    elif len(numberString) % 2 == 0:
        newElementLeft = int(numberString[0:len(numberString) // 2])
        newElementRight = int(numberString[len(numberString) // 2:])
        memoList[depth][number] = checkNumberRecursive(newElementLeft,memoList,depth+1) + checkNumberRecursive(newElementRight,memoList,depth+1)
        return memoList[depth][number]
    else:
        memoList[depth][number] = checkNumberRecursive(number*2024,memoList,depth+1)
        return memoList[depth][number]

inputList = [2, 77706, 5847, 9258441, 0, 741, 883933, 12]
cnt = 0
DEPTH = 75
memoList = []
for i in range(0,DEPTH):
    memoList.append({})


print(len(createList(inputList)))
end = perf_counter() - start
print(f"Time elapsed list: {end}")


start = perf_counter()
for i in inputList:
    cnt+=checkNumberRecursive(i,memoList)

  
print(cnt)
end = perf_counter() - start
print(f"Time elapsed recurs: {end}")