import re
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
        
    def navigate_list(self, nav, start, end):
        current_node = "AAA"
        steps = 0
        i = 0
        while current_node != end:
            current_node = self.navigate_one(current_node, nav[i])
            i += 1
            steps += 1
            if i == len(nav):
                i = 0
        return steps


desert_map = Map()
with open("./Day8 - Desert Map/map.txt") as f:
    directions = list(next(f))
    directions.pop(-1)
    next(f)
    for line in f:
        name, left, right = re.findall("([A-Z]{3})", line)
        desert_map.add_node(name, left, right)

print(desert_map.navigate_list(directions, "AAA", "ZZZ"))
        