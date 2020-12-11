import itertools
import copy

EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'


def check_change(seat_map, position_i, position_j, size_i, size_j):
    count = {EMPTY: 0, FLOOR: 0, OCCUPIED: 0}

    for i in itertools.filterfalse(lambda x: x < 0 or x >= size_i, range(position_i - 1, position_i + 2)):
        for j in itertools.filterfalse(lambda x: x < 0 or x >= size_j, range(position_j - 1, position_j + 2)):
            if i == position_i and j == position_j:
                continue
            # print(i,j)
            count[seat_map[i][j]] += 1
    if seat_map[position_i][position_j] == EMPTY and count[OCCUPIED] == 0:
        return OCCUPIED
    if seat_map[position_i][position_j] == OCCUPIED and count[OCCUPIED] >= 4:
        return EMPTY
    return seat_map[position_i][position_j]


with open('input11.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    line_count = len(lines)
    row_count = len(lines[0])
    new_lines = {}
    i = 0
    while i < line_count:
        new_lines[i] = list(lines[i])
        i += 1

    count = {EMPTY: 0, FLOOR: 0, OCCUPIED: 0}

    lines = new_lines
    i = 0
    j = 0
    next_seating_status = copy.deepcopy(lines)
    changes = 0
    while True:
        if i >= line_count or j >= row_count:
            if changes == 0:
                break
            else:
                i = 0
                j = 0
                changes = 0
                lines = next_seating_status
                next_seating_status = copy.deepcopy(lines)
                count = {EMPTY: 0, FLOOR: 0, OCCUPIED: 0}

        change = check_change(lines, i, j, line_count, row_count)
        count[change] += 1
        if change != lines[i][j]:
            changes += 1
            next_seating_status[i][j] = change
        j += 1
        if j >= row_count:
            j = 0
            i += 1

    print(count[OCCUPIED])
