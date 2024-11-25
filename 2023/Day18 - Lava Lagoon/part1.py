from aocd import get_data
import numpy as np
import pygame
from scipy import ndimage

class Lagoon:
    def __init__(self):
        self.area = np.array([[1]])
        self.position = (0,0)

    def dig(self, direction, distance):
        for _ in range(distance):
            self.add_edge()

            if direction == "U":
                self.area[self.position] = 2
                self.position = (self.position[0]-1, self.position[1])
                self.area[self.position] = 2

            elif direction == "D":
                self.area[self.position] = 2
                self.position = (self.position[0]+1, self.position[1])
                self.area[self.position] = 2

            elif direction == "L":
                self.position = (self.position[0], self.position[1]-1)
                self.area[self.position] = 1
            
            elif direction == "R":
                self.position = (self.position[0], self.position[1]+1)
                self.area[self.position] = 1

    def add_edge(self):
        if self.position[0] == self.area.shape[0]-1:
            self.area = np.append(self.area, np.zeros((1, self.area.shape[1])), axis=0)

        if self.position[1] == self.area.shape[1]-1:
            self.area = np.append(self.area, np.zeros((self.area.shape[0], 1)), axis=1)
        
        if self.position[0] == 0:
            self.area = np.append(np.zeros((1, self.area.shape[1])), self.area, axis=0)
            self.position = (self.position[0]+1, self.position[1])

        if self.position[1] == 0:
            self.area = np.append(np.zeros((self.area.shape[0], 1)), self.area, axis=1)
            self.position = (self.position[0], self.position[1]+1)

TEST = False

if TEST:
    with open("./2023/Day18 - Lava Lagoon/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=18, year=2023)


instructions = np.array([x.split(" ") for x in data.split("\n")])


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

lagoon = Lagoon()
for instruction in instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    lagoon.dig(instruction[0], int(instruction[1]))

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    square_height = screen.get_height()/(len(lagoon.area)+2)
    square_width = min(screen.get_width()/(len(lagoon.area[0])+2), square_height)
    for row in range(len(lagoon.area)):
        for col in range(len(lagoon.area[0])):
            if lagoon.area[row][col] > 0:
                pygame.draw.rect(screen, "red", ((1+col)*square_width, (1+row)*square_height, square_width, square_height))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    pygame.time.wait(10)

area = ndimage.binary_fill_holes(lagoon.area)
screen.fill("white")

square_height = screen.get_height()/(len(area)+2)
square_width = min(screen.get_width()/(len(area[0])+2), square_height)
for row in range(len(area)):
    for col in range(len(area[0])):
        if area[row][col] > 0:
            pygame.draw.rect(screen, "red", ((1+col)*square_width, (1+row)*square_height, square_width, square_height))
pygame.display.flip()
pygame.time.wait(10)

print("The area is:", np.sum(area))

    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
