from aocd import get_data
import numpy as np

TEST = True

if TEST:
    with open("./2023/Day17 - Clumsy Crucible/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=17, year=2023)

city = np.array([list(x) for x in data.split("\n")], dtype=int)
city = np.ones_like(city)
x, y = np.meshgrid(np.arange(city.shape[0]), np.arange(city.shape[1]))
heuristic = (((city.shape[0]-1-y) + (city.shape[1]-1-x)))
class Block:
    def __init__(self, x, y, loss, forward, direction, comes_from):
        self.x = x
        self.y = y
        self.loss = loss
        self.heuristic = heuristic[x, y]
        self.forward = forward+1
        self.direction = direction
        self.comes_from = comes_from

    def __repr__(self):
        #return self.direction_print()
        return str(self.forward)

    def __str__(self):
        return f"Block({self.x}, {self.y})"
    
    def __lt__(self, other):
        print(self, other, self.loss + self.heuristic < other.loss + other.heuristic)
        return self.loss + self.heuristic < other.loss + other.heuristic
    
    def direction_print(self):
        if self.direction == "N":
            return "^"
        if self.direction == "S":
            return "v"
        if self.direction == "E":
            return ">"
        if self.direction == "W":
            return "<"
        else:
            return "."

    def __eq__(self, other):
        return self.loss + self.heuristic == other.loss + other.heuristic

    def approx(self):
        return self.loss + self.heuristic

    def move(self):
        if self.x < city.shape[0]-1 and not (self.forward >= 3 and self.direction == "S") and not self.direction == "N":
            yield Block(self.x+1, self.y, self.loss+city[self.x+1, self.y], self.forward if self.direction == "S" else 0, "S", self)
        if self.y < city.shape[1]-1 and not (self.forward >= 3 and self.direction == "E") and not self.direction == "W":
            yield Block(self.x, self.y+1, self.loss+city[self.x, self.y+1], self.forward if self.direction == "E" else 0, "E", self)
        if self.x > 0 and not (self.forward >= 3 and self.direction == "N") and not self.direction == "S":
            yield Block(self.x-1, self.y, self.loss+city[self.x-1, self.y], self.forward if self.direction == "N" else 0, "N", self)
        if self.y > 0 and not (self.forward >= 3 and self.direction == "W") and not self.direction == "E":
            yield Block(self.x, self.y-1, self.loss+city[self.x, self.y-1], self.forward if self.direction == "W" else 0, "W", self)

grid = np.array([[Block(x, y, np.inf, -1, "", (0,0)) for y in range(city.shape[1])] for x in range(city.shape[0])])
grid[0][0].loss = 0

moves = [(0, 0)]

while moves:
    for newblock in grid[moves.pop(0)].move():
        if newblock.loss <= grid[newblock.x, newblock.y].loss:
            grid[newblock.x][newblock.y] = newblock
            if (newblock.x, newblock.y) not in moves:
                moves.append((newblock.x, newblock.y))
        # if newblock.x == city.shape[0]-1 and newblock.y == city.shape[1]-1:
        #     break
    moves = sorted(moves, key=lambda x: grid[x].approx(), reverse=True)
print(grid)
new_grid = np.array([[city[x][y] for y in range(city.shape[1])] for x in range(city.shape[0])], dtype=str)
coordinates = [city.shape[0]-1, city.shape[1]-1]
print(coordinates)
total = 0

while True:
    total += city[coordinates[0], coordinates[1]]
    new_grid[coordinates[0], coordinates[1]] = grid[coordinates[0], coordinates[1]].direction_print()
    coordinates = [grid[coordinates[0], coordinates[1]].comes_from.x, grid[coordinates[0], coordinates[1]].comes_from.y]

    if coordinates == [0,0]:
        break
print(grid)
print(new_grid)
print(total)
