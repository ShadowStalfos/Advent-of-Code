from aocd import get_data
import numpy as np

TEST = False

if TEST:
    with open("./2023/Day16 - Lava Floor/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=16, year=2023)


grid = np.array([list(x) for x in data.split("\n")])
energy = np.zeros(grid.shape)
beams = []
history = []
class beam:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        if (x, y, direction) not in history:
            history.append((x, y, direction))
            
        else:
            self.x = -1000
        
    def run(self):
        while True:
            self.x = self.x + self.direction[0]
            self.y = self.y + self.direction[1]
            if -1 < self.x < len(grid) and -1 < self.y < len(grid[0]):
                energy[self.y, self.x] += 1
                if grid[self.y][self.x] == "|" and self.direction[0] != 0:
                    beams.append(beam(self.x, self.y, (0, 1)))
                    beams.append(beam(self.x, self.y, (0, -1)))
                    break
                elif grid[self.y][self.x] == "-" and self.direction[1] != 0:
                    beams.append(beam(self.x, self.y, (1, 0)))
                    beams.append(beam(self.x, self.y, (-1, 0)))
                    break
                elif grid[self.y][self.x] == "\\":
                    beams.append(beam(self.x, self.y, (self.direction[1], self.direction[0])))
                    break
                elif grid[self.y][self.x] == "/":
                    beams.append(beam(self.x, self.y, (-self.direction[1], -self.direction[0])))
                    break
            else:
                break

beams.append(beam(-1, 0, (1, 0)))
while beams:
    beams.pop(0).run()

energy[energy>0] = 1

print(energy.sum())