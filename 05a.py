crates = []
instructions = []
with open("05-i.txt", "r") as fh:
    lines = fh.readlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            i += 1
            break
        crates.append(line)
        i += 1

    while i < len(lines):
        line = lines[i]
        instructions.append(line)
        i += 1 

num_crates = int(crates[-1].split()[-1])
stacks = [ [] for _ in range(num_crates) ]
print("CRATES")
print(crates)
print("NUMBER OF CRATES")
print(num_crates)
print(stacks)

for row in crates[:-1]:
    print(row)
    col = 1
    while col < len(row):
        char = row[col]
        if char.strip() != "":
            stack_pos = int((col - 1) / 4)
            stacks[stack_pos].insert(0, char)
        col += 4

for stack in stacks:
    print(stack)