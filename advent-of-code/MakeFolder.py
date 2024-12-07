import sys
import os

try:
    day = sys.argv[1]
    directory_name = "day" + str(day)
except:
    print("Folder name not given")
    exit()


try:
    os.mkdir(directory_name)
    f = open(f"./{directory_name}/{directory_name}.cpp", "x")
    f.write(r"int main(){return 0;}")
    f.close()
    f = open(f"./{directory_name}/main.py", "x")
    f.close()
    f = open(f"./{directory_name}/input.txt", "x")
    f.close()
    f = open(f"./{directory_name}/{directory_name}_2.cpp", "x")
    f.write(r"int main(){return 0;}")
    f.close()
    f = open(f"./{directory_name}/readme.md", "x")
    f.write(
        f"# [Day {day}](https://adventofcode.com/2024/day/{day})\n"
        f"### Usage\n"
        f"```\n"
        f"foo@bar:~$ make\n"
        f"```\n"
        f"### Output\n"
        f"```\n"
        f"```"
    )

    f.close()
    f = open(f"./{directory_name}/Makefile", "x")
    f.write(
        f"""all: {directory_name} {directory_name}_2 run
run: {directory_name}.exe {directory_name}_2.exe
\t{directory_name}.exe && {directory_name}_2.exe
{directory_name}: {directory_name}.cpp
\tg++ {directory_name}.cpp -o {directory_name}.exe
{directory_name}_2: {directory_name}_2.cpp
\tg++ {directory_name}_2.cpp -o {directory_name}_2.exe
"""
    )
    f.close()
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
