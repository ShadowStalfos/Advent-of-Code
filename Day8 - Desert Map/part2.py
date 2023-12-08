import re
from math import lcm

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

class Map:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, name, left, right):
        self.nodes[name] = Node(name, left, right)
    
    def navigate_one(self, name, direction):
        if direction == "L":
            return self.nodes[name].left
        else:
            return self.nodes[name].right
        
    def navigate_list(self, nav, nodes, end):
        count = []
        for node in nodes:
            i = 0
            while not set([node]).issubset(end):
                node = self.navigate_one(node, nav[i])
                i += 1
                if i == len(nav):
                    i = 0

            node = self.navigate_one(node, nav[i])
            i+=1
            steps = 1
            while not set([node]).issubset(end):
                node = self.navigate_one(node, nav[i])
                i += 1
                if i == len(nav):
                    i = 0
                steps += 1
            count.append(steps)
        return lcm(*count)


desert_map = Map()
with open("./Day8 - Desert Map/map.txt") as f:
    directions = list(next(f))
    directions.pop(-1)
    next(f)
    start = []
    end = set()
    for line in f:
        name, left, right = re.findall("([A-Z]{3})", line)
        if name[2] == "A":
            start.append(name)
        elif name[2] == "Z":
            end.add(name)

        desert_map.add_node(name, left, right)

print(desert_map.navigate_list(directions, start, end))
        