import re


# FILENAME = "aoc21-0.txt"
FILENAME = "aoc21-1.txt"

ROOT = 'root'

FUNCS = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
         '/': lambda x, y: x // y}

INVRS = {'+': lambda v, x, dir: v - x,
         '-': lambda v, x, dir: x - v if dir else v + x,
         '*': lambda v, x, dir: v // x,
         '/': lambda v, x, dir: x // v if dir else v * x}


def parse_input(filename: str) -> dict:
    monkeys = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if match := re.match(r'^(\w+):\s*(\w+)\s*(\S)?\s*(\w+)?\s*$', line):
                (m, a, op, b) = (match.group(1), match.group(2), match.group(3), match.group(4))
                # print(m, a, op, b)
                monkeys[m] = (op, a, b) if op is not None else int(a)
    return monkeys

def calc(monkeys: dict, m: str):
    item = monkeys[m]
    if isinstance(item, int):
        return item
    (op, a, b) = item
    f = FUNCS[op]
    return f(calc(monkeys, a), calc(monkeys, b))


def main():
    monkeys = parse_input(FILENAME)
    print(monkeys)
    print(calc(monkeys, ROOT))


if __name__ == '__main__':
    main()
