import numpy as np

# grid = np.zeros((100,100), dtype="S1")
# grid[0,50] = 'H'
# print(grid)
# print(grid.nbytes)

def get_grid_size(input):    
    max_steps = {
        'L': 0,
        'R': 0,
        'U': 0,
        'D': 0,
    }

    sum_steps = {
        'L': 0,
        'R': 0,
        'U': 0,
        'D': 0,
    }

    all_steps = {
        'L': [],
        'R': [],
        'U': [],
        'D': [],
    }

    for line in sorted(input):
        dir, steps = line.split()
        steps = int(steps)
        all_steps[dir].append(steps)
        # if max_steps[dir] < steps:
        #     max_steps[dir] = steps
        
    

    # print(all_steps)
    sum_r = sum(all_steps['R'])
    sum_l = sum(all_steps['L'])

    if sum_l > sum_r:
        width = sum_r + ((sum_r - sum_l) * -1)
    else:
        width = sum_r

    print(sum_r, sum_l, sum_r - sum_l)
    print("WIDTH:", width)

    sum_u = sum(all_steps['U'])
    sum_d = sum(all_steps['D'])

    if sum_u > sum_d:
        height = sum_d + ((sum_d - sum_u) * -1)
    else:
        height = sum_d

    print("HEIGHT:", height)

    # print(max_r, sum_r, sum_l)
    

    # exit(0)
    
    # width = (max_steps['L'] + max_steps['R']) * 4
    # height = (max_steps['U'] + max_steps['D']) * 4
    
    return width, height

def main():
    with open("09-i.txt", "r") as fh:
        lines = fh.read().splitlines()
    width, height = get_grid_size(lines)

    spos = [(height // 2) - 1, (width // 2) - 1]    # Start position
    hpos = [spos[0], spos[1]]                   # Head position
    tpos = [spos[0], spos[1]]                   # Tail position

    grid = np.zeros((height, width), dtype='S1')
    grid[spos[0], spos[1]] = 'H'
    print(width, height, spos)

    first_hpos = hpos.copy()

    # Parse instructions, move head and tail
    for line in lines:
        dir, steps = line.split()
        steps = int(steps)
        match dir:
            case "L":
                for _ in range(steps):
                    if hpos[1] - 1 >= 0:
                        print("hpos before:", hpos, end=" -- ")
                        hpos[1] -= 1
                        print("hpos after:", hpos, "dir --", dir, "steps --", steps)
                    else:
                        print(hpos, steps)
                        raise RuntimeError("We've calculated the width wrong here...")
            case "R":
                for _ in range(steps):
                    if hpos[1] + 1 < width:
                        print("hpos before:", hpos, end=" -- ")
                        hpos[1] += 1
                        print("hpos after:", hpos, "dir --", dir, "steps --", steps)
                    else:
                        print(hpos, steps)
                        raise RuntimeError("We've calculated the width wrong here...")
            case "U":
                for _ in range(steps):
                    if hpos[0] - 1 >= 0:
                        print("hpos before:", hpos, end=" -- ")
                        hpos[0] -= 1
                        print("hpos after:", hpos, "dir --", dir, "steps --", steps)
                    else:
                        print(hpos, steps)
                        raise RuntimeError("We've calculated the height wrong here...")
            case "D":
                for _ in range(steps):
                    if hpos[0] + 1 < height:
                        print("hpos before:", hpos, end=" -- ")
                        hpos[0] += 1
                        print("hpos after:", hpos, "dir --", dir, "steps --", steps)
                    else:
                        print(hpos, steps)
                        raise RuntimeError("We've calculated the width wrong here...")

    last_hpos = hpos.copy()

    print("Head position:", hpos)

    print("first:", first_hpos)
    print("last:", last_hpos)

    # with np.printoptions(threshold=np.inf):
    #     print(grid)

if __name__ == "__main__":
    main()