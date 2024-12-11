"""Day 6 part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
from tqdm import tqdm

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

guard_map = np.array([list(x) for x in data.split("\n")])

def guard_walk(guard_map):
    visited = np.zeros([*guard_map.shape, 4], dtype=bool)
    visits = np.zeros(guard_map.shape, dtype=int)
    rotations = 0
    while True:
        guard_location = np.argwhere(guard_map == "^")[0]
        if visited[guard_location[0], guard_location[1], rotations]:
            return (True, np.rot90(visits, 4-rotations))
        if visits[guard_location[0], guard_location[1]] == 5:
            return (True, np.rot90(visits, 4-rotations))
        visited[guard_location[0], guard_location[1], rotations] = True
        visits[guard_location[0], guard_location[1]] += 1
        if guard_location[0] == 0: 
            return (False, np.rot90(visits, 4-rotations))
        if guard_map[guard_location[0] - 1, guard_location[1]] == "#":
            guard_map = np.rot90(guard_map)
            visited = np.rot90(visited)
            visits = np.rot90(visits)
            rotations = (rotations+1)%4
        else:
            guard_map[guard_location[0] - 1, guard_location[1]] = "^"
            guard_map[guard_location[0], guard_location[1]] = "."

total = 0
path = guard_walk(guard_map.copy())[1]
locations = np.argwhere(path > 0)
for place in tqdm(locations):
        if guard_map[place[0], place[1]] == ".":
            new_map = guard_map.copy()
            new_map[place[0], place[1]] = "#"
            total += guard_walk(new_map)[0]
            guard_map[place[0], place[1]] = "x"
print(total)