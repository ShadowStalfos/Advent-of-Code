order = {"2": "1", 
         "3": "2", 
         "4": "3",
         "5": "4",
         "6": "5",
         "7": "6",
         "8": "7",
         "9": "8",
         "T": "9",
         "J": "0",
         "Q": "A",
         "K": "B",
         "A": "C"}

class Hand:
    def __init__(self, hand, bid):
        self.hand = list(hand)
        self.fil_hand = list(hand)
        self.bid = int(bid)
        self.jokers = 0

        while "J" in self.fil_hand:
            self.fil_hand.remove("J")
            self.jokers += 1

        if len(self.fil_hand) == 0:
            self.fil_hand = self.hand

        self.classify_hand()

    def classify_hand(self):
        self.rank = "0x"
        unique = set(self.fil_hand)
        match len(unique):
            #Five-of-a-kind
            case 1:
                self.rank += "6"
        
            #Four-of-a-kind or Full-House
            case 2:
                (num1, _) = unique
                #Four-of-a-kind
                if self.hand.count(num1) == 1 or self.hand.count(num1)+self.jokers == 4:
                    self.rank += "5"
                
                #Full-House
                else:
                    self.rank += "4"
            
            #Three-of-a-kind or Two-Pair
            case 3:
                (num1, num2, num3) = unique
                #Three-of-a-kind
                if self.hand.count(num1)+self.jokers == 3 or self.hand.count(num2)+self.jokers == 3 or self.hand.count(num3)+self.jokers == 3:
                    self.rank += "3"
                
                #Two-Pair
                else:
                    self.rank += "2"

            #One-Pair
            case 4:
                self.rank += "1"
            
            #High-card
            case _:
                self.rank += "0"

        for value in self.hand:
            self.rank += order[value]

    def get_winning(self, rank):
        return self.bid*rank
    
hands = {}
with open("./Day7 - Camel Cards/hands.txt") as f:
    for line in f:
        hand, bid = line.split("\n")[0].split(" ")
        current_hand = Hand(hand, bid)
        hands[int(current_hand.rank, 0)] = current_hand
    
ordered_ranks = sorted(hands.keys())
winnings = 0
for rank, key in enumerate(ordered_ranks):
    winnings += hands[key].get_winning(rank+1)

print(winnings)