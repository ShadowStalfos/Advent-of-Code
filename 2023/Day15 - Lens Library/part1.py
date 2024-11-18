from aocd import get_data

TEST = True

if TEST:
    with open("./2023/Day15 - Lens Library/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=15, year=2023)

split_data = data.split(",")

total = 0
for step in split_data:
    subtotal = 0
    for char in step[:2]:
        subtotal = ((subtotal + ord(char))*17)%256
    print(subtotal)
    total += subtotal
print(total)
