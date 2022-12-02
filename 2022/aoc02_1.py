"""Advent of Code 2022-12-02"""

abc = ('A', 'B', 'C')
xyz = ('X', 'Y', 'Z')
pts = (1, 2, 3)
rel = (1, 2, 0)

with open("aoc02-1.txt", "r", encoding = "utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

rounds_alpha = [l.split() for l in lines]

rounds = [(abc.index(a), xyz.index(x)) for a, x in rounds_alpha]
print(f"{rounds!r}")

score = 0

for r in rounds:
    a, x = r
    z = None
    for y in range(3):
        w = rel[y - a]
        if w == x:
            z = y
    p = pts[z]
    w = rel[z - a]
    s = p + w * 3
    print(f"{a} {z} ({x}) -> {s}\n")
    score += s

print(f"{score}\n")
