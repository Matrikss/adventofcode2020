def get_position(code):
    row = code[0:7].replace('F', '0').replace('B', '1')
    column = code[7:10].replace('R', '1').replace('L', '0')
    row_number = int(row, 2)
    column_number = int(column, 2)
    return row_number, column_number


with open('input/input5.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    highest_id = 0
    rows = [0 for _ in range(128)]
    for line in lines:
        row, column = get_position(line)
        rows[row] += 1
        id = row * 8 + column
        if id > highest_id:
            highest_id = id

    my_row = rows.index(7)
    columns = [0 for _ in range(8)]
    for line in lines:
        row, column = get_position(line)
        if row == my_row:
            columns[column] = row * 8 + column

    print(highest_id)
    print(columns)
