def get_start_of_sequence_position(chunk_size, input_list):
    for i in range(len(input_list)):
        chunk = input_list[i:i + chunk_size]
        if len(set(chunk)) == chunk_size:
            return i + chunk_size


def get_solution():
    with open("day_6/data.txt") as input_vals:
        sequence = input_vals.read()
        listified_input = list(sequence)
        part_one_answer = get_start_of_sequence_position(chunk_size=4, input_list=listified_input)
        part_two_answer = get_start_of_sequence_position(chunk_size=14, input_list=listified_input)
        print(f"Part one answer: {part_one_answer}")
        print(f"Part two answer: {part_two_answer}")


if __name__ == "__main__":
    get_solution()
