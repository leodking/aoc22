import os

# def get_size(dir):
#     pass

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

    def get_size(self):
        pass

def get_size(dirpath):
    dirs = []
    files = []
    for fd in os.scandir(dirpath):
        if fd.is_dir():
            dirs.append(fd)
        elif fd.is_file():
            files.append(fd)

    total_size = 0

    for d in dirs:
        total_size += get_size(d)
        # print(d)

    for f in files:
        with open(f.path, "r") as fh:
            size = int(fh.read())
        print("File:", f.path, "Size:", size)
        total_size += size

    print("Total size:", total_size)
    return total_size

def main():
    # Create the files described the first time
    if not os.path.exists("rootdir"):
        with open("07-i.txt", "r") as fr:
            lines = fr.read().splitlines()
        os.mkdir("rootdir")
        os.chdir("rootdir")
        for line in lines[1:]:
            args = line.split()
            if args[0] == "$":  # Command
                if args[1] == "cd":
                    os.chdir(args[2])
                    print("Navigating to", args[2])
            else:               # file or dir
                if args[0] == "dir":    # dir
                    os.mkdir(args[1])
                    print("Creating dir", args[1])
                else:                   # file
                    fname, fsize = args[1], args[0]
                    if not os.path.exists(fname):
                        print("Creating file", fname)
                        with open(fname, 'w') as fw:    # Create file in directory
                            fw.write(fsize)             # Write file size into file
    
    if os.path.exists("rootdir"):
        get_size("rootdir")

if __name__ == "__main__":
    main()
# root = Dir("rootdir")

# for root, subdirs, files in os.walk("rootdir", topdown=False):
#     # print("--\n"+root)
#     for sd in subdirs:
#         print(os.path.join(root, sd))
#     for fl in files:
#         print(os.path.join(root, fl))
# root.add_dir(Dir("a"))
# root.add_dir(Dir("b"))

# print(root.list())
