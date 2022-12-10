import numpy as np

def get_dist(arr_slice, tree):
    for index, num in enumerate(arr_slice):
        if num >= tree:
            return index + 1
    return len(arr_slice)

def main():
    lines = []

    with open("08-i.txt", "r") as fh:
        for line in fh:
            lines.append(list(line.strip()))

    arr = np.array(lines)

    width, height = arr.shape

    scenic_scores = []

    for row in range(1, width-1):
        for col in range(1, height-1):
            num = arr[row, col]

            # Check trees to the left to find the first blocking tree
            left = np.flip(arr[row, :col])
            left_dist = get_dist(left, num)

            # Next check trees to the right
            right = arr[row, col+1:]
            right_dist = get_dist(right, num)

            # Then the trees above
            above = np.flip(arr[:row, col])
            above_dist = get_dist(above, num)

            # And lastly, the trees below
            below = arr[row+1:, col]
            below_dist = get_dist(below, num)

            scenic_score = left_dist * right_dist * above_dist * below_dist
            scenic_scores.append(scenic_score)

    print("The maximum possible scenic score is:", max(scenic_scores))

if __name__ == "__main__":
    main()