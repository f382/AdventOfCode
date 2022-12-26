import math
import re
from collections import defaultdict


# FILENAME = "aoc22-0.txt"
# NET = lambda: net_0
FILENAME = "aoc22-1.txt"
NET = lambda: net_1

DELTAS = (-1, 0, 1)
edge_size = None


def net_0(face: tuple, direction: tuple) -> tuple:
    match face:
        case (0, 2):
            match direction:
                case (1, 0):
                    return ((1, 2), 0)
                case (-1, 0):
                    return ((1, 0), 2)
                case (0, 1):
                    return ((2, 3), 2)
                case (0, -1):
                    return ((1, 1), -1)
        case (1, 0):
            match direction:
                case (1, 0):
                    return ((2, 2), 2)
                case (-1, 0):
                    return ((0, 2), 2)
                case (0, 1):
                    return ((1, 1), 0)
                case (0, -1):
                    return ((2, 3), 1)
        case (1, 1):
            match direction:
                case (1, 0):
                    return ((2, 2), -1)
                case (-1, 0):
                    return ((0, 2), 1)
                case (0, 1):
                    return ((1, 2), 0)
                case (0, -1):
                    return ((1, 0), 0)
        case (1, 2):
            match direction:
                case (1, 0):
                    return ((2, 2), 0)
                case (-1, 0):
                    return ((0, 2), 0)
                case (0, 1):
                    return ((2, 3), 1)
                case (0, -1):
                    return ((1, 1), 0)
        case (2, 2):
            match direction:
                case (1, 0):
                    return ((1, 0), 2)
                case (-1, 0):
                    return ((1, 2), 0)
                case (0, 1):
                    return ((2, 3), 0)
                case (0, -1):
                    return ((1, 1), 1)
        case (2, 3):
            match direction:
                case (1, 0):
                    return ((1, 0), -1)
                case (-1, 0):
                    return ((1, 2), -1)
                case (0, 1):
                    return ((0, 2), 2)
                case (0, -1):
                    return ((2, 2), 0)
    raise ValueError(f'No transition from {face=} to {direction=}')

def net_1(face: tuple, direction: tuple) -> tuple:
    match face:
        case (0, 1):
            match direction:
                case (1, 0):
                    return ((1, 1), 0)
                case (-1, 0):
                    return ((3, 0), 1)
                case (0, 1):
                    return ((0, 2), 0)
                case (0, -1):
                    return ((2, 0), 2)
        case (0, 2):
            match direction:
                case (1, 0):
                    return ((1, 1), 1)
                case (-1, 0):
                    return ((3, 0), 0)
                case (0, 1):
                    return ((2, 1), 2)
                case (0, -1):
                    return ((0, 1), 0)
        case (1, 1):
            match direction:
                case (1, 0):
                    return ((2, 1), 0)
                case (-1, 0):
                    return ((0, 1), 0)
                case (0, 1):
                    return ((0, 2), -1)
                case (0, -1):
                    return ((2, 0), -1)
        case (2, 0):
            match direction:
                case (1, 0):
                    return ((3, 0), 0)
                case (-1, 0):
                    return ((1, 1), 1)
                case (0, 1):
                    return ((2, 1), 0)
                case (0, -1):
                    return ((0, 1), 2)
        case (2, 1):
            match direction:
                case (1, 0):
                    return ((3, 0), 1)
                case (-1, 0):
                    return ((1, 1), 0)
                case (0, 1):
                    return ((0, 2), 2)
                case (0, -1):
                    return ((2, 0), 0)
        case (3, 0):
            match direction:
                case (1, 0):
                    return ((0, 2), 0)
                case (-1, 0):
                    return ((2, 0), 0)
                case (0, 1):
                    return ((2, 1), -1)
                case (0, -1):
                    return ((0, 1), -1)
    raise ValueError(f'No transition from {face=} to {direction=}')

def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    (grid, instructions) = content.split('\n\n')
    grid = grid.split('\n')
    instructions = re.findall(r'(\d+)(\D+)?+', instructions.strip())
    grid = [[ch == '#' if not ch.isspace() else None for ch in line] for line in grid]
    instructions = [(int(dist), (1 if rot == 'R' else -1) if rot else 0) for (dist, rot) in instructions]
    return (grid, instructions)

def widen(grid: list):
    width = max(len(line) for line in grid)
    for line in grid:
        while len(line) < width:
            line.append(None)

def add(*args: tuple) -> tuple:
    return tuple(sum(t) for t in zip(*args))

