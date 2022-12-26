import re


# FILENAME = "aoc22-0.txt"
FILENAME = "aoc22-1.txt"


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

def rotate(direction: tuple, rotation: int) -> tuple:
    if not rotation:
        return direction
    (y, x) = direction
    return (x * rotation, y * (-rotation))

def normalize_position(grid: list, position: tuple, direction: tuple) -> tuple:
    (y, x) = position
    while True:
        y = y % len(grid)
        x = x % len(grid[y])
        if grid[y][x] is not None:
            return (y, x)
        (y, x) = add((y, x), direction)

def move(grid: list, position: tuple, direction: tuple, distance: int) -> tuple:
    position = normalize_position(grid, position, direction)
    while distance:
        new_posit = normalize_position(grid, add(position, direction), direction)
        (b, a) = new_posit
        if grid[b][a]:
            break
        position = new_posit
        distance -= 1
    return position

def move_and_rotate(grid: list, position: tuple, direction: tuple, distance: int, rotation: int) -> tuple:
    position = move(grid, position, direction, distance)
    direction = rotate(direction, rotation)
    return (position, direction)

def calc_result(position: tuple, direction: tuple):
    (y, x) = position
    return (y + 1, x + 1, ((0, 1), (1, 0), (0, -1), (-1, 0)).index(direction))

def main():
    (grid, instructions) = parse_input(FILENAME)
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
