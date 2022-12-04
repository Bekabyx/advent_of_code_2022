import string
import itertools

letter_values = {value: index + 1 for index, value in enumerate(string.ascii_letters)}


def split_bag_contents(bag_contents):
    char_list = list(bag_contents.strip())
    half_line_length = int(len(char_list) / 2)
    compartment_one = char_list[:half_line_length]
    compartment_two = char_list[half_line_length:]
    return [compartment_one, compartment_two]


def format_elf_group_bags(bags):
    formatted_bags = []
    for bag_contents in bags:
        formatted_bags.append(list(bag_contents.strip()))

    return formatted_bags

def get_intersection(bags):
    return list(set.intersection(*map(set, bags)))[0]


def get_priority_total(duplicated_items):
    total = 0
    for letter, occurrences in duplicated_items.items():
        total += (letter_values.get(letter) * occurrences)
    return total


def get_part_one_solution():
    with open("day_3/data.txt") as input_vals:
        lines = input_vals.readlines()
        all_duplicated_items = {}
        for line in lines:
            split_bag = split_bag_contents(line)
            duplicate_item = get_intersection(split_bag)
            if duplicate_item in all_duplicated_items:
                all_duplicated_items[duplicate_item] += 1
            else:
                all_duplicated_items[duplicate_item] = 1

        print(f"Part one total: {get_priority_total(all_duplicated_items)}")


def get_part_two_solution():
    with open("day_3/data.txt") as input_vals:
        all_duplicated_items = {}
        for elf_one, elf_two, elf_three in itertools.zip_longest(*[input_vals] * 3):
            bags = format_elf_group_bags([elf_one, elf_two, elf_three])
            duplicate_item = get_intersection(bags)
            if duplicate_item in all_duplicated_items:
                all_duplicated_items[duplicate_item] += 1
            else:
                all_duplicated_items[duplicate_item] = 1

        print(f"Part two total: {get_priority_total(all_duplicated_items)}")


if __name__ == "__main__":
    get_part_one_solution()
    get_part_two_solution()
