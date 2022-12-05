#FILENAME = "aoc05-0.txt"
FILENAME = "aoc05-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    data = file.read()

import re

#stack_matches = re.findall(r'^(?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   )', data, re.M)
stack_matches = re.findall(r'^(?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   ) (?:\[(\w)\]|   )', data, re.M)
#print(stack_matches)

moves = (tuple(int(d) for d in t) for t in re.findall(r'move (\d+) from (\d+) to (\d+)', data))
#print(moves)

stacks = tuple([] for _ in stack_matches[0])

for sm in stack_matches:
    for i, x in enumerate(sm):
        if x:
            stacks[i].insert(0, x)
print(stacks)

def move(n: int, a: list, b: list):
    y = a[-n:]
    del a[-n:]
    b.extend(y)

for m in moves:
    move(m[0], stacks[m[1] - 1], stacks[m[2] - 1])
print(stacks)

print("".join(s[-1] for s in stacks))
