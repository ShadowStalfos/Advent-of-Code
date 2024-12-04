"""Day 4 part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

search = np.array([list(x) for x in data.split("\n")])
found = np.zeros(search.shape)
total=0
for _ in range(4):
    search = np.rot90(search, 1)
    found = np.rot90(found, 1)
    for i in range(search.shape[0]):
        for j in range(search.shape[1]):
            if search[i,j] == "X":
                try:
                    if search[i+1,j] == "M" and search[i+2,j] == "A" and search[i+3,j] == "S":
                        total += 1
                        found[i:i+4,j] = 1
                except:
                    pass
                # try:
                #     if search[i,j+1] == "M" and search[i,j+2] == "A" and search[i,j+3] == "S":
                #         total += 1
                #         found[i,j:j+4] = 1
                # except:
                #     pass
                try:
                    if search[i+1,j+1] == "M" and search[i+2,j+2] == "A" and search[i+3,j+3] == "S":
                        total += 1
                        found[i,j] = 1
                        found[i+1,j+1] = 1
                        found[i+2,j+2] = 1
                        found[i+3,j+3] = 1
                except:
                    pass

print(total)
print(np.where(found, search, "."))