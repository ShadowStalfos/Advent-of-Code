"""Day N part 1 of AOC 2024"""

from aocd import get_data
import numpy as np
import os
from functools import cache

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    day = __file__.split("\\")[-2].split(" -")[0]
    if day[-2].isdigit():
        day = day[-2:]
    else:
        day = day[-1]
    data = get_data(day=int(day), year=2024)

stones = [x.split(" ") for x in data.split("\n")][0]

@cache
def get_stone_blinks(stone, blinks):
    if blinks == 0:
        return 1
    
    if stone == 0:
        return get_stone_blinks(1, blinks - 1)
    elif len(str(stone))%2 == 0:
        stone = str(stone)
        stone_a, stone_b = stone[:len(stone)//2], stone[len(stone)//2:]
        return get_stone_blinks(int(stone_a), blinks - 1) + get_stone_blinks(int(stone_b), blinks - 1)
    else:
        return get_stone_blinks(stone*2024, blinks - 1)
    
total = 0

for stone in stones:
    total += get_stone_blinks(int(stone), 25)

print(total)