"""Day 3 part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
import re

TEST = True

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

commands = re.findall("mul\(\d+,\d+\)", data)
total = 0
for command in commands:
    a, b = re.findall("\d+", command)
    total += int(a)*int(b)
print(total)
