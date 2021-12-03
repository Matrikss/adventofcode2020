import numpy
from scipy.spatial.transform import Rotation as R

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

with open('input/input12.txt') as f:
    read_data = f.read()

    lines = read_data.split('\n')

    ship_position_a = numpy.array([0, 0, 0])
    ship_orientation = numpy.array([1, 0, 0])

    ship_position_b = numpy.array([0.0, 0.0, 0.0])
    waypoint_position = numpy.array([10.0, 1.0, 0.0])

    for line in lines:
        instruction = line[0]
        magnitude = int(line[1:])
        if instruction == NORTH:
            ship_position_a[1] += magnitude
            waypoint_position[1] += magnitude
        if instruction == SOUTH:
            ship_position_a[1] -= magnitude
            waypoint_position[1] -= magnitude
        if instruction == EAST:
            ship_position_a[0] += magnitude
            waypoint_position[0] += magnitude
        if instruction == WEST:
            ship_position_a[0] -= magnitude
            waypoint_position[0] -= magnitude
        if instruction == LEFT:
            r = R.from_euler('z', magnitude, degrees=True)
            ship_orientation = r.apply(ship_orientation).astype(int)
            waypoint_position = r.apply(waypoint_position)
        if instruction == RIGHT:
            r = R.from_euler('z', magnitude, degrees=True).inv()
            ship_orientation = r.apply(ship_orientation).astype(int)
            waypoint_position = r.apply(waypoint_position)
        if instruction == FORWARD:
            ship_position_a += ship_orientation * magnitude
            ship_position_b += waypoint_position * magnitude

    print(abs(ship_position_a[0]) + abs(ship_position_a[1]))
    print(abs(ship_position_b[0]) + abs(ship_position_b[1]))
