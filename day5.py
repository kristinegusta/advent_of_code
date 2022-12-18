from puzzle_inputs.cargo import positions, steps

strategy_guide = steps.split('\n')

# Parsing the strategy guide to a list that each item is a list with numeric values
rearrangement_procedure = []

for move in strategy_guide:
    # Spliting the move string first
    move_split = move.split(' ')
    move_with_numbers = []
    for v in move_split:
        if v.isdigit():
            move_with_numbers.append(int(v))

    rearrangement_procedure.append(move_with_numbers)

# Part 1 moves
# for move in rearrangement_procedure:
#     # First, get the items that need to be moved (move x amount from y). Remember the index will be y-1. can use .pop()
#     loop_counter = 0
#     amount_of_boxes_to_move = move[0]
#     while loop_counter < amount_of_boxes_to_move:
#         removed_box = positions[move[1]-1].pop()
#         positions[move[2]-1].append(removed_box)
#         loop_counter += 1



# Part two moves
for move in rearrangement_procedure:
    amount_of_boxes_to_move = move[0]
    from_this_stack = positions[move[1]-1]
    to_this_stack = positions[move[2]-1]

    if amount_of_boxes_to_move == 1:
        removed_box = from_this_stack.pop()
        to_this_stack.append(removed_box)
    else:
        # Get the items and append them
        removed_boxes = from_this_stack[-amount_of_boxes_to_move:]
        for box in removed_boxes:
            to_this_stack.append(box)
        # Then, remove from original
        del from_this_stack[-amount_of_boxes_to_move:]


# Get the puzzle answer
answer = ''
for stack in positions:
    answer = answer + stack[len(stack)-1]

print(answer)