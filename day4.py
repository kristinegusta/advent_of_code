from puzzle_inputs.section_assignments import section_assignment_string

# Parsing the section assignment string to a list where each list item is an assignment pair
def parse_input(input_string):
    input_list = input_string.split('\n')
    for i, pair in enumerate(input_list):
        input_list[i] = pair.split(',')
    return input_list

input_list = parse_input(section_assignment_string)

# Function to return a string of numbers in a given range, for example, '2-6' to '2,3,4,5,6'
def change_range_to_string(range_string):
    list_of_start_stop = range_string.split('-')
    start = int(list_of_start_stop[0])
    stop = int(list_of_start_stop[1])
    range_list = set(range(start, stop+1))
    # range_string = ','.join(map(str,range_list))
    return range_list

# Parsing each asignment pair string to a list of numbers in a given range
def parse_input_list_range(input):
    for value in input:
        for i, item in enumerate(value):
            value[i] = change_range_to_string(item)
    return input

list_with_range_as_string = parse_input_list_range(input_list)

# Check if an assigment is fully covered by both elves
def check_if_fully_contains_and_calc_result(list):
    result = 0
    for value in list:
        if value[0].issubset(value[1]) or value[1].issubset(value[0]):
            result += 1
    return result

# Answer for part one
print(check_if_fully_contains_and_calc_result(list_with_range_as_string))

# Part two

# Check if there is any intersection
def check_if_any_itersection(set):
    result = 0
    for value in set:
        if not value[0].isdisjoint(value[1]):
            result +=1
    return result

print(check_if_any_itersection(list_with_range_as_string))