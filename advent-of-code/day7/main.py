from functools import reduce
from operator import mul
import itertools
from time import perf_counter, sleep
start = perf_counter()
f = open("./advent-of-code/day7/input.txt", "r")

results = []
operators = []
numbers = []
foundBadSamples = 0
cnt = 0
for line in f.readlines():
    splitLine = line.split(":")
    results.append(int(splitLine[0]))
    numbers.append([int(i) for i in splitLine[1][:-1].strip().split(" ")])


def tryCalculateLine(result, line):

    operators = itertools.product(*([["+", "|", "*"]] * (len(line) - 1)))
    res = 0
    for op in operators:
        for idx, num in enumerate(line):

            if idx == 0:
                res = num
            else:
                if op[idx - 1] == "+":
                    res += num
                elif op[idx - 1] == "|":
                    res = int(str(res) + str(num))
                elif op[idx - 1] == "*":
                    res *= num
        #print(f"Calculated {res} for {result} : {[i for i in line]} - {[o for o in op]}")
                    
        if res == result:
            return result

    return 0


solution = 0
cnt = 0
for result, num in zip(results, numbers):
    # if(sum(num) > result or reduce(mul, num) < result):
    #     foundBadSamples+=1
    #     continue
    if tryCalculateLine(result, num):
        solution += result
    cnt += 1
    #print(f"{cnt} of {len(numbers)} done")
    # print(f"{result} : {[i for i in num]} - possible - sum {cnt} - calculated {tryCalculateLine(result,num)}")
    # cnt += result


print(solution)
end = perf_counter() - start
print(f"Time elapsed : {end}")