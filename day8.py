with open('input8.txt') as f:
    read_data = f.read()

    acc = 0

    lines = read_data.split('\n')
    line_visits = [0 for _ in range(len(lines))]
    i = 0
    while True:
        line_visits[i] += 1
        if line_visits[i] > 1:
            break
        instruction = lines[i].split(' ')
        if instruction[0] == 'nop':
            i += 1
            continue
        if instruction[0] == 'acc':
            acc += int(instruction[1])
            i += 1
            continue
        if instruction[0] == 'jmp':
            i += int(instruction[1])

    print(acc)
