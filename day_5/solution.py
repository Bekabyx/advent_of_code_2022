import itertools


def get_stacks(stack_data):
    stack_data.reverse()
    trimmed_stack_data = []

    for row in stack_data[1:]:
        trimmed_row = list(row)[1::4]
        trimmed_stack_data.append(trimmed_row)

    normalized_stack_data = list(zip(*itertools.zip_longest(*trimmed_stack_data, fillvalue=' ')))
    stacks = [list(column) for column in zip(*normalized_stack_data)]

    filtered_stacks = []
    for stack in stacks:
        filtered = filter(lambda crate: crate != ' ', stack)
        filtered_stacks.append(list(filtered))

    return filtered_stacks


def get_instruction_list(instruction_data):
    instruction_list = []
    for instruction in instruction_data.splitlines():
        instruction_parts = instruction.split(" ")
        instruction_list.append(dict(zip(instruction_parts[::2], instruction_parts[1::2])))

    return instruction_list


def run_cratemover_9000_instructions(instruction_list, stacks):
    for instruction in instruction_list:
        pop_from = int(instruction.get("from"))-1
        append_to = int(instruction.get("to"))-1
        no_items = int(instruction.get("move"))

        for i in range(no_items):
            crate_to_move = stacks[pop_from].pop()
            stacks[append_to].append(crate_to_move)

    return stacks


def run_cratemover_9001_instructions(instruction_list, stacks):
    for instruction in instruction_list:
        pop_from = int(instruction.get("from"))-1
        append_to = int(instruction.get("to"))-1
        no_items = int(instruction.get("move"))
        crates_to_move = []

        for i in range(no_items):
            crates_to_move.append(stacks[pop_from].pop())
        crates_to_move.reverse()
        stacks[append_to].extend(crates_to_move)

    return stacks


def get_top_crates(sorted_stacks):
    return [crate[-1] for crate in sorted_stacks]


def get_solution():
    with open("day_5/data.txt") as input_vals:
        lines = input_vals.read()
        stack_data, instruction_data = lines.split("\n\n")
        instructions = get_instruction_list(instruction_data)
        part_one_stacks = run_cratemover_9000_instructions(instructions, get_stacks(stack_data.splitlines()))
        part_two_stacks = run_cratemover_9001_instructions(instructions, get_stacks(stack_data.splitlines()))

        print(f"Part one solution: {get_top_crates(part_one_stacks)}")
        print(f"Part two solution: {get_top_crates(part_two_stacks)}")


if __name__ == "__main__":
    get_solution()
