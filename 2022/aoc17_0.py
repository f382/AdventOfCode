# FILENAME = "aoc17-0.txt"
FILENAME = "aoc17-1.txt"

BLOCKS = (((1, 1, 1, 1),),
          ((0, 1, 0), (1, 1, 1), (0, 1, 0)),
          ((0, 0, 1), (0, 0, 1), (1, 1, 1)),
          ((1,), (1,), (1,), (1,)),
          ((1, 1), (1, 1)))
WIDENESS = 7
INNER_X = 2
DIST_Y = 3
COUNT = 2022

WIDTH = WIDENESS + 2
DIST_X = INNER_X + 1
MAXSIZE = 4
HEIGHT = MAXSIZE * (1 + COUNT) + DIST_Y + 1
(FREE, MOVING, FIXED) = (0, 1, 2)


def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="utf-8") as file:
        return tuple(1 if ch == '>' else -1 if ch == '<' else None for ch in file.read().strip())

def shift(grid: list, top: int, direction: int, check_only: bool = False) -> bool:
    if not check_only:
        if not shift(grid, top, direction, True):
            return False
    bound = WIDTH - 1 if direction > 0 else 0 if direction < 0 else None
    assert WIDTH - bound - 1 == (0 if direction > 0 else WIDTH - 1)
    for x in range(bound, WIDTH - bound - 1, -direction):
        for y in range(top, top + MAXSIZE):
            value = grid[y][x - direction]
            if grid[y][x] == FIXED:
                if value == MOVING:
                    return False
                continue
            if check_only:
                continue
            grid[y][x] = MOVING if value == MOVING else FREE
    return True

def fall(grid: list, top: int, check_only: bool = False) -> bool:
    if not check_only:
        if not fall(grid, top, True):
            return False
    for y in range(top + MAXSIZE, top - 1, -1):
        for x in range(0, WIDTH):
            value = grid[y - 1][x]
            if grid[y][x] == FIXED:
                if value == MOVING:
                    return False
                continue
            if check_only:
                continue
            grid[y][x] = MOVING if value == MOVING else FREE
    return True

def fixate(grid: list, top: int):
    for y in range(top, top + MAXSIZE):
        for x in range(0, WIDTH):
            if grid[y][x] == MOVING:
                grid[y][x] = FIXED

def find_top(grid: list, top: int) -> int:
    while True:
        if any(grid[top][1:-1]):
            return top
        top += 1

def drop(grid: list, height: int, block: tuple, wind: tuple, step: int) -> tuple:
    top = HEIGHT - height - DIST_Y - len(block)
    left = DIST_X
    for (y, stripe) in enumerate(block):
        for (x, value) in enumerate(stripe):
            grid[top + y][left + x] = value
    y = top
    while True:
        # print_grid(grid, f'{y=} {wind[step]=}')
        shift(grid, y, wind[step])
        step = (step + 1) % len(wind)
        if not fall(grid, y):
            fixate(grid, y)
            break
        y += 1
    top = find_top(grid, top)
    height = HEIGHT - top
    return (height, step)

def print_grid(grid: list, title: str = ''):
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
    grid = [[0] * WIDTH for y in range(HEIGHT)]
    for y in range(HEIGHT - MAXSIZE, HEIGHT):
        for x in range(WIDTH):
            grid[y][x] = FIXED
    for y in range(HEIGHT):
        for x in (0, -1):
            grid[y][x] = FIXED
    print_grid(grid, 'start')
    height = MAXSIZE
    current = 0
    step = 0
    for k in range(COUNT):
        (height, step) = drop(grid, height, BLOCKS[current], wind, step)
        current = (current + 1) % len(BLOCKS)
        # print_grid(grid, str(k + 1))
        print(k + 1, height - MAXSIZE)

if __name__ == '__main__':
    main()
