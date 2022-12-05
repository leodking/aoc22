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

crates = [c.strip("\n") for c in crates]

for row in crates[:-1]:
    col = 1
    while col < len(row):
        char = row[col]
        if char.strip() != "":
            stack_pos = int((col - 1) / 4)
            stacks[stack_pos].insert(0, char)
        col += 4

print("BEFORE MOVING")
for stack in stacks:
    print(stack)

for ins in instructions:
    ins_s = ins.split()
    # Parse instructions
    move_num, from_stack, to_stack = int(ins_s[1]), int(ins_s[3])-1, int(ins_s[5])-1
    c = stacks[from_stack][move_num*-1:]    # Select the last n letters from 'from_stack'
    len_s = len(stacks[from_stack])         # Calculate length of 'from_stack'
    stacks[from_stack] = stacks[from_stack][:len_s-move_num]    # Remove last n letters

    # Move selected letters to 'to_stack'
    stacks[to_stack].extend(c)

print()
print("AFTER MOVING")
answer = ""
for stack in stacks:
    answer += stack[-1]
    print(stack)

print()
print("ANSWER")
print(answer)
