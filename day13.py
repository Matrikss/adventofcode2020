import math
import threading
import cProfile
from multiprocessing import Process

OUT_OF_SERVICE = '0'


def get_first_element(item):
    return item[0]


def match_found(dict, timestamp):
    for offset in dict.keys():
        remainder = (timestamp + offset) % dict[offset]
        if remainder > 0:
            return False
    return True


def print_progress():
    print(' Progress: ' + str(progress))
    threading.Timer(60, print_progress).start()


def solve(offsets, lowest_freq, start, iterator):
    i = start
    global progress
    progress = 0
    print_progress()

    while True:
        timestamp = lowest_freq * i
        progress = timestamp
        if match_found(offsets, timestamp):
            return timestamp
        i += iterator


def part2(start, iterator_offset, iterator=1):
    with open('input13.txt') as f:
        read_data = f.read()

        lines = read_data.split('\n')
        buses = lines[1].replace('x', '0').split(',')

        time = int(lines[0])
        divisions = {}

        for bus in buses:
            if bus == OUT_OF_SERVICE:
                continue
            divisions[math.modf(time / int(bus))] = int(bus)

        ordered = sorted(divisions.keys(), key=get_first_element, reverse=True)
        result = ((ordered[0][1] + 1) * divisions[ordered[0]] - time) * divisions[ordered[0]]

        print(result)

        offsets = {}
        size = len(buses)
        lowest_f = int(sorted(buses, key=int, reverse=True)[0])
        lowest_f_index = buses.index(str(lowest_f))

        j = 0
        while j < size:
            if buses[j] == OUT_OF_SERVICE or j == lowest_f_index:
                j += 1
                continue
            offset = j - lowest_f_index
            offsets[offset] = int(buses[j])
            j += 1

        result = solve(offsets, lowest_f, int(start / lowest_f) + iterator_offset, iterator)

        print(result - lowest_f_index)


if __name__ == '__main__':
    # part2(1, 0)
    # cProfile.run('part2(1, 0)')
    even = Process(target=part2, args=(100000000000000, 0, 2,))
    even.start()
    odd = Process(target=part2, args=(100000000000000, 1, 2,))
    odd.start()
