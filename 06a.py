with open("06-i.txt", "r") as fh:
    line = fh.readline()

i = 3

while i < len(line):
    slice = list(line[i-3:i+1])
    print(slice, set(slice))
    if len(slice) == len(set(slice)):
        break
    i += 1

i += 1
print("START OF PACKET:", i)