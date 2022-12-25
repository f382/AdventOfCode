from copy import deepcopy


# FILENAME = "aoc23-0.txt"
FILENAME = "aoc23-1.txt"

DELTAS = (-1, 0, +1)
DIRECTIONS = ((-1, 0), (+1, 0), (0, -1), (0, +1))


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [[ch == '#' for ch in line.strip()] for line in file.readlines() if line]

def add(*args: tuple) -> tuple:
    return tuple(sum(t) for t in zip(*args))

def rotate(stuff: list):
    stuff.append(stuff.pop(0))

def grow(grid: list):
    if any(grid[0]):
        grid.insert(0, [False for _ in grid[0]])
    if any(grid[-1]):
        grid.append([False for _ in grid[-1]])
    if any(row[0] for row in grid):
        for row in grid:
            row.insert(0, False)
    if any(row[-1] for row in grid):
        for row in grid:
            row.append(False)

def shrink(grid: list):
    while not any(grid[0]):
        grid.pop(0)
    while not any(grid[-1]):
        grid.pop()
    while not any(row[0] for row in grid):
        for row in grid:
            row.pop(0)
    while not any(row[-1] for row in grid):
        for row in grid:
            row.pop()

def is_clear(grid: list, point: tuple) -> bool:
    (y, x) = point
    return not any(grid[y + dy][x + dx]
                   for dy in DELTAS for dx in DELTAS
                   if dy or dx)

def want_move(grid: list, point: tuple, direction: tuple) -> bool:
    (y, x) = point
    (db, da) = direction
    return not any(grid[y + dy][x + dx]
                   for dy in DELTAS if not db or dy == db
                   for dx in DELTAS if not da or dx == da)

def propose(grid: list, directions: list) -> tuple:
    grow(grid)
    intent = [[None for elf in row] for row in grid]
    number = [[0 for elf in row] for row in grid]
    for (y, row) in enumerate(grid):
        for (x, elf) in enumerate(row):
            if not elf:
                continue
            point = (y, x)
            intent[y][x] = point
            if is_clear(grid, point):
                continue
            for direction in directions:
                if want_move(grid, point, direction):
                    target = add(point, direction)
                    intent[y][x] = target
                    (b, a) = target
                    number[b][a] += 1
                    break
    return (intent, number)

def move(grid: list, intent: list, number: list) -> list:
    has_moved = False
    new = deepcopy(grid)
    for (y, row) in enumerate(grid):
        for (x, elf) in enumerate(row):
            if not elf:
                continue
            point = (y, x)
            target = intent[y][x]
            if target == point:
                continue
            (b, a) = target
            if number[b][a] == 1:
                has_moved = True
                new[y][x] = False
                new[b][a] = True
    if not has_moved:
        new = grid
    shrink(new)
    return new

def iterate(grid: list, directions: list) -> list:
    (intent, number) = propose(grid, directions)
    new = move(grid, intent, number)
    rotate(directions)
    return new

def count_empty(grid: list) -> int:
    return sum(not elf for row in grid for elf in row)

def print_grid(grid: list, title: str = ''):
    print(title)
    for row in grid:
        print(''.join(['#' if p else '.' for p in row]))

def main():
    grid = None
    directions = list(DIRECTIONS)
    new = parse_input(FILENAME)
    i = 0
    print_grid(new)
    while new != grid:
        grid = new
        new = iterate(grid, directions)
        i += 1
        empty = count_empty(new)
        # print_grid(new, str(i))
        print(f'{i=}\t{empty=}')


if __name__ == '__main__':
    main()
