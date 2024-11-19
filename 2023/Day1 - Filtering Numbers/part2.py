import re

word_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

with open("./Day1/Codes.txt") as f:
    total = 0
    for line in f:
        line_dict = {}

        for word, num in word_dict.items():
            indexes = [m.start() for m in re.finditer(word, line)]
            for i in indexes:
                line_dict[i] = num

        for num in range(10):
            num = str(num)
            indexes = [m.start() for m in re.finditer(num, line)]
            for i in indexes:
                line_dict[i] = num
        
        ordered_keys = sorted(list(line_dict.keys()))
        total += int(line_dict[ordered_keys[0]] + line_dict[ordered_keys[-1]])
            
print(total)