import numpy as np

with open("./advent-of-code/day25/input.txt", "r") as file:
    lines = file.read().splitlines()

keysList = []
locksList = []

for i in range(0,len(lines),8):
    dp = np.array([-1,-1,-1,-1,-1]) # Initialize dp array to -1 beacause of padding
    arr = np.array(lines[i:i+7])
    
    for row in arr:  
        for char in range(0,len(row)):
            if row[char] == '#':
                dp[char] += 1
        
    if arr[0] == "#####":
        keysList.append(dp)
    else:
        locksList.append(dp)
c = 0
cc = 0

for singleKey in keysList:
    for singleLock in locksList:
        if any(i>5 for i in singleKey+singleLock):
            continue
        else:
            c+=1

print(c)
print(cc)