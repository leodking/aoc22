iwin = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

ilose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

equiv = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

value = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

with open("02-i.txt", "r") as fh:
    totalscore = 0
    for line in fh:
        score = 0
        opponent, strategy = line.strip().split(" ")
        if strategy == "X":     # I must lose -> 0 + value of losing letter
            score += 0 + value[ilose[opponent]]
        elif strategy == "Y":   # I must draw -> 3 + value of opponent's letter
            score += 3 + value[equiv[opponent]]
        elif strategy == "Z":   # I must win -> 6 + value of winning letter
            score += 6 + value[iwin[opponent]]

        print(opponent, strategy, score)
        totalscore += score


print("------------")
print("TOTAL SCORE:", totalscore)