def find_containers(bag_dict={}, bag=''):
    result = []
    if bag in bag_dict.keys():
        for b in bag_dict[bag]:
            result.append(b)
            result += find_containers(bag_dict, b)
    return result


with open('input7.txt') as f:
    read_data = f.read()

    bags = {}

    lines = read_data.split('\n')
    for line in lines:
        rule = line.split('contain')
        clean_container = rule[0].replace('bags', '').replace('bag', '').rstrip()
        contents = rule[1].split(',')
        for content in contents:
            split_content = content.replace('no other bags.', '').split(' ')
            if len(split_content) < 5:
                continue
            clean_content = split_content[2] + ' ' + split_content[3]
            if clean_content in bags.keys():
                bags[clean_content].append(clean_container)
            else:
                bags[clean_content] = [clean_container]

    answer_a = set(find_containers(bags, 'shiny gold'))

    print(len(answer_a))
