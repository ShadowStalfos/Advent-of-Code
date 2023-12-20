import regex as re
import itertools

total = 0
with open("./Day12 - Hot Spring/springs.txt") as f:
    for index, line in enumerate(f):
        if index%50 == 0:
            print(index)
        springs, division = line.split("\n")[0].split(" ")
        division = division.split(",")
        division = [int(num) for num in division]
        blanksprings = springs.replace("?", ".")
        indices = [i for i in range(len(springs)) if springs[i] == "?"]
        for length in range(len(indices)+1):
            for subset in itertools.combinations(indices, length):
                newsprings = list(blanksprings)
                for i in subset:
                    newsprings[i] = "#"
                newsprings = [len(batch) for batch in re.findall("#+", "".join(newsprings))]
                if newsprings == division:
                    total+=1
print(total)
