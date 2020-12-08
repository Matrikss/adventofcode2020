JMP = 'jmp'
NOP = 'nop'
ACC = 'acc'


def run_code(code):
    code_size = len(code)
    line_visits = [0 for _ in range(code_size)]
    acc = 0
    i = 0
    while i < code_size:
        line_visits[i] += 1
        if line_visits[i] > 1:
            return acc, i
        instruction = code[i].split(' ')
        if instruction[0] == NOP:
            i += 1
            continue
        if instruction[0] == ACC:
            acc += int(instruction[1])
            i += 1
            continue
        if instruction[0] == JMP:
            i += int(instruction[1])
    return acc, i


def find_nop_jmp(code):
    code_size = len(code)
    jmp_nop = []
    i = 0
    while i < code_size:
        instruction = code[i].split(' ')[0]
        if instruction == NOP or instruction == JMP:
            jmp_nop.append(i)
        i += 1
    return jmp_nop


def flip(line):
    if line.startswith(NOP):
        return line.replace(NOP, JMP)
    return line.replace(JMP, NOP)


with open('input8.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')
    answer_a = run_code(lines)[0]

    jmp_nop_map = find_nop_jmp(lines)

    program_length = len(lines)
    for j in jmp_nop_map:
        changed_code = lines.copy()
        changed_code[j] = flip(changed_code[j])

        result = run_code(changed_code)
        if result[1] == program_length:
            answer_b = result[0]
            break

    print(answer_a)
    print(answer_b)
