from aocd import get_data
import numpy as np
from tqdm import tqdm
import copy

test = True

if test == True:
    with open("./2023/Day14 - Reflector Dish/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=14, year=2023)

data_list = np.array([list(x) for x in data.split("\n")])
pivoted_platform = np.rot90(data_list, 2)
history = copy.deepcopy(pivoted_platform)

for rotation in tqdm(range(1000000000)):
    pivoted_platform = np.rot90(pivoted_platform, 3)
    weight_total = 0
    for row in pivoted_platform:
        length = len(row)
        weight = 0
        for i in range(length):
            if row[i] == ".":
                pass
            elif row[i] == "#":
                length = len(row)-i-1
            elif row[i] == "O":
                row[i] = "."
                row[len(row)-length] = "O"
                weight += length
                length -= 1
        weight_total += weight
    if rotation%4==0:
        if (history == pivoted_platform).all():
            break
        else:
            history = copy.deepcopy(pivoted_platform)

print(weight_total)