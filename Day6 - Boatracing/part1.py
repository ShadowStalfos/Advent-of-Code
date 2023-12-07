with open("./Day6/races.txt") as f:
    lines = []
    for line in f:
        line = line.split("\n")[0].split(":")[1].split(" ")
        while("" in line):
            line.remove("")
        lines.append(line)
    time, distance = lines
valid = 1
for ms, mm in zip(time, distance):
    ms = int(ms)
    mm = int(mm)
    wins = 0
    for option in range(ms):
        if (ms-option)*option>mm:
            wins += 1
    valid *= wins
print(valid)

