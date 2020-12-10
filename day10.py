import cProfile


def add_rating(dict, rating):
    if rating in dict.keys():
        dict[rating] += 1
    else:
        dict[rating] = 1


def look_ahead(adapters, starting_position):
    i = starting_position
    j = i + 1
    target = int(adapters[i]) + 3
    current_seq = 0
    while j < len(adapters):
        next = int(adapters[j])
        if next == target:
            current_seq += 1
            return current_seq
        if next < target:
            current_seq += 1
            j += 1
            continue
        if next > target:
            return current_seq


def explore(adapters, starting_position, look_aheads, size):
    i = starting_position
    while i < size:
        next_in_range = look_aheads[i]
        if next_in_range == 2:
            return explore(adapters, i + 1, look_aheads, size) + explore(adapters, i + 2, look_aheads, size)
        if next_in_range == 3:
            return explore(adapters, i + 1, look_aheads, size) + explore(adapters, i + 2, look_aheads, size) + explore(adapters, i + 3, look_aheads, size)
        i += 1
    return 1


with open('input10.txt') as f:
    read_data = f.read()

    frequency = {}

    lines = sorted(read_data.split('\n'), key=int)
    lines = [0] + lines + [int(lines[len(lines) - 1]) + 3]
    i = 1
    while i < len(lines):
        rating_diff = int(lines[i]) - int(lines[i - 1])
        add_rating(frequency, rating_diff)
        i += 1

    answer_a = frequency[1] * frequency[3]

    look_aheads = [0 for _ in range(len(lines))]
    i = 0
    while i < len(lines):
        look_aheads[i] = look_ahead(lines, i)
        i += 1
    answer_b = explore(lines, 0, look_aheads, len(lines))
    # cProfile.run('explore(lines, 0, look_aheads, len(lines))')

    print(answer_a)
    print(answer_b)
