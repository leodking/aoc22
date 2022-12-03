ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_priority = 0
with open('03-i.txt', 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        first, second = line[0:len(line)//2], line[len(line)//2:]
        common = (set(first).intersection(set(second)))
        priority = ALPHA.find(list(common)[0]) + 1
        total_priority += priority
        print(line, "--", common, "--", priority)

print(total_priority)