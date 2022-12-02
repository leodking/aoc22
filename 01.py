numlist = []

with open("01-i.txt", 'r') as fh:
    num = 0
    for line in fh:
        if line.strip() == "":
            numlist.append(num)
            num = 0
        else:
            num += int(line)

print(sorted(numlist))
print(sum(sorted(numlist)[-3:]))