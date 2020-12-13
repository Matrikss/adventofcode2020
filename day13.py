import math

OUT_OF_SERVICE = 'x'


def get_first_element(item):
    return item[0]


with open('input13.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    buses = lines[1].split(',')

    time = int(lines[0])
    divisions = {}

    for bus in buses:
        if bus == OUT_OF_SERVICE:
            continue
        divisions[math.modf(time / int(bus))] = int(bus)

    ordered = sorted(divisions.keys(), key=get_first_element, reverse=True)
    result = ((ordered[0][1] + 1) * divisions[ordered[0]] - time) * divisions[ordered[0]]

    print(result)
