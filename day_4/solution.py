def get_assignment_sets(assignments):
    shift_patterns = []
    for assignment in assignments:
        start, end = assignment.strip().split("-")
        shift_patterns.append(set(range(int(start), int(end)+1)))
    return shift_patterns


def check_assignment_subset(assignments):
    return assignments[0].issubset(assignments[1]) or assignments[1].issubset(assignments[0])


def check_assignment_intersection(assignments):
    return assignments[0].intersection(assignments[1])


def get_solution():
    with open("day_4/data.txt") as input_vals:
        lines = input_vals.readlines()
        subset_shift_patterns = 0
        intersecting_shift_patterns = 0
        for line in lines:
            pattern_one, pattern_two = line.strip().split(",")
            assignments = get_assignment_sets([pattern_one, pattern_two])

            if check_assignment_subset(assignments):
                subset_shift_patterns += 1
            if len(check_assignment_intersection(assignments)) > 0:
                intersecting_shift_patterns += 1

        print(f"Part one solution: {subset_shift_patterns}")
        print(f"Part two solution: {intersecting_shift_patterns}")


if __name__ == "__main__":
    get_solution()
