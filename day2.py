# A,X - Rock 1
# B,Y - Paper 2
# C,Z - Scissors 3
# 0 = loss, 3 = draw, 6 = won

from puzzle_inputs.strategy_guide import strategy_guide

# Go over the puzzle input string to parse it in a list where each item is one round
def parse_puzzle(puzzle_string):
    input = puzzle_string.split('\n')
    for value in input:
        new_value = value.split(" ")
        i = input.index(value)
        input[i] = new_value
    return input
        
# Get a proper puzzle input
puzzle_array = parse_puzzle(strategy_guide)

# Calculating score of Part 1 , assuming the second item is our choice between rock paper siccors 
def return_round_score(round):
    loss = 0
    draw = 3
    won = 6
    match round[1]:
        case "X":
            if round[0] == "A":
                return draw + 1
            elif round[0] == "B":
                return loss + 1
            elif round[0] == "C":
                return won + 1
        case "Y":
            if round[0] == "A":
                return won + 2
            elif round[0] == "B":
                return draw + 2
            elif round[0] == "C":
                return loss + 2
        case "Z":
            if round[0] == "A":
                return loss + 3
            elif round[0] == "B":
                return won + 3
            elif round[0] == "C":
                return draw + 3


# Calculate the score of Part 2, figuring out which move to make in order to lose (X,0), draw (Y,3), win (Z,6)
def return_round_score_part_two(round):
    rock = 1
    paper = 2
    scissors = 3
    match round[1]:
        case "X":
            if round[0] == "A":
                return scissors
            elif round[0] == "B":
                return rock
            elif round[0] == "C":
                return paper
        case "Y":
            if round[0] == "A":
                return rock + 3
            elif round[0] == "B":
                return paper + 3
            elif round[0] == "C":
                return scissors + 3
        case "Z":
            if round[0] == "A":
                return paper + 6
            elif round[0] == "B":
                return scissors + 6
            elif round[0] == "C":
                return rock + 6

def calculate_score(puzzle_array):
    score = 0
    for round in puzzle_array:
        score = score + return_round_score_part_two(round)
    print(score)
    return score

calculate_score(puzzle_array)