def negative(direction: tuple) -> tuple:
    return tuple(-u for u in direction)

def calc_edge_size(grid: list) -> int:
    size = sum(1 for row in grid for value in row if value is not None)
    return round(math.sqrt(size / 6))

def rotate(direction: tuple, rotation: int, with_edge: int = 1) -> tuple:
    (y, x) = direction
    n = with_edge - 1
    match rotation % 4:
        case 1:
            return (  x, n-y)
        case 2:
            return (n-y, n-x)
        case 3:
            return (n-x,   y)
    return direction

def normalize_position(grid: list, position: tuple, direction: tuple) -> tuple:
    (y, x) = position
    while True:
        y = y % len(grid)
        x = x % len(grid[y])
        if grid[y][x] is not None:
            return (y, x)
        (y, x) = add((y, x), direction)

def step(position: tuple, direction: tuple) -> tuple:
    (y, x) = position
    (k, j) = (y // edge_size, x // edge_size)
    (new_y, new_x) = add(position, direction)
    (new_k, new_y) = divmod(new_y, edge_size)
    (new_j, new_x) = divmod(new_x, edge_size)
    rotation = 0
    if (new_k, new_j) != (k, j):
        ((new_k, new_j), rotation) = NET()((k, j), direction)
    (new_y, new_x) = rotate((new_y, new_x), rotation, edge_size)
    (new_y, new_x) = (new_k * edge_size + new_y, new_j * edge_size + new_x)
    new_direct = rotate(direction, rotation)
    return ((new_y, new_x), new_direct)

def move(grid: list, position: tuple, direction: tuple, distance: int) -> tuple:
    position = normalize_position(grid, position, direction)
    while distance:
        (new_posit, new_direct) = step(position, direction)
        (b, a) = new_posit
        if grid[b][a]:
            break
        position = new_posit
        direction = new_direct
        distance -= 1
    return (position, direction)

def move_and_rotate(grid: list, position: tuple, direction: tuple, distance: int, rotation: int) -> tuple:
    (position, direction) = move(grid, position, direction, distance)
    direction = rotate(direction, rotation)
    return (position, direction)

def calc_result(position: tuple, direction: tuple):
    (y, x) = position
    return (y + 1, x + 1, ((0, 1), (1, 0), (0, -1), (-1, 0)).index(direction))

def test_rotate():
    rotated = point = (3, 2)
    for i in range(5):
        assert rotate(point, i) == rotated
        assert rotate(rotated, 4 - i) == point
        rotated = rotate(rotated, 1)

def test_net(f):
    departures = defaultdict(set)
    arrivals = defaultdict(set)
    depart_dir = defaultdict(set)
    arriv_dir = defaultdict(set)
    for k in range(0, 5):
        for j in range(0, 5):
            for dk in DELTAS:
                for dj in DELTAS:
                    try:
                        ((new_k, new_j), rotation) = f((k, j), (dk, dj))
                    except ValueError:
                        continue
                    new_direct = rotate((dk, dj), rotation)
                    departures[(k, j)].add((new_k, new_j))
                    arrivals[(new_k, new_j)].add((k, j))
                    depart_dir[(k, j)].add((dk, dj))
                    arriv_dir[(new_k, new_j)].add(new_direct)
                    ((k_again, j_again), rot_back) = f((new_k, new_j), negative(new_direct))
                    assert (k_again, j_again) == (k, j)
                    assert (rotation + rot_back) % 4 == 0
    def check_is_cube(collect: dict) -> bool:
        assert len(collect) == 6
        for edge_trans in collect.values():
            assert len(edge_trans) == 4
    check_is_cube(departures)
    check_is_cube(arrivals)
    check_is_cube(depart_dir)
    check_is_cube(arriv_dir)

def test():
    test_rotate()
    test_net(net_0)
    test_net(net_1)

def main():
    test()
    (grid, instructions) = parse_input(FILENAME)
    global edge_size
    edge_size = calc_edge_size(grid)
    widen(grid)
    for line in grid:
        print(''.join(('#' if ch else '.') if ch is not None else '|' for ch in line))
    print(instructions)
    position = (0, 0)
    direction = (0, 1)
    for (distance, rotation) in instructions:
        (position, direction) = move_and_rotate(grid, position, direction, distance, rotation)
        print(position, direction)
    (row, col, fac) = calc_result(position, direction)
    print(row, col, fac, row * 1000 + col * 4 + fac)


if __name__ == '__main__':
    main()
