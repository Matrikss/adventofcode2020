TARGET = 2020

input = [12, 1, 16, 3, 11, 0]
input_size = len(input)
visits = {}

previous_turn_number = 0
turn = 1
for i in input:
    visits[i] = turn
    previous_turn_number = i
    turn += 1

while turn <= TARGET:
    if previous_turn_number in visits:
        if turn == input_size + 1:
            # especial after start
            previous_turn_number = 0
            # print(str(turn) + ':' + str(previous_turn_number))
            turn += 1
            continue
        # seen before
        prev_prev = previous_turn_number
        previous_turn_number = (turn - 1) - visits[previous_turn_number]
        visits[prev_prev] = turn - 1
    else:
        # new
        visits[previous_turn_number] = turn - 1
        previous_turn_number = 0
    # print(str(turn) + ':' + str(previous_turn_number))
    turn += 1

print(previous_turn_number)
