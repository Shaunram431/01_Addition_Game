game_summary = []

rounds_lost = 0
rounds_played = 5

for item in range(1, 6):
    result = input("choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1


    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost

# ***** Calculate Game Stats ******
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("***** Game History ******")
for game in game_summary:
    print(game)

print()

# displayed game starts with : values to the nearest whole number
print("****** Game Statistics ******")
print("win: {}, ({:.0f}%)\nLoss:{}, "
      "({:.0f}%)".format(rounds_won,
                                            percent_win,
                                            rounds_lost,
                                            percent_lose))
