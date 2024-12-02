from aocd import get_data
import numpy as np

TEST = False

if TEST:
    with open("./2024/Day1 - Historian Hysteria/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=1, year=2024)


first, second = np.array([x.split("   ") for x in data.split("\n")], dtype=int).T
unique, counts = np.unique(second, return_counts=True)
counts = dict(zip(unique, counts))

similiarity = [counts[x] * x for x in first if x in second]
print(sum(similiarity))