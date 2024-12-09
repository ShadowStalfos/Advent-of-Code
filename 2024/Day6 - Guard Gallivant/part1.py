"""Day 6 part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

guard_map = np.array([list(x) for x in data.split("\n")])
visited = np.zeros(guard_map.shape, dtype=bool)
rotations = 0
while True:
    guard_location = np.argwhere(guard_map == "^")[0]
    visited[guard_location[0], guard_location[1]] = True
    if guard_location[0] == 0:
        break
    if guard_map[guard_location[0] - 1, guard_location[1]] == "#":
        guard_map = np.rot90(guard_map)
        visited = np.rot90(visited)
        rotations += 1
    else:
        guard_map[guard_location[0] - 1, guard_location[1]] = "^"
        guard_map[guard_location[0], guard_location[1]] = "."

print(np.sum(visited))
