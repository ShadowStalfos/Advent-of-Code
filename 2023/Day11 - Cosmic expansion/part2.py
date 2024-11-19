import numpy as np

class Universe:
    def __init__(self):
        self.galaxies = []
    
    def compare_pairs(self):
        total = 0
        for i in range(len(self.galaxies)):
            for j in range(i+1, len(self.galaxies)):
                total += self.galaxies[i].distance(self.galaxies[j])
        return total

    def add_galaxy(self, x, y):
        self.galaxies.append(Galaxy(x, y))
        return len(self.galaxies)

class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, galaxy):
        return abs(self.x-galaxy.x)+abs(self.y-galaxy.y)

space = []
with open("./Day11 - Cosmic expansion/space.txt") as f:
    for line in f:
        space.append(list(line.split("\n")[0]))
space = np.array(space)

EXPANSION = 1000000

universe = Universe()
expand_y = 0
for i in range(space.shape[0]):
    if len(np.unique(space[i])) == 1:
        expand_y += EXPANSION-1
        continue

    expand_x = 0
    for j in range(space.shape[1]):
        if len(np.unique(space[:, j])) == 1:
            expand_x += EXPANSION-1
            continue

        if space[i,j] == "#":
            space[i,j] = universe.add_galaxy(i+expand_y,j+expand_x)

print(universe.compare_pairs())
print(space)

np.savetxt("./Day11 - Cosmic expansion/categorized_space.txt", space, fmt="%c", delimiter="")