import copy
import functools
import itertools
import math

EDGE_LENGTH = 10


class Tile:
    id = 0
    top = ''
    bottom = ''
    left = 0
    right = 0
    links = 0

    def __init__(self, line_list=['']):
        self.id = int(line_list[0].replace('Tile ', '').replace(':', ''))
        self.top = line_list[1]
        self.bottom = line_list[EDGE_LENGTH]
        self.left = []
        self.right = []
        for i in range(1, EDGE_LENGTH + 1):
            self.left.append(line_list[i][0])
            self.right.append(line_list[i][EDGE_LENGTH - 1])
        self.left = ''.join(self.left)
        self.right = ''.join(self.right)
        self.links = set()
        self.is_valid()

    def is_valid(self):
        assert self.top[EDGE_LENGTH - 1] == self.right[0]
        assert self.right[EDGE_LENGTH - 1] == self.bottom[EDGE_LENGTH - 1]
        assert self.bottom[0] == self.left[EDGE_LENGTH - 1]
        assert self.left[0] == self.top[0]

    def flip_horizontally(self):
        new = copy.deepcopy(self)
        new.right = self.left
        new.left = self.right
        new.top = self.top[::-1]
        new.bottom = self.bottom[::-1]
        new.is_valid()
        return new

    def flip_vertically(self):
        new = copy.deepcopy(self)
        new.top = self.bottom
        new.bottom = self.top
        new.right = self.right[::-1]
        new.left = self.left[::-1]
        new.is_valid()
        return new

    def rotate_right(self):
        new = copy.deepcopy(self)
        new.top = self.left[::-1]
        new.right = self.top
        new.bottom = self.right[::-1]
        new.left = self.bottom
        new.is_valid()
        return new

    def rotate_left(self):
        new = copy.deepcopy(self)
        new.top = self.right
        new.right = self.bottom[::-1]
        new.bottom = self.left
        new.left = self.top[::-1]
        new.is_valid()
        return new

    def is_corner_tile(self):
        return len(self.links) == 2

    def is_internal_tile(self):
        return len(self.links) == 4

    def is_edge_tile(self):
        return len(self.links) == 3

    def get_edges(self):
        return {self.top, self.bottom, self.left, self.right}

    def check_link_with(self, other_tile):
        this = self.get_edges()
        this.update({x[::-1] for x in this})
        other = other_tile.get_edges()
        other.update({x[::-1] for x in other})
        matches = this.intersection(other)
        if len(matches) > 0:
            self.links.add(other_tile.id)
            other_tile.links.add(self.id)


def parse_tiles():
    tiles = []
    with open('input20.txt') as f:
        read_data = f.read()
        lines = read_data.split('\n')

        current_tile = []

        for line in lines:
            if line == '':
                tiles.append(Tile(current_tile))
                current_tile = []
                continue
            current_tile.append(line)
    return tiles


if __name__ == '__main__':
    tile_list = parse_tiles()
    for i, j in itertools.combinations(tile_list, 2):
        i.check_link_with(j)
    corners = [x.id for ind, x in enumerate(tile_list) if tile_list[ind].is_corner_tile()]
    interiors = [x.id for ind, x in enumerate(tile_list) if tile_list[ind].is_internal_tile()]
    edges = [x.id for ind, x in enumerate(tile_list) if tile_list[ind].is_edge_tile()]
    assert len(corners) == 4
    mosaic_sides = int(math.sqrt(len(tile_list)))
    assert len(interiors) == len(tile_list) - ((mosaic_sides - 2) * 4) - 4
    assert len(edges) == (mosaic_sides - 2) * 4
    print(functools.reduce(lambda x, y: x * y, corners))
