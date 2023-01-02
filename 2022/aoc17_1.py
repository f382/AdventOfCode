import numpy
from collections import defaultdict

# FILENAME = "aoc17-0.txt"
FILENAME = "aoc17-1.txt"
# COUNT = 2022
COUNT = 1000000000000

BLOCKS = (((1, 1, 1, 1),),
          ((0, 1, 0), (1, 1, 1), (0, 1, 0)),
          ((0, 0, 1), (0, 0, 1), (1, 1, 1)),
          ((1,), (1,), (1,), (1,)),
          ((1, 1), (1, 1)))
WIDENESS = 7
INNER_X = 2
DIST_Y = 3

WIDTH = WIDENESS + 2
DIST_X = INNER_X + 1
MAXSIZE = 4
SIZE_INCREMENT = 100_000
(FREE, MOVING, FIXED) = (0, 1, 2)


def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="utf-8") as file:
        return tuple(1 if ch == '>' else -1 if ch == '<' else None for ch in file.read().strip())

def shift(grid: numpy.ndarray, top: int, direction: int, check_only: bool = False) -> bool:
    if not check_only:
        if not shift(grid, top, direction, True):
            return False
    if direction > 0:
        x_range = range(WIDTH - 1, 0, -1)
    elif direction < 0:
        x_range = range(0, WIDTH - 1, 1)
    for x in x_range:
        for y in range(top, top - MAXSIZE, -1):
            value = grid[y, x - direction]
            if grid[y, x] == FIXED:
                if value == MOVING:
                    return False
                continue
            if check_only:
                continue
            grid[y, x] = MOVING if value == MOVING else FREE
    return True

def fall(grid: numpy.ndarray, top: int, check_only: bool = False) -> bool:
    if not check_only:
        if not fall(grid, top, True):
            return False
    for y in range(top - MAXSIZE, top + 1):
        for x in range(1, WIDTH):
            value = grid[y + 1, x]
            if grid[y, x] == FIXED:
                if value == MOVING:
                    return False
                continue
            if check_only:
                continue
            grid[y, x] = MOVING if value == MOVING else FREE
    return True

def fixate(grid: numpy.ndarray, top: int):
    for y in range(top, top - MAXSIZE, -1):
        for x in range(1, WIDTH):
            if grid[y, x] == MOVING:
                grid[y, x] = FIXED

def find_height(grid: numpy.ndarray, height: int) -> int:
    while True:
        top = height - 1
        if any(grid[top, 1:-1]):
            return height
        height = top

def enlarge_grid(grid: numpy.ndarray, min_height: int):
    old_height = len(grid)
    if min_height <= old_height:
        return
    min_height = ((min_height - 1) // SIZE_INCREMENT + 1) * SIZE_INCREMENT
    grid.resize((min_height, WIDTH), refcheck = False)
    grid[old_height:min_height, -1].fill(FIXED)
    grid[old_height:min_height, 0].fill(FIXED)

def place_block(grid: numpy.ndarray, height: int, block: tuple) -> int:
    height += DIST_Y + len(block)
    enlarge_grid(grid, height)
    for (y, stripe) in enumerate(block):
        for (x, value) in enumerate(stripe):
            grid[height - y - 1, DIST_X + x] = value
    return height

def get_skyline(grid: numpy.ndarray, height: int) -> tuple:
    state = [FREE] * WIDTH
    for y in range(0, height):
        row = grid[height - y - 1]
        state = [max(*t) for t in zip(row, state)]
        if min(state) == FIXED:
            return tuple(map(tuple, grid[height - y : height]))

def loop(grid: numpy.ndarray, wind: tuple, target: int) -> int:
    states = defaultdict(list)
    extra_height = 0
    height = len(grid)
    total = 0
    step = 0
    active = False
    while True:
        height = find_height(grid, height)
        if total == target:
            print_grid(grid[height - MAXSIZE : height])
            print(total, extra_height, height)
            return extra_height + height
        current = total % len(BLOCKS)
        if step == 0:
            state = get_skyline(grid, height)
            history = states[state]
            history.append((total, current, height))
            print_grid(grid[height - MAXSIZE : height])
            print(history)
            for reuse in history[:-1]:
                if reuse[1] != current:
                    continue
                delta = total - reuse[0]
                skip = (target - total) // delta
                total += delta * skip
                extra_height += (height - reuse[2]) * skip
                break
        if not active:
            height = place_block(grid, height, BLOCKS[current])
            y = height
            active = True
        y -= 1
        shift(grid, y, wind[step])
        if not fall(grid, y):
            fixate(grid, y)
            active = False
            total += 1
        step = (step + 1) % len(wind)

def print_grid(grid: numpy.ndarray, title: str = ''):
    if title:
        print(title)
    noskip = False
    for row in grid:
        noskip = noskip or any(row[1:-1])
        if noskip:
            print(''.join('#' if part == FIXED else '@' if part == MOVING else '.' for part in row))

def main():
    for block in BLOCKS:
        for row in block:
            print(''.join('#' if part else '.' for part in row))
        print()
    wind = parse_input(FILENAME)
    print(wind)
    grid = numpy.full((MAXSIZE, WIDTH), FIXED, numpy.byte)
    height = loop(grid, wind, COUNT)
    print(height - MAXSIZE)

if __name__ == '__main__':
    main()
