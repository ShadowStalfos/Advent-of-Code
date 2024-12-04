"""Day 3 part 2 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
import re

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

commands = re.findall("((mul)\(\d+,\d+\)|(do)\(\)|(don't)\(\))", data)
total = 0
do = True
for command in commands:
    if command[1] != "" and do:
        a, b = re.findall("\d+", command[0])
        total += int(a)*int(b)
    if command[2] != "":
        do = True
    if command[3] != "":
        do = False
    
print(total)
