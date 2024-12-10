"""Day N part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
import itertools
from tqdm import tqdm

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

equations = [x.split(": ") for x in data.split("\n")]

part_total = 0
for equation in tqdm(equations):
    result, equation = equation
    result = int(result)
    numbers = [x for x in equation.split(" ")]
    done = False
    for possible_operators in itertools.combinations_with_replacement(["+", "*"], len(numbers)-1):
        if done == False:
            for operators in itertools.permutations(possible_operators):
                total = numbers[0]
                for i in range(len(operators)):
                    exec(f"total = {total} {operators[i]} {numbers[i+1]}")
                    if total > result:
                        break
                if total == result:
                    done = True
                    break
    if done == True:
        part_total += result
print(part_total)