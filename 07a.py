import os
import copy

# def get_size(dir):
#     pass

class File():
    def __init__(self, path, size):
        self.path = path
        self.size = size

    def basename(self):
        return os.path.basename(self.path)

    def get_size(self):
        return self.size

class Dir():
    def __init__(self, path, contents):
        self.path = path
        self.contents = copy.deepcopy(contents)
        self.size = self._set_size()

    def basename(self):
        return os.path.basename(self.path)

    # def add_file(self, name, size):
    #     F = File(name, size)
    #     self.contents.append(F)

    # def add_dir(self, name):
    #     D = Dir(name)
    #     self.contents.append(D)

    # def list(self):
    #     for c in self.contents:
    #         print(c)

    def _set_size(self):
        total_size = 0
        for el in self.contents:
            total_size += el.get_size()
        self.size = total_size

    def get_size(self):
        return self.size

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
        print(d)

    for f in files:
        with open(f.path, "r") as fh:
            size = int(fh.read())
        print("File:", f.path, "Size:", size)
        total_size += size

    print("Total size:", total_size)
    return total_size

def create_dirs():
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

def get_file_size(filepath):
    with open(filepath, "r") as fh:
        return int(fh.read())

def get_dirs(dirpath):

    # Go through each directory at the path, create a Dir object and add to contents
    contents = []

    for fd in os.scandir(dirpath):
        if fd.is_dir():
            # Recursively call this function
            contents.append(get_dirs(fd))

        # For each file, read the size, create a File object, add it to contents
        if fd.is_file():
            size = get_file_size(fd.path)
            # Create new file and add to contents
            contents.append(File(fd.path, size))

    # Create directory object to return to caller with all the info about dirs and files
    # This will also calculate the size of the directory based on contents
    dir_obj = Dir(dirpath, contents)

    print(dir_obj.path, "--", dir_obj.contents)

    # return a dir object containing files with sizes, and calc dir object sizes as well
    return dir_obj

def main():
    # Create the files described the first time
    if not os.path.exists("rootdir"):
        create_dirs()
    
    # Get the root node for the tree
    root = get_dirs("rootdir")

    # if os.path.exists("rootdir"):
    #     get_size("rootdir")

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
