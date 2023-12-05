import numpy as np
import re
num_list = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
with open("./Day3/engine.txt") as f:
    engine = []
    for line in f:
        txt = line.split("\n")[0]
        engine.append(np.array(list(txt)))
engine = np.array(engine)

total_parts = 0
with open("./Day3/engine.txt") as f:
    for n, line in enumerate(f):
        i = 0
        while i < len(line):
            if line[i] in num_list: 
                min_i =  max(i-1,0)
                max_i = i+1
                while max_i<len(line) and line[max_i] in num_list:
                    max_i += 1
                if i == 0:
                    num = line[min_i:max_i]
                else:
                    num = line[min_i+1:max_i]
                surrounding = engine[max(n-1, 0):n+2,min_i:max_i+1]
                for element in surrounding.flatten():
                    if (not element.isnumeric()) and element!=".":
                        total_parts += int(num)
                        break

                i=max_i
            else:
                i+=1

print(total_parts)

