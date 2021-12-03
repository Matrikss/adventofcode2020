DAY1_TARGET = 2020


def sum_search(numbers, target):
    numbers = sorted(numbers, key=int)
    target = int(target)
    start = 0
    end = len(numbers) - 1
    while True:
        if start >= end:
            return None
        sum = int(numbers[start]) + int(numbers[end])
        if sum == target:
            return int(numbers[start]) * int(numbers[end])
        if sum < target:
            start += 1
        else:
            end -= 1


with open('input/input1.txt') as f:
    read_data = f.read()

    numbers = read_data.split('\n')
    print(sum_search(numbers, DAY1_TARGET))

    start = 0
    middle = 1
    end = len(numbers) - 1
    numbers = sorted(numbers, key=int)
    while True:
        sum = int(numbers[start]) + int(numbers[middle]) + int(numbers[end])
        if sum == DAY1_TARGET:
            print(int(numbers[start]) * int(numbers[middle]) * int(numbers[end]))
            break
        if sum < DAY1_TARGET:
            start += 1
        if sum > DAY1_TARGET:
            end -= 1
        if start >= end:
            middle += 1
            start = 0
            end = len(numbers) - 1
