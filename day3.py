from puzzle_inputs.rucksack_contents import rucksack_contents
import string

# Parsing the puzzle input string to a list where each item is the rucksack contents in 2 compartments
def parse_rucksack(rucksack_string):
    rucksack_array = rucksack_string.split('\n')
    for value in rucksack_array:
        middle_index = len(value) // 2
        first_half = value[:middle_index]
        second_half = value[middle_index:]
        index = rucksack_array.index(value)
        rucksack_array[index] = [first_half, second_half]
    return(rucksack_array)

# Finding the first repeating character and appending its numeric value as statd in the puzzle guide
def find_char_that_repeats_and_give_score(rucksack_array):
    repeating_elemet_array = []
    for rucksack in rucksack_array:
        for char in rucksack[0]:
            if(char in rucksack[1]):
                repeating_elemet_array.append((string.ascii_letters).index(char) + 1)
                break
    return repeating_elemet_array



parsed_rucksack = parse_rucksack(rucksack_contents)
score_array = find_char_that_repeats_and_give_score(parsed_rucksack)
# The sum of the list (answer to the puzzle part 1)
print(sum(score_array))

# Part 2
def parse_rucksack_part_two(rucksack_string):
    rucksack_array = rucksack_string.split('\n')
    return rucksack_array

# List where each item is one rucksack 
rucksack = parse_rucksack_part_two(rucksack_contents)

def split_in_groups_by_three(rucksack_array):
    for i in range(0, len(rucksack_array), 3):
        yield rucksack_array[i:i + 3]

grouped_elves = list(split_in_groups_by_three(rucksack))

# Part two
def find_matching_char(grouped_elves_list):
    repeating_elemet_array = []
    for elve_group in grouped_elves_list:
        unique_chars = set()
        for s in elve_group:
            for char in s:
                unique_chars.add(char)
    # Find the intersection of the sets of characters for each
        intersection = unique_chars.intersection(*elve_group)        
        if intersection:
            unique_char = next(iter(intersection))
            repeating_elemet_array.append((string.ascii_letters).index(unique_char) + 1)
    return repeating_elemet_array

# Answer of the second part pf the puzzle
print(sum(find_matching_char(grouped_elves)))
