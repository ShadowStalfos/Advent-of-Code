"""Day 9 part 2 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
from tqdm import tqdm

TEST = True

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

disk_map = np.array([list(x) for x in data.split("\n")][0], dtype=int)

class Disk:
    def __init__(self, disk_map):
        self.disk_map = disk_map
        self.disk = []
        blocks = True
        ID = 0
        self.blocks = []
        self.empty = []
        for i in range(len(disk_map)):
            count = disk_map[i]
            if not blocks:
                self.empty.append([len(self.disk), count])
                self.disk.extend(["." for _ in range(count)])
            else:
                self.blocks.append([len(self.disk), count])
                self.disk.extend([ID for _ in range(count)])
                ID += 1
            blocks = not blocks
        self.disk = np.array(self.disk, dtype=str)
        self.blocks = np.array(self.blocks)[::-1]
        self.empty = np.array(self.empty)


    def restructure(self):
        for location, length in tqdm(self.blocks):
            for i, (e_loc, e_len) in enumerate(self.empty):
                if e_loc > location:
                    break

                if length <= e_len:
                    ID = self.disk[location]
                    self.disk[location:location+length] = "."
                    self.disk[e_loc:e_loc+length] = ID
                    if e_len-length == 0:
                        self.empty = np.delete(self.empty, i, axis=0)
                    else:
                        self.empty[np.argwhere(self.empty == [e_loc, e_len])[0][0]] = [e_loc+length, e_len-length]
                    break

    def calc(self):
        total = 0
        for i in range(len(self.disk)):
            if self.disk[i] == ".":
                continue
            else:
                total+=i*int(self.disk[i])
        return total

result = Disk(disk_map)
result.restructure()
print(result.calc())