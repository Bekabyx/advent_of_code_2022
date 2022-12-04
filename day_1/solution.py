import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--elves', '-e', help="Number of top elves calories to sum", type=int, default=3)


def get_per_elf_cal_counts():
    with open("day_1/data.txt") as input_vals:
        per_elf_calorie_counts = []
        elf_calorie_total = 0
        lines = input_vals.readlines()
        for line in lines:
            if line != "\n":
                elf_calorie_total += int(line)
            else:
                per_elf_calorie_counts.append(elf_calorie_total)
                elf_calorie_total = 0

        per_elf_calorie_counts = sorted(per_elf_calorie_counts, reverse=True)
        return per_elf_calorie_counts


def get_solution(no_elves):
    calorie_counts = get_per_elf_cal_counts()
    print(f"Top elf cal count: {calorie_counts[0]}")
    print(f"Top {no_elves} elves cal count: {sum(calorie_counts[:no_elves])}")


if __name__ == "__main__":
    args = parser.parse_args()
    get_solution(args.elves)
