from aocd import get_data
import numpy as np

TEST = True

if TEST:
    with open("./2024/Day2 - Red-Nosed Reports/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=2, year=2024)

def test_sequence(sequence):
    direction = np.sign(int(sequence[1]) - int(sequence[0]))
    for i in range(len(sequence)-1):
        if 4>direction*(int(sequence[i+1]) - int(sequence[i]))>0:
            continue
        else:
            return False
    return True

reports = [x.split(" ") for x in data.split("\n")]
total = 0
for report in reports:
    if test_sequence(report):
        total += 1

print(total)

