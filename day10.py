def add_rating(dict, rating):
    if rating in dict.keys():
        dict[rating] += 1
    else:
        dict[rating] = 1


with open('input10.txt') as f:
    read_data = f.read()

    frequency = {}

    lines = sorted(read_data.split('\n'), key=int)
    i = 1
    while i < len(lines):
        rating_diff = int(lines[i]) - int(lines[i - 1])
        add_rating(frequency, rating_diff)
        i += 1
    add_rating(frequency, int(lines[0]))
    add_rating(frequency, 3)

    answer_a = frequency[1] * frequency[3]

    print(answer_a)
