def is_value_in_any_range(rules={}, value=0):
    for rule in rules.values():
        if value in range(rule[0], rule[1] + 1) or value in range(rule[2], rule[3] + 1):
            return True
    return False


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

    my_ticket = lines[separator1 + 2]
    # print(my_ticket)

    invalid_values = []

    i = separator1 + 5
    while i < line_count:
        # others
        ticket_values = lines[i].split(',')
        for ticket_value in ticket_values:
            if not is_value_in_any_range(rules, int(ticket_value)):
                invalid_values.append(int(ticket_value))
        i += 1

    print(sum(invalid_values))
