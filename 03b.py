ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_priority = 0
with open('03-i.txt', 'r') as fh:
    lines = fh.readlines()
    for i in range(0, len(lines), 3):
        sets = [set(l.strip()) for l in lines[i:i+3]]
        common = set.intersection(*sets)
        priority = ALPHA.find(list(common)[0]) + 1
        total_priority += priority
        print(common, "--", priority)
        

print(total_priority)