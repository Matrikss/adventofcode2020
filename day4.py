import re


def validate(passport):
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if 1920 > int(passport['byr']) or int(passport['byr']) > 2002:
        return False
    if 2010 > int(passport['iyr']) or int(passport['iyr']) > 2020:
        return False
    if 2020 > int(passport['eyr']) or int(passport['eyr']) > 2030:
        return False
    if re.search('^1\d\dcm|^[5-7]\din', passport['hgt']) is None:
        return False
    if re.search('^#[0-9a-f]{6}$', passport['hcl']) is None:
        return False
    if passport['ecl'] not in eye_colors:
        return False
    if re.search('^\d{9}$', passport['pid']) is None:
        return False
    return True


with open('input4.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    mandatory = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    valid_passports_a = 0
    valid_passports_b = 0
    passport = {}
    for line in lines:
        if len(line) == 0:
            if mandatory.issubset(passport.keys()):
                valid_passports_a += 1
                if validate(passport):
                    valid_passports_b += 1
            passport = {}
            continue
        fields = line.split(' ')
        for field in fields:
            key_value = field.split(':')
            passport[key_value[0]] = key_value[1]

    print(valid_passports_a)
    print(valid_passports_b)
