colour_dict = {"red": 12, "green": 13, "blue": 14}
id_total = 0
with open("./Day2/games.txt") as f:
    for line in f:
        game, draws = line.split(": ")
        game_id = int(game.split(" ")[1])
        draws = draws.split("\n")[0]
        draws = draws.split("; ")
        impossible = False
        for draw in draws:
            colour_draws = draw.split(", ")
            for colour_draw in colour_draws:
                count, colour = colour_draw.split(" ")
                if int(count)>colour_dict[colour]:
                    impossible = True
        if not impossible:
            id_total += game_id
    print(id_total)