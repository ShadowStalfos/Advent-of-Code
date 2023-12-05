colour_dict = {"red": 0, "green": 1, "blue": 2}
power_total = 0
with open("./Day2/games.txt") as f:
    for line in f:
        game, draws = line.split(": ")
        game_id = int(game.split(" ")[1])
        draws = draws.split("\n")[0]
        draws = draws.split("; ")
        minimum = [0,0,0]
        for draw in draws:
            colour_draws = draw.split(", ")
            for colour_draw in colour_draws:
                count, colour = colour_draw.split(" ")
                index = colour_dict[colour]
                if int(count)>minimum[index]:
                    minimum[index] = int(count)
        power_total += minimum[0] * minimum[1] * minimum[2]
    print(power_total)