iwin = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

value = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

equiv = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}


with open("02-i.txt", "r") as fh:
    totalscore = 0
    for line in fh:
        score = 0
        outcome = ""
        opponent, me = line.strip().split(" ")
        if equiv[opponent] == me:   # Draw - Me and opponent have equivalent letters (A=X, B=Y, C=Z)
            score += 3 + value[me]
            outcome = "DRAW"
        elif iwin[opponent] == me:  # I won - my letter beats opponent's letter (Y>A, Z>B, X>C)
            score += 6 + value[me]
            outcome = "I WIN"
        else:                       # I lost - opponent's letter beat my letter (A>Z, B>X, C>Y)
            score += value[me]
            outcome = "I LOSE"

        totalscore += score

        print(f"Opponent: {opponent} | Me: {me}. Outcome: {outcome}. Score: {score}")

print("------------")
print("TOTAL SCORE:", totalscore)