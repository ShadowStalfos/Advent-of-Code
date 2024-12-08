"""Day N part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
from collections import defaultdict
from functools import cmp_to_key

TEST = True

def sorting_lists(a, b):
    if b in after[a]:
        return 1
    elif b in before[a]:
        return -1
    return 0

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

split = data.index("\n\n")
rules = [x.split("|") for x in data[:split].split("\n")]
updates = [x.split(",") for x in data[split+2:].split("\n")]

before = defaultdict(list)
after = defaultdict(list)

for rule in rules:
    after[rule[0].strip()].append(rule[1].strip())
    before[rule[1].strip()].append(rule[0].strip())

correct = 0
for update in updates:
    wrong = False
    for i in range(len(update)):
        if len(set(update[:i]) & set(after[update[i]])) > 0:
            wrong = True
            break
    if wrong:
        update.sort(key=cmp_to_key(sorting_lists))
        print(update)
        correct += int(update[int(len(update)/2)])
            

print(correct)