from collections import defaultdict
class Scratchcard:
    def __init__(self, id, wins, draws):
        self.id = id
        self.wins = set(wins)
        self.draws = draws
    
    def get_next(self):
        score = 1
        for draw in self.draws:
            if draw in self.wins:
                score += 1
        return score, range(self.id, self.id+score-1)

class Scratchcard_collection:
    def __init__(self):
        self.cards = []
        with open("./Day4/cards.txt") as f:
            for i, line in enumerate(f):
                numbers = line.split("\n")[0].split(": ")[1] 
                wins, draws = numbers.split(" | ")

                wins = wins.split(" ")
                while("" in wins):
                    wins.remove("")

                draws = draws.split(" ")
                while("" in draws):
                    draws.remove("")
                self.cards.append(Scratchcard(i+1, wins, draws))
    
    def __len__(self):
        return len(self.cards)
    
    def scratch(self, index):
        return self.cards[index].get_next()

    def scratch_per_card(self, index):
        total = 0
        scratchcards = defaultdict(lambda: 1)
        for i in range(index):
            total += scratchcards[i]
            _, next_cards = self.cards[i].get_next()
            for j in next_cards:
                scratchcards[j] += scratchcards[i]
        return total

    def scratch_all(self):
        return self.scratch_per_card(len(self))

collect = Scratchcard_collection()
print(collect.scratch_all())