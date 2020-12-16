import functools


def is_value_in_a_range(value, rule_range=[]):
    return value in range(rule_range[0], rule_range[1] + 1) or value in range(rule_range[2], rule_range[3] + 1)


def is_value_in_any_range(rules={}, value=0):
    for rule in rules.values():
        if is_value_in_a_range(value, rule):
            return True
    return False


def rules_valid_for_value(value=0, rules={}):
    result = []

    for rule_key in rules.keys():
        if is_value_in_a_range(value, rules[rule_key]):
            result.append(rule_key)
    return result


with open('input16.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    line_count = len(lines)
    separator1 = lines.index('')
    rules = {}

    i = 0
    while i < separator1:
        # rules
        rule_split = lines[i].split(':')
        interval_split = rule_split[1].split(' ')
        rules[rule_split[0]] = [int(interval_split[1].split('-')[0]), int(interval_split[1].split('-')[1]), int(interval_split[3].split('-')[0]), int(interval_split[3].split('-')[1])]
        # print(lines[i])
        i += 1

    my_ticket = lines[separator1 + 2].split(',')
    # print(my_ticket)

    invalid_values = []
    invalid_tickets = []

    i = separator1 + 5
    while i < line_count:
        # find invalid tickets
        ticket_values = lines[i].split(',')
        for ticket_value in ticket_values:
            if not is_value_in_any_range(rules, int(ticket_value)):
                invalid_values.append(int(ticket_value))
                invalid_tickets.append(i)
        i += 1

    sudoku = {}
    others_start = separator1 + 5
    columns = len(rules.keys())
    i = others_start
    j = 0
    possible_fields = []
    while j < columns:
        # find fields
        if i == line_count:
            sudoku[j] = possible_fields
            j += 1
            i = others_start
            continue
        if i in invalid_tickets:
            i += 1
            continue
        ticket_values = lines[i].split(',')
        if i == others_start:
            possible_fields = rules_valid_for_value(int(ticket_values[j]), rules)
            i += 1
            continue
        possible_fields = set(rules_valid_for_value(int(ticket_values[j]), rules)).intersection(possible_fields)
        i += 1

    fields = [None for _ in range(columns)]
    while True:
        unique = [x for x in sudoku if len(sudoku[x]) == 1]
        if len(unique) == 0:
            break
        unique = unique[0]
        fields[unique] = sudoku[unique].pop()
        for sets in sudoku.values():
            if fields[unique] in sets:
                sets.remove(fields[unique])

    departure_fields = [ind for ind, x in enumerate(fields) if x.startswith('departure')]
    relevant_fields = [int(x) for ind, x in enumerate(my_ticket) if ind in departure_fields]

    print(sum(invalid_values))
    print(functools.reduce(lambda x, y: x * y, relevant_fields))
