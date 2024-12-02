from aocd import get_data
import numpy as np

TEST = False

if TEST:
    with open("./2024/Day1 - Historian Hysteria/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=1, year=2024)


locations = np.array([x.split("   ") for x in data.split("\n")], dtype=int).T
locations = np.sort(locations, axis=1)
print(np.sum(abs(locations[1] - locations[0])))