import re


def calculate_line(line, is_part2=False):
    groups = re.findall('\\(([^()]*)\\)', line)
    while len(groups) > 0:
        for group in groups:
            result = calculate(0, group, is_part2)
            line = line.replace('(' + group + ')', str(result), 1)
        groups = re.findall('\\(([^()]*)\\)', line)
    return calculate(0, line, is_part2)


def calculate(start_index=0, expression='', is_part2=True):
    if is_part2:
        match = re.search('(\\d+ \\+ \\d+)', expression)
        while match:
            group = match.groups()[0]
            expression = expression.replace(group, str(eval(group)), 1)
            match = re.search('(\\d+ \\+ \\d+)', expression)
        return eval(expression)
    else:
        expression_split = expression.split(' ')
    result = int(expression_split[start_index])
    i = start_index
    while i < len(expression_split) - 1:
        result = eval(str(result) + expression_split[i + 1] + expression_split[i + 2])
        i += 2
    return result


part_1 = []
part_2 = []

with open('input/input18.txt') as f:
    read_data = f.read()
    lines = read_data.split('\n')

    for line in lines:
        result_1 = calculate_line(line, False)
        result_2 = calculate_line(line, True)
        part_1.append(result_1)
        part_2.append(result_2)

    print(sum(part_1))
    print(sum(part_2))
