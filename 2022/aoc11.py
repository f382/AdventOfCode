from re import search
from collections import deque
from dataclasses import dataclass, field
from functools import reduce, partial
from operator import add, mul
from typing import Callable, Generator
from math import lcm

# FILENAME = "aoc11-0.txt"
FILENAME = "aoc11-1.txt"

# ROUNDS = 20
# COOLDOWN = 3
ROUNDS = 10000
COOLDOWN = 1

OPERATIONS = {'+': add, '*': mul}

def double_args(f: Callable) -> Callable:
    return lambda *args: f(*args, *args)

def compile_rule(operation: tuple, test: int, throw: tuple) -> Callable:
    (symbol, value) = operation
    f = OPERATIONS[symbol]
    if value is not None:
        g = partial(f, value)
    else:
        g = double_args(f)
    if COOLDOWN == 1:
        h = g
    else:
        h = lambda item: g(item) // COOLDOWN
    def apply(item: int) -> tuple:
        item = h(item)
        return (item, throw[item % test != 0])
    return apply

@dataclass(order=True)
class Monkey:
    activity: int = field(default=0, init=False)
    test: int = field()
    rule: Callable = field(repr=False, compare=False)
    items: deque = field(default_factory=deque)

    def act(self, monkeys: list, multiple: int):
        while self.items:
            item = self.items.popleft()
            (item, target) = self.rule(item)
            monkeys[target].items.append(item % multiple)
            self.activity += 1

def parse_input(filename: str) -> Generator:
    with open(filename, "r", encoding="utf-8") as file:
        for chunk in file.read().split('\n\n'):
            m = search(r'\s*Starting items: (.*)'
                       r'\s*Operation: new = old (.+) (.+)'
                       r'\s*Test: divisible by (.+)'
                       r'\s*If true: throw to monkey (.+)'
                       r'\s*If false: throw to monkey (.+)',
                       chunk)
            items = deque(int(item) for item in m.group(1).split(', '))
            operand = m.group(3)
            operation = (m.group(2), int(operand) if operand.isnumeric() else None)
            test = int(m.group(4))
            throw = (int(m.group(5)), int(m.group(6)))
            yield Monkey(test, compile_rule(operation, test, throw), items)

def business(monkeys: list, multiple: int):
    for monkey in monkeys:
        monkey.act(monkeys, multiple)

def print_monkeys(k: int, monkeys: list):
    print(f'== {k:5} ==')
    for monkey in monkeys:
        print(monkey)

def main():
    monkeys = list(parse_input(FILENAME))
    multiple = lcm(*(monkey.test for monkey in monkeys))
    for k in range(ROUNDS):
        if k % 100 == 0:
            print_monkeys(k, monkeys)
        business(monkeys, multiple)
    print_monkeys(ROUNDS, monkeys)
    most_active = sorted(monkeys, reverse=True)
    monkey_business = reduce(mul, (monkey.activity for monkey in most_active[:2]), 1)
    print(monkey_business)

if __name__ == '__main__':
    main()
