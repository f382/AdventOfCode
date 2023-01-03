import copy

# FILENAME = "aoc24-0.txt"
FILENAME = "aoc24-1.txt"

CHARACTERS = ('v'   , '^'    , '>'   , '<'    , '.')
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
NO_MOVE = CHARACTERS.index('.')


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        grid = [[[i == k for k in range(len(DIRECTIONS))] for i in row]
                for row in [[CHARACTERS.index(ch) for ch in line if ch in CHARACTERS]
                            for line in file.readlines()]
                if row != [NO_MOVE]]
    # print_grid(grid)
    return grid

def print_grid(grid: list, possibilites: list, title = ''):
    print(title)
    def state_symbol(state: list, value: int) -> str:
        n = sum(state)
        if n == 0:
            if value:
                return chr(ord('E') + value - 1)
            else:
                return CHARACTERS[NO_MOVE]
        if n > 1:
            return str(n)
        i = state.index(True)
        return CHARACTERS[i]
    for (row_g, row_p) in zip(grid, possibilites):
        print(''.join(state_symbol(state, value) for (state, value) in zip(row_g, row_p)))

def sub_m(p: tuple, q: tuple, moduli: tuple) -> tuple:
    return tuple((a - b) % m for (a, b, m) in zip(p, q, moduli))

def sub(p: tuple, q: tuple) -> tuple:
    return tuple(a - b for (a, b) in zip(p, q))

def shape(grid: list) -> tuple:
    return (len(grid), len(grid[0]))

def in_range(p: tuple, lengths: tuple) -> bool:
    return all(0 <= a < length for (a, length) in zip(p, lengths))

def iterated(f, *args):
    yield args
    yield from iterated(f, *f(*args))

def evolve(grid: list) -> list:
    lengths = shape(grid)
    new_g = copy.deepcopy(grid)
    for (y, row) in enumerate(new_g):
        for (x, state) in enumerate(row):
            for (k, d) in enumerate(DIRECTIONS):
                (v, u) = sub_m((y, x), d, moduli = lengths)
                state[k] = grid[v][u][k]
    return new_g

def find_possibilities(grid: list, possible: list, start: int, stop: int) -> list:
    lengths = shape(grid)
    new_p = copy.deepcopy(possible)
    for (y, row) in enumerate(new_p):
        for (x, value) in enumerate(row):
            row[x] = max(possible[y][x],
                         max(possible[v][u] for (v, u) in (sub((y, x), d)
                                                           for (k, d) in enumerate(DIRECTIONS))
                                            if in_range((v, u), lengths))
                        ) if not any(grid[y][x]) else 0
    if not any(grid[0][0]):
        new_p[0][0] = max(new_p[0][0], start)
    if not any(grid[-1][-1]):
        new_p[-1][-1] = max(new_p[-1][-1], stop)
    return new_p

def proceed(grid: list, possible: list, start: int, stop: int) -> tuple:
    new_g = evolve(grid)
    new_p = find_possibilities(new_g, possible, start, stop)
    return (new_g, new_p, max(start, (possible[0][0] & ~1) + 1), max(stop, (possible[-1][-1] + 1) & ~1))

def main():
    init_g = parse_input(FILENAME)
    init_p = [[0 for state in row] for row in init_g]
    iterations = iterated(proceed, init_g, init_p, 1, 0)
    (oldstart, oldstop) = (0, 0)
    for (step, (grid, possible, start, stop)) in enumerate(iterations):
        if start > oldstart or stop > oldstop:
            print_grid(grid, possible, f'{start=}, {stop=}, {step=}')
            (oldstart, oldstop) = (start, stop)
            if stop == 4:
                print(step)
                break

if __name__ == '__main__':
    main()
