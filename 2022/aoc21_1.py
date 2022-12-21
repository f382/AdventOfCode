import re


# FILENAME = "aoc21-0.txt"
FILENAME = "aoc21-1.txt"

ROOT = 'root'
HUMN = 'humn'


FUNCS = {'=': lambda x, y: x == y,
         '+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
         '/': lambda x, y: x // y}

INVRS = {'=': lambda v, x, dir: x,
         '+': lambda v, x, dir: v - x,
         '-': lambda v, x, dir: x - v if dir else v + x,
         '*': lambda v, x, dir: v // x,
         '/': lambda v, x, dir: x // v if dir else v * x}


def parse_input(filename: str) -> dict:
    monkeys = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if match := re.match(r'^(\w+):\s*(\w+)\s*(\S)?\s*(\w+)?\s*$', line):
                (m, a, op, b) = (match.group(1), match.group(2), match.group(3), match.group(4))
                if m == ROOT:
                    op = '='
                # print(m, a, op, b)
                monkeys[m] = (op, a, b) if op is not None else int(a)
    return monkeys

def discern(monkeys: dict, humn_dir: dict, m: str):
    if m == HUMN:
        humn_dir[m] = 0
        return True
    item = monkeys[m]
    if isinstance(item, int):
        return False
    (_, a, b) = item
    if discern(monkeys, humn_dir, a):
        humn_dir[m] = 0
        return True
    if discern(monkeys, humn_dir, b):
        humn_dir[m] = 1
        return True
    return False

def calc(monkeys: dict, humn_dir: dict, m: str, v = None):
    dir = humn_dir.get(m)
    if m == HUMN:
        monkeys[m] = v
    item = monkeys[m]
    if isinstance(item, int):
        return item
    (op, a, b) = item
    f = FUNCS[op]
    if dir is None:
        return f(calc(monkeys, humn_dir, a), calc(monkeys, humn_dir, b))
    (source, target) = (a, b) if dir else (b, a)
    x = calc(monkeys, humn_dir, source)
    g = INVRS[op]
    y = g(v, x, dir)
    if dir:
        assert f(x, y) == v
    else:
        assert f(y, x) == v
    return calc(monkeys, humn_dir, target, y)

def main():
    monkeys = parse_input(FILENAME)
    discern(monkeys, humn_dir := {}, ROOT)
    print(monkeys)
    print(calc(monkeys, humn_dir, ROOT, True))
    print(monkeys[HUMN])


if __name__ == '__main__':
    main()
