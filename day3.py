with open('input/input3.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    trees_a = 0
    trees_b = 0
    trees_c = 0
    trees_d = 0
    trees_e = 0
    pos_a = 0
    pos_b = 0
    pos_c = 0
    pos_d = 0
    mapsize = len(lines[0])

    for line in lines:
        if line[pos_a] == '#':
            trees_a += 1
        if line[pos_b] == '#':
            trees_b += 1
        if line[pos_c] == '#':
            trees_c += 1
        if line[pos_d] == '#':
            trees_d += 1
        pos_a = divmod(pos_a + 1, mapsize)[1]
        pos_b = divmod(pos_b + 3, mapsize)[1]
        pos_c = divmod(pos_c + 5, mapsize)[1]
        pos_d = divmod(pos_d + 7, mapsize)[1]

    pos_a = 0
    line_count = 0
    for line in lines:
        if line[pos_a] == '#' and (line_count % 2) == 0:
            trees_e += 1
        if (line_count % 2) == 0:
            pos_a = divmod(pos_a + 1, mapsize)[1]
        line_count += 1

    print(trees_a)
    print(trees_b)
    print(trees_c)
    print(trees_d)
    print(trees_e)

    print(trees_a * trees_b * trees_c * trees_d * trees_e)
