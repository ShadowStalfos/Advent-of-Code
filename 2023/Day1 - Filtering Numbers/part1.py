import re
total = 0
with open("./Day1/1/Codes.txt") as f:
    for line in f:
        numbers = re.findall("\d", line)
        total += int(numbers[0]+numbers[-1])
print(total)