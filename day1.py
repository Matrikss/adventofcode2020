TARGET = 2020


def sum_search(numbers, target):
    numbers = sorted(numbers, key=int)
    start = 0
    end = len(numbers) - 1
    while True:
        if start >= end:
            return None
        sum = int(numbers[start]) + int(numbers[end])
        if sum == TARGET:
            return int(numbers[start]) * int(numbers[end])
        if sum < TARGET:
            start += 1
        else:
            end -= 1


with open('input1.txt') as f:
    read_data = f.read()

    numbers = read_data.split('\n')
    print(sum_search(numbers, TARGET))

    start = 0
    middle = 1
    end = len(numbers) - 1
    numbers = sorted(numbers, key=int)
    while True:
        sum = int(numbers[start]) + int(numbers[middle]) + int(numbers[end])
        if sum == TARGET:
            print(int(numbers[start]) * int(numbers[middle]) * int(numbers[end]))
            break
        if sum < TARGET:
            start += 1
        if sum > TARGET:
            end -= 1
        if start >= end:
            middle += 1
            start = 0
            end = len(numbers) - 1
