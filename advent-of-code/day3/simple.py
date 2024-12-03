import re
from time import perf_counter,sleep

start = perf_counter()
res = 0
do = True
for op in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt", "r").read()):
    if op[2] == "(":  do = True
    elif op[2] == "n": do = False
    if do and op[2] == "l": 
        reg = re.findall(r"\d+", op)
        res += int(reg[0]) * int(reg[1])
print(res)
end = perf_counter() - start
print(end)
