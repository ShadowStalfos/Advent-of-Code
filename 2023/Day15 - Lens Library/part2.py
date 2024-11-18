from aocd import get_data, submit

class Box:
    def __init__(self, id):
        self.id = id+1
        self.lenses = []
        self.label = []
    def new_lens(self, label, focal_length):
        if label not in self.label:
            self.lenses.append(focal_length)
            self.label.append(label)
        else:
            self.lenses[self.label.index(label)] = focal_length
    
    def remove_lens(self, label):
        if label in self.label:
            self.lenses.pop(self.label.index(label))
            self.label.pop(self.label.index(label))
    
    def get_power(self):
        total = 0
        for i, lens in enumerate(self.lenses):
            total += self.id*lens*(i+1)
        return total



TEST = False

if TEST:
    with open("./2023/Day15 - Lens Library/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=15, year=2023)

boxes = [Box(i) for i in range(256)]

split_data = data.split(",")

total = 0
for step in split_data:
    box_id = 0
    if step[-1] == "-":
        for char in step[:-1]:
            box_id = ((box_id + ord(char))*17)%256
        boxes[box_id].remove_lens(step[:-1])
    else:
        for char in step[:-2]:
            box_id = ((box_id + ord(char))*17)%256
        boxes[box_id].new_lens(step[:-2], int(step[-1]))

for box in boxes:
    total += box.get_power()

print(total)
submit(total, part="b", day=15, year=2023)
