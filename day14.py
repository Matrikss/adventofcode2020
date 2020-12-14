MASK = 'mask'
MASK_SIZE = 36
MASK_IGNORE = 'X'

with open('input14.txt') as f:
    read_data = f.read()

    memory = {}
    mask = {}
    lines = read_data.split('\n')
    for line in lines:

        split_line = line.replace(' ', '').split('=')
        if split_line[0] == MASK:
            mask = {}
            mask_list = list(split_line[1])
            i = 0
            while i < MASK_SIZE:
                if mask_list[i] != MASK_IGNORE:
                    mask[i] = mask_list[i]
                i += 1
        else:
            binary_value = bin(int(split_line[1])).replace('0b', '')
            binary_value = list(binary_value.rjust(MASK_SIZE, '0'))

            for key in mask:
                binary_value[key] = mask[key]
            value = int(''.join(binary_value), 2)
            memory_location = int(split_line[0].split('[')[1].split(']')[0])
            memory[memory_location] = value

    print(sum(memory.values()))
