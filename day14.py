import itertools

MASK = 'mask'
MASK_SIZE = 36
MASK_IGNORE = 'X'


def get_binary(int_value):
    bin_value = bin(int_value).replace('0b', '')
    return list(bin_value.rjust(MASK_SIZE, '0'))


with open('input/input14.txt') as f:
    read_data = f.read()

    memory_a = {}
    memory_b = {}
    mask_a = {}
    mask_b_x = []
    mask_b_1 = []

    lines = read_data.split('\n')
    for line in lines:

        split_line = line.replace(' ', '').split('=')
        if split_line[0] == MASK:
            mask_a = {}
            mask_b_x = []
            mask_b_1 = []
            mask_list = list(split_line[1])
            i = 0
            while i < MASK_SIZE:
                if mask_list[i] == MASK_IGNORE:
                    mask_b_x.append(i)
                if mask_list[i] == '1':
                    mask_b_1.append(i)
                    mask_a[i] = mask_list[i]
                if mask_list[i] == '2':
                    mask_a[i] = mask_list[i]
                i += 1
        else:
            instruction_value = int(split_line[1])
            memory_location = int(split_line[0].split('[')[1].split(']')[0])

            binary_value = get_binary(instruction_value)
            binary_location = get_binary(memory_location)

            for key in mask_a:
                binary_value[key] = mask_a[key]
            value = int(''.join(binary_value), 2)

            memory_a[memory_location] = value

            for i in mask_b_1:
                binary_location[i] = '1'

            num_of_x = len(mask_b_x)
            for i in itertools.product('01', repeat=num_of_x):
                j = 0
                while j < num_of_x:
                    binary_location[mask_b_x[j]] = i[j]
                    j += 1

                value = int(''.join(binary_location), 2)
                memory_b[value] = instruction_value

    print(sum(memory_a.values()))
    print(sum(memory_b.values()))
