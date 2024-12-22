from time import perf_counter, sleep
start = perf_counter()

def mix(value,secretNumber):
    return value ^ secretNumber
def prune(secretNumber):
    return secretNumber%16777216

def shift_left(arr, k):
    n = len(arr)
    k = min(k, n)  
    return arr[k:] + [0] * k

def calculateSecretNumber(initialNum,sequenceValues):
    sequence = [0,0,0,0]
    prev = initialNum %10
    visitedSequences = {}
    for i in range(0,2000):
      
        
   
        initialNum = (initialNum << 6 ^ initialNum  )% 16777216
        initialNum = (initialNum >> 5  ^ initialNum)% 16777216
        initialNum = (initialNum << 11 ^ initialNum  )% 16777216
       
        value = initialNum%10
        change = value - prev
        sequence[-1] = change
        
        if i>2 and value > 0:
            seqTuple = tuple(sequence)
            if seqTuple not in sequenceValues:
                sequenceValues[seqTuple] = value
                visitedSequences[seqTuple] = True
            else:
                if seqTuple not in visitedSequences:
                    sequenceValues[seqTuple] += value
                    visitedSequences[seqTuple] = True
                
                
        prev = value
        sequence = shift_left(sequence,1)
    return initialNum

def sumList(ls):
    total = 0
    for idx,member in enumerate(ls):
        total+= member * idx
    return total
        
sequenceValues = {}

with open("./advent-of-code/day22/input.txt", "r") as file:

    lines = file.read().splitlines()

for num in lines:
    calculateSecretNumber(int(num),sequenceValues)
    


key = max(sequenceValues,key=sequenceValues.get)
bananas = sequenceValues[key]
print(bananas)
end = perf_counter() - start
print(f"Time elapsed recurs: {end}")