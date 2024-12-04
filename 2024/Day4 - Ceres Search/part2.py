"""Day N part 2 of AOC 2024"""

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

corners = ["M", "S"]

for i in range(search.shape[0]):
    for j in range(search.shape[1]):
        if search[i,j] in corners:
            try:
                if search[i+1,j+1] == "A":
                    if search[i+2,j+2] in corners and not search[i,j] == search[i+2,j+2]:
                        if search[i, j+2] in corners and search[i+2, j] in corners and not search[i, j+2] == search[i+2, j]:
                            total += 1
                            found[i,j] = 1
                            found[i+1,j+1] = 1
                            found[i+2,j+2] = 1
                            found[i, j+2] = 1
                            found[i+2, j] = 1
            except:
                pass

print(total)
print(np.where(found, search, "."))