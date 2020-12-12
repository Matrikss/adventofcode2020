from numpy import array
from scipy.spatial.transform import Rotation as R

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

with open('input12.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')

    ship_position = array([0, 0, 0])
    ship_orientation = array([1, 0, 0])

    for line in lines:
        instruction = line[0]
        magnitude = int(line[1:])
        if instruction == NORTH:
            ship_position[1] += magnitude
        if instruction == SOUTH:
            ship_position[1] -= magnitude
        if instruction == EAST:
            ship_position[0] += magnitude
        if instruction == WEST:
            ship_position[0] -= magnitude
        if instruction == LEFT:
            r = R.from_euler('z', magnitude, degrees=True)
            ship_orientation = r.apply(ship_orientation).astype(int)
        if instruction == RIGHT:
            r = R.from_euler('z', magnitude, degrees=True).inv()
            ship_orientation = r.apply(ship_orientation).astype(int)
        if instruction == FORWARD:
            ship_position += ship_orientation * magnitude

    print(abs(ship_position[0]) + abs(ship_position[1]))
