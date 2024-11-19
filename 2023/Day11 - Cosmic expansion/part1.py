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

inserts = 0
for i in range(len(space)):
    if len(np.unique(space[i+inserts])) == 1:
        space = np.insert(space, i+inserts, ".", axis=0)
        inserts += 1

inserts = 0
for j in range(space.shape[1]):
    if len(np.unique(space[:, j+inserts])) == 1:
        space = np.insert(space, j+inserts, ".", axis=1)
        inserts += 1

universe = Universe()
for i in range(space.shape[0]):
    for j in range(space.shape[1]):
        if space[i,j] == "#":
            space[i,j] = universe.add_galaxy(i,j)

print(universe.compare_pairs())