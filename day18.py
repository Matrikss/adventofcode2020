import re


def calculate(start_index=0, expression=['']):
    result = int(expression[start_index])
    i = start_index
    while i < len(expression) - 1:
        result = eval(str(result) + expression[i + 1] + expression[i + 2])
        i += 2
    return result


part_1 = []

with open('input18.txt') as f:
    read_data = f.read()
    lines = read_data.split('\n')

    for line in lines:
        groups = re.findall('\\(([^()]*)\\)', line)
        while len(groups) > 0:
            for group in groups:
                result = calculate(0, group.split(' '))
                line = line.replace('(' + group + ')', str(result))
            groups = re.findall('\\(([^()]*)\\)', line)

        expression = line.split(' ')
        result = calculate(0, expression)
        part_1.append(result)

    print(sum(part_1))
