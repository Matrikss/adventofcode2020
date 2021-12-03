def get_initial_state():
    result = {}

    with open('input/input17.txt') as f:
        read_data = f.read()
        lines = read_data.split('\n')

        y = len(lines) - 1
        for line in lines:
            xs = list(line)
            activeX = [ind for ind, x in enumerate(xs) if x == '#']
            for x in activeX:
                result[(x, y, 0, 0)] = 1
            y -= 1

    return result


def update_min_max(this, min, max):
    mx = min[0]
    my = min[1]
    mz = min[2]
    mw = min[3]
    Mx = max[0]
    My = max[1]
    Mz = max[2]
    Mw = max[3]
    if mx > this[0]:
        mx = this[0]
    if my > this[1]:
        my = this[1]
    if mz > this[2]:
        mz = this[2]
    if mw > this[3]:
        mw = this[3]
    if Mx < this[0]:
        Mx = this[0]
    if My < this[1]:
        My = this[1]
    if Mz < this[2]:
        Mz = this[2]
    if Mw < this[3]:
        Mw = this[3]
    return (mx, my, mz, mw), (Mx, My, Mz, Mw)


initial_active_state = get_initial_state()

next_active_state = {}

cycle = 0
while cycle < 6:
    # actives
    active_min = (0, 0, 0, 0)
    active_max = (0, 0, 0, 0)
    for x, y, z, w in initial_active_state.keys():
        active_around = 0
        active_min, active_max = update_min_max((x, y, z, w), active_min, active_max)
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    for l in range(w - 1, w + 2):
                        if i == x and j == y and k == z and l == w:
                            continue
                        if (i, j, k, l) in initial_active_state:
                            active_around += 1
        if active_around == 2 or active_around == 3:
            next_active_state[(x, y, z, w)] = 1

    # inactives
    for x in range(active_min[0] - 2, active_max[0] + 3):
        for y in range(active_min[1] - 2, active_max[1] + 3):
            for z in range(active_min[2] - 2, active_max[2] + 3):
                for w in range(active_min[3] - 2, active_max[3] + 3):
                    if (x, y, z, w) in initial_active_state:
                        continue
                    active_around = 0
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            for k in range(z - 1, z + 2):
                                for l in range(w - 1, w + 2):
                                    if i == x and j == y and k == z and l == w:
                                        continue
                                    if (i, j, k, l) in initial_active_state:
                                        active_around += 1
                    if active_around == 3:
                        next_active_state[(x, y, z, w)] = 1
    initial_active_state = next_active_state
    next_active_state = {}
    cycle += 1

print(252)  # just remove the 4th coordinate, or check the git history :P
print(len(initial_active_state))
