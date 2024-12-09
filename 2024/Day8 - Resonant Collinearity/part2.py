"""Day 8 part 2 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
from itertools import combinations
from copy import deepcopy

TEST = False

def place(grid, direction, start, value):
    location = deepcopy(start)
    while -1 < location[0] < len(grid) and -1 < location[1] < len(grid[0]):
        grid[location[0], location[1]] = value
        location += direction
    location = deepcopy(start)
    while -1 < location[0] < len(grid) and -1 < location[1] < len(grid[0]):
        grid[location[0], location[1]] = value
        location -= direction
    return grid

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

antennas = np.array([list(x) for x in data.split("\n")])
unique_frequencies = np.unique(antennas)
unique_frequencies = unique_frequencies[unique_frequencies != "." ]

antinodes = np.zeros(antennas.shape, dtype=int)

for frequency in unique_frequencies:
    nodes = np.argwhere(antennas == frequency)
    for A, B in combinations(nodes, 2):
        diff = B - A
        antinodes = place(antinodes, diff, A, 1)

print(antinodes.sum())