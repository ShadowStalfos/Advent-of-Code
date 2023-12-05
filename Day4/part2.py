class Scratchcard:
    def __init__(self, id, wins, draws):
        self.id = id
        self.wins = wins
        self.draws = draws
    
    def get_next(self):
        for win, draws in zip(self.wins, self.draws):
            score = 0
            for draw in draws:
                if draw in win:
                    score += 1
        return score, range(self.id, self.id+score)

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
    
    def scratch(self, index):
        return self.cards[index].get_next()

    def scratch_recursive(self, index):
        index_list = [index]
        score = 0
        while len(index_list) > 0:
            score += 1
            i = index_list.pop(0)
            _, card_next = self.scratch(i)
            index_list += card_next
        return score
    
    def scratch_all(self, max_id):
        score = 0
        for i in range(max_id):
            score += self.scratch_recursive(i)
        return score

collect = Scratchcard_collection()
print(collect.scratch_all(188))