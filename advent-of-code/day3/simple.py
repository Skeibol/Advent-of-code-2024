import re
res = 0
do = True
for op in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt", "r").read()):
    if op[2] == "(":  do = True
    elif op[2] == "n": do = False
    if do and op[2] == "l": res += int(re.findall(r"\d+", op)[0]) * int(re.findall(r"\d+", op)[1])
print(res)