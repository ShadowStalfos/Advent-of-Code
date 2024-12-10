"""Day 9 part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os

TEST = False

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
        for i in range(len(disk_map)):
            count = disk_map[i]
            if not blocks:
                self.disk.extend(["." for _ in range(count)])
            else:
                self.disk.extend([ID for _ in range(count)])
                ID += 1
            blocks = not blocks
        self.disk = np.array(self.disk, dtype=str)
        self.filled = np.argwhere(self.disk != ".").flatten()[::-1]

    def restructure(self):
        for i in self.filled:
            self.empty = list(np.argwhere(self.disk == ".").flatten())
            if not self.empty:
                break
            if i < self.empty[0]:
                break
            ID = self.disk[i]
            self.disk[i] = "."
            self.disk[self.empty.pop(0)] = ID

    def calc(self):
        total = 0
        for i in range(len(self.disk)):
            if self.disk[i] == ".":
                break
            else:
                total+=i*int(self.disk[i])
        return total

result = Disk(disk_map)
result.restructure()
print(result.calc())