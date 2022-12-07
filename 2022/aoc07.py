#FILENAME = "aoc07-0.txt"
FILENAME = "aoc07-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

import re

TOTAL = 70000000
NEEDED = 30000000

tree = {}
pos = []
cur = pos

sizes = {}

def putdir(pos: list, d: str):
    loc = tree
    for p in pos:
        loc = loc.setdefault(p, {})
    loc.setdefault(d, {})

def putfile(pos: list, f: str, s: int):
    loc = tree
    for p in pos:
        loc = loc.setdefault(p, {})
    loc[f] = s

def calcsize(tree) -> int:
    size = 0
    if isinstance(tree, dict):
        for c in tree.values():
            size += calcsize(c)
        sizes[id(tree)] = size
    if isinstance(tree, int):
        size = tree
    return size

for l in lines:
    if match := re.match(r'^\$ cd (.*)', l):
        target = match.group(1)
        print(f"{l} {target=}")
        match target:
            case '/':
                del pos[:]
            case '..':
                pos.pop()
            case d:
                pos.append(d)
    # if match := re.match(r'^\$ ls', l):
    #     cur = pos
    #     print(f"{l} {cur=}")
    if match := re.match(r'^dir (.*)', l):
        d = match.group(1)
        putdir(cur, d)
    if match := re.match(r'^(\d+) (.*)', l):
        s, f = int(match.group(1)), match.group(2)
        putfile(cur, f, s)

print(tree)

calcsize(tree)
print(sizes)

small = [s for s in sizes.values() if s <= 100000]
print(sum(small))

used = sizes[id(tree)]
ss = sorted(sizes.values())
ok = [s for s in ss if TOTAL - used + s >= NEEDED]

print(ok)
