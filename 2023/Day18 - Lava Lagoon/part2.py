from aocd import get_data
import numpy as np
import pygame

TEST = False

if TEST:
    with open("./2023/Day18 - Lava Lagoon/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=18, year=2023)


instructions = np.array([x.split(" ")[-1].strip("()#") for x in data.split("\n")])

def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

contour = [[0,0]]
total = 0
for instruction in instructions:
    distance = int(instruction[:-1], base=16)
    direction = int(instruction[-1])
    if direction == 0:
        contour.append([contour[-1][0]+distance, contour[-1][1]])

    elif direction == 1:
        contour.append([contour[-1][0], contour[-1][1]-distance])
    
    elif direction == 2:
        contour.append([contour[-1][0]-distance, contour[-1][1]])

    else:
        contour.append([contour[-1][0], contour[-1][1]+distance])
    
    total+=distance

contour = np.array(contour)
contour = contour.reshape(-1,2)


area = shoelace(contour)
print(area+total/2+1)

