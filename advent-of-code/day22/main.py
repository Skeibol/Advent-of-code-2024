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
def encode_number(n):
    if not (-9 <= n <= 9):
        raise ValueError("Number out of range (-9 to 9)")
    return bytes([n & 0b11111])


def calculateSecretNumber(initialNum,sequenceValues):
    sequence = 0 
    prev = initialNum %10
    visitedSequences = {}
    for i in range(0,2000):
        initialNum = (initialNum << 6 ^ initialNum  )% 16777216
        initialNum = (initialNum >> 5  ^ initialNum)% 16777216
        initialNum = (initialNum << 11 ^ initialNum  )% 16777216
       
        value = initialNum%10
       
        encodedChange = value - prev & 0b11111  # Encode to 5 bits
        sequence = (sequence << 5) | encodedChange  # Shift left and insert
        sequence &= (1 << 20) - 1  # Truncate
       
      
        if i>2 and value>0:
            if sequence not in sequenceValues:
                sequenceValues[sequence] = value
                visitedSequences[sequence] = True
            else:
                if sequence not in visitedSequences:
                    sequenceValues[sequence] += value
                    visitedSequences[sequence] = True
                
        prev = value
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