contain_pairs = 0

with open("04-i.txt", "r") as fh:
    for line in fh.readlines():
        line = line.strip()
        first, second = line.split(",")
        first_range = first.split("-")
        second_range = second.split("-")
        first_set = set([
            i for i in range(
                int(first_range[0]), int(first_range[1])+1
            )
        ])
        second_set = set([
            i for i in range(
                int(second_range[0]), int(second_range[1])+1
            )
        ])
        if set.issubset(first_set, second_set):
            contain_pairs += 1
            print("A CONTAINS B:", first_set, "--", second_set, f"({line})")
        elif set.issubset(second_set, first_set):
            contain_pairs += 1
            print("B CONTAINS A:", first_set, "--", second_set, f"({line})")
        else:
            print(first_set, "--", second_set, f"({line})")

print()
print("Total pairs where one contains the other:", contain_pairs)