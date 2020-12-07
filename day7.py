def find_containers(bag_dict={}, bag=''):
    result = []
    if bag in bag_dict.keys():
        for b in bag_dict[bag]:
            result.append(b)
            result += find_containers(bag_dict, b)
    return result


def find_containers_b(bag_dict={}, bag=''):
    result = 0
    if bag in bag_dict.keys():
        for b in bag_dict[bag]:
            result += int(b[1]) + int(b[1]) * find_containers_b(bag_dict, b[0])
    return result


with open('input7.txt') as f:
    read_data = f.read()

    bags = {}
    bags_b = {}

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
            if clean_container in bags_b.keys():
                bags_b[clean_container].append([clean_content, split_content[1]])
            else:
                bags_b[clean_container] = [[clean_content, split_content[1]]]

    answer_a = set(find_containers(bags, 'shiny gold'))
    answer_b = find_containers_b(bags_b, 'shiny gold')

    print(len(answer_a))
    print(answer_b)
