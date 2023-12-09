import numpy as np
extrapol = 0
with open("./Day9 - OASIS/history.txt") as f:
    for line in f:
        values = np.array(line.split(), dtype=int)
        addition = [values[-1]]
        while(set(values) != set([0])):
            values = values[1:]-values[:-1]
            addition.append(values[-1])
        
        for value in addition:
            extrapol += value
print(extrapol)
            