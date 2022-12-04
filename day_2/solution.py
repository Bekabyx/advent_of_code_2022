from enum import Enum


class PlayScores(Enum):
    rock = 1
    paper = 2
    scissors = 3
    win = 6
    lose = 0
    draw = 3


def parse_move(move):
    if move in ["A", "X"]:
        return "rock"
    elif move in ["B", "Y"]:
        return "paper"
    elif move in ["C", "Z"]:
        return "scissors"
    else:
        return None


def get_player_move(elf_move, player_instruction):
    if player_instruction == "X":
        return MATCHUPS.get(elf_move).get("wins_against")
    elif player_instruction == "Y":
        return elf_move
    elif player_instruction == "Z":
        return MATCHUPS.get(elf_move).get("loses_against")


MATCHUPS = {
    "rock": {
        "loses_against": "paper",
        "wins_against": "scissors"
    },
    "paper": {
        "loses_against": "scissors",
        "wins_against": "rock"
    },
    "scissors": {
        "loses_against": "rock",
        "wins_against": "paper"
    }

}


def get_matchup_points(elf_move, player_move):
    if MATCHUPS.get(elf_move).get("loses_against") == player_move:
        return PlayScores.win.value
    elif MATCHUPS.get(elf_move).get("wins_against") == player_move:
        return PlayScores.lose.value
    else:
        return PlayScores.draw.value


def get_result(line, part=1):
    elf_move, player_move = line.strip().split(" ")
    parsed_elf_move = parse_move(elf_move)
    if part == 1 or part != 2:
        parsed_player_move = parse_move(player_move)
    elif part == 2:
        parsed_player_move = get_player_move(parsed_elf_move, player_move)

    matchup_points = get_matchup_points(parsed_elf_move, parsed_player_move)
    move_points = PlayScores[parsed_player_move].value

    return matchup_points + move_points


def get_solution():
    with open("day_2/data.txt") as input_vals:
        lines = input_vals.readlines()
        part_one_total_score = 0
        part_two_total_score = 0
        for line in lines:
            if line != "\n":
                part_one_line_result = get_result(line, part=1)
                part_one_total_score += part_one_line_result

                part_two_line_result = get_result(line, part=2)
                part_two_total_score += part_two_line_result

        print(f"Part one score: {part_one_total_score}")
        print(f"Part two score: {part_two_total_score}")


if __name__ == "__main__":
    get_solution()
