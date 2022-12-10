lines = ""
with open("08-i.txt", "r") as fh:
    lines = fh.readlines()

for l in lines:
    print(l, end="")

# 1st row and last row are visible automatically.
# 1st col and last col are visible automatically
# So add to the count, count of 1st and last line, plus number of lines - 2

count = len(lines[0]) + len(lines[-1]) + (len(lines) - 2)