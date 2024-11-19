import numpy as np

class Pattern:
    def __init__(self, pattern: list):
        self.pattern = pattern
        self.multiplier = 100
    
    def check_mirror(self):
        for i in range(len(self.pattern)-1):
            if (self.pattern[i] != self.pattern[i+1]).any():
                continue
            true_mirror = True
            for j in range(1, min(i+1, len(self.pattern)-i-1)):
                if (self.pattern[i-j] != self.pattern[i+j+1]).any():
                    true_mirror = False
                    break

            if true_mirror:
                return (i+1)*self.multiplier
        if self.multiplier == 1:
            return 0
            
        self.pattern = self.pattern.T
        self.multiplier = 1
        return self.check_mirror()

maps = []
with open("Day13 - Mirrors/patterns.txt") as f:
    pattern = np.array(list(next(f).strip("\n")))
    new = False
    for line in f:
        if new:
            new = False
            pattern = np.array(list(line.strip("\n")))
        elif line[0] == "\n":
            new = True
            maps.append(Pattern(pattern))
        else:
            pattern = np.vstack((pattern, list(line.strip("\n"))))
    maps.append(Pattern(pattern))

total = 0
for map in maps:
    total += map.check_mirror()

print(total)
        
            
            