overlap_pairs = 0

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

        intersection = set.intersection(first_set, second_set)
        print(intersection)
        if len(intersection) > 0:
            overlap_pairs += 1

print()
print("Number of pairs with overlapping items:", overlap_pairs)
