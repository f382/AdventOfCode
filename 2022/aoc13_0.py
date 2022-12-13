import ast
from functools import cmp_to_key

# FILENAME = "aoc13-0.txt"
FILENAME = "aoc13-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    data = file.read().strip()

def parse(s: str):
    # print(repr(x))
    return ast.literal_eval(s)

def compare(a: list | int, b: list | int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        if a > b:
            return 1
        return 0
    if isinstance(a, int):
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])
    ## comment this out for part two (why?!):
    if not any(a) and not any(b):
        return 0
    ##
    if not any(a):
        return -1
    if not any(b):
        return 1
    d = compare(a[0], b[0])
    if d:
        return d
    return compare(a[1:], b[1:])

pairs = [[parse(s) for s in c.split('\n')] for c in data.split('\n\n')]
# print(pairs)

cmp = [compare(*p) for p in pairs]
# print(cmp)

ok = [(i, d) for (i, d) in enumerate(cmp) if d <= 0]

print(sum(i + 1 for (i, _) in ok))

stuff = [x for p in pairs for x in p]
stuff.append([[2]])
stuff.append([[6]])
stuff.sort(key=cmp_to_key(compare))
# for x in stuff:
#     print(repr(x))
# print(len(stuff))
j = stuff.index([[2]]) + 1
k = stuff.index([[6]]) + 1
print(j, k, j * k)
