def get_cards():
    with open("./Day4/cards.txt") as f:
        win_list = []
        draw_list = []
        for line in f:
            numbers = line.split("\n")[0].split(": ")[1] 
            wins, draws = numbers.split(" | ")

            wins = wins.split(" ")
            while("" in wins):
                wins.remove("")
            win_list.append(wins)

            draws = draws.split(" ")
            while("" in draws):
                draws.remove("")
            draw_list.append(draws)
    return win_list, draw_list

wins, draws_list = get_cards()
total = 0
for win, draws in zip(wins, draws_list):
    score = 0
    for draw in draws:
        if draw in win:
            if score == 0:
                score = 1
            else:
                score *= 2
    total+=score

print(total)