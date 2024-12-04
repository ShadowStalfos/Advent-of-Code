from aocd import get_data
import numpy as np

TEST = False

if TEST:
    with open(f"{os.path.split(os.path.abspath(__file__))[0]}\\example.txt", "r", encoding="utf-8") as f:
        data = f.read()
else:
    data = get_data(day=int(__file__.split("\\")[-2].split(" -")[0][-1]), year=2024)

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

