import numpy as np
from colorama import Fore

lines = []

with open("08-i.txt", "r") as fh:
    for line in fh:
        lines.append(list(line.strip()))

arr = np.array(lines)

width, height = arr.shape

# 1st row and last row are visible automatically.
# 1st col and last col are visible automatically
# So add to the count, count of 1st and last line, plus number of lines - 2
# (don't count the corners on 1st and last row twice!)

count = width + width + (height - 2) + (height - 2)

for row in range(1, width-1):
    for col in range(1, height-1):
        num = arr[row, col]
        
        # First check from the left
        left = arr[row, :col]
        if max(left) < num:
            count += 1
            print(Fore.GREEN + num + Fore.RESET, end="")
            continue

        # Then check from the right
        right = arr[row, col+1:]
        if max(right) < num:
            count += 1
            print(Fore.GREEN + num + Fore.RESET, end="")
            continue

        # Then check from above
        above = arr[:row, col]
        if max(above) < num:
            count += 1
            print(Fore.GREEN + num + Fore.RESET, end="")
            continue

        # Lastly count from below
        below = arr[row+1:, col]
        if max(below) < num:
            count += 1
            print(Fore.GREEN + num + Fore.RESET, end="")
            continue

        print("-", end="")
    print()

print("Number of visible trees:", count)