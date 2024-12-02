from aocd import get_data

TEST = True

if TEST:
    with open("./2023/Day19 - Aplenty/example.txt") as f:
        data = f.read()
else:
    data = get_data(day=19, year=2023)

split = data.index("\n\n")
steps = data[:split].split("\n")
parts = data[split+2:].split("\n")
workflow = dict()

for step in steps:
    name = step.split("{")[0]
    instructions = step[step.index("{"):]
    instructions = instructions.replace("{", "").replace("}", "").split(",")
    inst_dict = dict()
    for inst in instructions[:-1]:
        inst = inst.split(":")
        inst_dict[inst[0]] = inst[1]
    inst_dict["_other"] = instructions[-1]
    workflow[name] = inst_dict

total = 0
for part in parts:
    part = part.replace("{","").replace("}","").split(",")
    for i in part:
        exec(i)
    location = "in"
    while location not in ["A", "R"]:
        step = workflow[location]
        for i in step.keys():
            if i != "_other" and eval(i):
                location = step[i]
                break
        else:
            location = step["_other"]
    if location == "A":
        total += x+m+a+s

print(total)
    