import numpy as np
from math import ceil
compass = {0: np.array([-1, 0]),
           1: np.array([0, 1]),
           2: np.array([1, 0]),
           3: np.array([0, -1])}

guide = {"|": {0: 0, 2: 2},
         "-": {1: 1, 3: 3},
         "L": {3: 0, 2: 1},
         "J": {1: 0, 2: 3},
         "7": {0: 3, 1: 2},
         "F": {0: 1, 3: 2}}
maze = np.array([])

with open("./Day10 - Pipeline Maze/maze.txt") as f:
    for line in f:
        maze = np.append(maze, np.array(list(line)[:-1]))
        line_len = len(line)-1

maze = maze.reshape((-1, line_len))
startx, starty = np.where(maze=="S")
x = startx[0]
y = starty[0]

#North
if maze[x-1, y] in {"F", "7", "|"}:
    x -= 1
    direction = 0
#East
elif maze[x, y+1] in {"J", "7", "-"}:
    y += 1
    direction = 1
#South
elif maze[x+1, y] in {"J", "L", "|"}:
    x += 1
    direction = 2

area = startx[0]*y - starty[0]*x
new_maze = np.zeros(maze.shape, dtype=str)
new_maze[:] = "."
current = maze[x, y]
new_maze[x,y] = maze[x,y]
parts = 1
while current != "S":
    direction = guide[current][direction]
    oldx, oldy = x, y
    x, y = [x,y]+compass[direction]
    current = maze[x, y]
    new_maze[x,y] = maze[x,y]
    #print(np.array([[oldx, x], [oldy,y]]))
    area += oldx*y - oldy*x
    parts += 1

print((area/2)-parts)

np.savetxt("./Day10 - Pipeline Maze/new_maze.txt", new_maze, fmt="%c", delimiter="")