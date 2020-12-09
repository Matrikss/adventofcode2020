from day1 import sum_search

WINDOW_SIZE = 25

with open('input9.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    line_count = len(lines)
    i = WINDOW_SIZE
    while i < line_count:
        result = sum_search(lines[i - WINDOW_SIZE:i], lines[i])
        if not result:
            print(lines[i])
            break
        i += 1
