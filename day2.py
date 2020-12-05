with open('input2.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    valid_passwords = 0

    for line in lines:
        sections = line.split(' ')
        letter = sections[1].split(':')[0]
        occurrences = sections[2].count(letter)
        interval = sections[0].split('-')
        r = range(int(interval[0]), int(interval[1])+1)
        if occurrences in r:
            valid_passwords += 1

    print(valid_passwords)

    valid_passwords = 0
    for line in lines:
        sections = line.split(' ')
        letter = sections[1].split(':')[0]
        interval = sections[0].split('-')
        if (sections[2][int(interval[0])-1]==letter) != (sections[2][int(interval[1])-1]==letter):
            valid_passwords += 1

    print(valid_passwords)