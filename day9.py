from day1 import sum_search

WINDOW_SIZE = 25

with open('input/input9.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    line_count = len(lines)
    value_a = None
    i = WINDOW_SIZE
    while i < line_count:
        result = sum_search(lines[i - WINDOW_SIZE:i], lines[i])
        if not result:
            value_a = int(lines[i])
            break
        i += 1

    print(value_a)

    i = 0
    j = 1
    sum = int(lines[i])
    while True:
        sum += int(lines[j])
        if sum == value_a:
            numbers = sorted(lines[i:j + 1], key=int)
            print(int(numbers[0]) + int(numbers[len(numbers) - 1]))
            break
        if sum > value_a:
            i += 1
            j = i + 1
            sum = int(lines[i])
            continue
        j += 1
