class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir():
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.contents = []

    def add_file(self, name, size):
        F = File(name, size)
        self.contents.append(F)

    def add_dir(self, name):
        D = Dir(name)
        self.contents.append(D)

    def list(self):
        for c in self.contents:
            print(c)

with open("07-i.txt", "r") as fh:
    lines = fh.read().splitlines()

root = Dir("/")
root.add_dir(Dir("a"))
root.add_dir(Dir("b"))

print(root.list())

for i in range(1, 10):
    print(lines[i])
    if lines[i][0] == "$":  # Command - do something
        args = lines[i].split()[1:]
        print(args)
        if args[0] == "cd": # Create new dir
            pass
# root = Dir("/")