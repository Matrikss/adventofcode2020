import re

RULES = 1
MESSAGES = 2
COMPLETE_RULE = re.compile('[a-z\\|\\(\\)\\s]+')


def construct_expression(raw_r={}, is_part_2=False):
    if is_part_2:
        magic_number = {'8': 3, '11': 2}
        raw_r['8'] = ' 42 | 42 8'
        raw_r['11'] = ' 42 31 | 42 11 31'
    else:
        magic_number = {}

    leaf_rules = {key: value.replace('"', '').rstrip().lstrip() for (key, value) in raw_r.items() if '"' in value}
    while len(leaf_rules.keys()) < len(raw_r.keys()):
        for key, value in raw_r.items():
            if key not in leaf_rules:
                replaced = value
                for rule_id, rule_value in leaf_rules.items():
                    if '|' in rule_value:
                        replaced = re.sub('\\b' + rule_id + '\\b', '(' + rule_value + ')', replaced)
                    else:
                        replaced = re.sub('\\b' + rule_id + '\\b', rule_value, replaced)
                if COMPLETE_RULE.fullmatch(replaced):
                    leaf_rules[key] = replaced
                if key in magic_number:
                    if COMPLETE_RULE.fullmatch(re.sub('\\b' + key + '\\b', '', replaced)):
                        if magic_number[key] == 1:
                            leaf_rules[key] = re.sub('\\b' + key + '\\b', '(' + re.sub('\\b' + key + '\\b', '', replaced) + ')', replaced)
                        else:
                            raw_r[key] = re.sub('\\b' + key + '\\b', '(' + replaced + ')', replaced)
                            magic_number[key] -= 1

    return leaf_rules['0'].replace(' ', '')


valid_part1 = 0
valid_part2 = 0
raw_rules = {}

with open('input/input19.txt') as f:
    read_data = f.read()
    lines = read_data.split('\n')

    mode = RULES
    for line in lines:
        if line == '':
            mode = MESSAGES
            compiled_expression1 = re.compile(construct_expression(raw_rules, False))
            compiled_expression2 = re.compile(construct_expression(raw_rules, True))
            continue
        if mode == RULES:
            line_split = line.split(':')
            raw_rules[line_split[0]] = line_split[1]
            continue
        if mode == MESSAGES:
            if compiled_expression1.fullmatch(line):
                valid_part1 += 1
            if compiled_expression2.fullmatch(line):
                valid_part2 += 1

print(valid_part1)
print(valid_part2)
