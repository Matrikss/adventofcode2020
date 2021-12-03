with open('input/input6.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')

    total_count_a = 0
    total_count_b = 0
    group_answers = {}
    group_people = 0
    for line in lines:
        if len(line) == 0:
            total_count_a += len(group_answers.keys())
            total_count_b += len([x for x in group_answers.keys() if group_answers[x] == group_people])
            group_answers = {}
            group_people = 0
            continue
        for letter in line:
            if letter in group_answers.keys():
                group_answers[letter] += 1
            else:
                group_answers[letter] = 1
        group_people += 1

    print(total_count_a)
    print(total_count_b)
