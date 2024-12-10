"""Day N part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
from copy import deepcopy

def get_from_grid(x, y, default=None):
    if x < 0 or y < 0:
        return default
    try:
        return int(top_map[y][x]) if top_map[y][x] != "." else default
    except IndexError:
        return default
class Seeker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = get_from_grid(x, y)
    def find(self):
        if self.value == 9:
            return (1, [(self.x, self.y)])
        locations = []
        if get_from_grid(self.x+1, self.y) == self.value+1:
            locations.append((self.x+1, self.y))
        if get_from_grid(self.x-1, self.y) == self.value+1:
            locations.append((self.x-1, self.y))
        if get_from_grid(self.x, self.y+1) == self.value+1:
            locations.append((self.x, self.y+1))
        if get_from_grid(self.x, self.y-1) == self.value+1:
            locations.append((self.x, self.y-1))
        total = 0
        total_locations = []
        for loc in locations:
            result = Seeker(loc[0], loc[1]).find()
            total += result[0]
            total_locations.extend(result[1])
        return (total, list(set(total_locations)))

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-2:]), year=2024)

top_map = [list(x) for x in data.split("\n")]
top_map = np.array(top_map)

starting_points = np.argwhere(top_map == "0")

total_ends = 0
visited = np.zeros_like(top_map, dtype=bool)
for point in starting_points:
    seek = Seeker(point[1], point[0])
    found = seek.find()
    total_ends += len(found[1])
    for location in found[1]:
        visited[location[1], location[0]] = True
#print(np.where(visited, top_map, "#"))
print(total_ends)