import numpy as np
num_list = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

def get_engine():
    with open("./Day3/engine.txt") as f:
        engine = []
        for lin in f:
            txt = lin.split("\n")[0]
            line = list(txt)
            i=0
            while i < len(line):
                if line[i] in num_list: 
                    min_i = i
                    max_i = i+1
                    while max_i<len(line) and line[max_i] in num_list:
                        max_i += 1
                    num = line[min_i:max_i]
                    num = "".join(num)
                    for i in range(min_i, max_i):
                        line[i] = num
                    i=max_i
                else:
                    i+=1
            engine.append(np.array(line))
    return np.array(engine)


engine = get_engine()
gear = 0
for y, line in enumerate(engine):
    for x, element in enumerate(line):
        if element == "*":
            surrounding = engine[max(y-1, 0):y+2, max(x-1, 0):x+2]
            surr_set = set()
            for surr in surrounding.flatten():
                if surr.isnumeric():
                    surr_set.add(surr)
            if len(surr_set) == 2:
                (a, b) = surr_set
                gear += int(a)*int(b)
print(gear)


