import re

RULES = 1
MESSAGES = 2
COMPLETE_RULE = re.compile('[a-z\\|\\(\\)\\s]+')


def construct_expression(raw_r={}):
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

    return leaf_rules['0'].replace(' ', '')


valid_part1 = 0
raw_rules = {}

with open('input19.txt') as f:
    read_data = f.read()
    lines = read_data.split('\n')

    mode = RULES
    for line in lines:
        if line == '':
            mode = MESSAGES
            compiled_expression = re.compile(construct_expression(raw_rules))
            continue
        if mode == RULES:
            line_split = line.split(':')
            raw_rules[line_split[0]] = line_split[1]
            continue
        if mode == MESSAGES:
            if compiled_expression.fullmatch(line):
                valid_part1 += 1

print(valid_part1)
