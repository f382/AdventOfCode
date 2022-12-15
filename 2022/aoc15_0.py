import re

# FILENAME = "aoc15-0.txt"
# Y = 10
FILENAME = "aoc15-1.txt"
Y = 2000000

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines()]

pairs = []
for line in lines:
    if m := re.match(r'.*?x=(.*), y=(.*): .*?x=(.*), y=(.*)', line):
        s = (int(m.group(1)), int(m.group(2)))
        b = (int(m.group(3)), int(m.group(4)))
        pairs.append((s, b))


def dist(p, q) -> int:
    return abs(q[0] - p[0]) + abs(q[1] - p[1])

def dist_y(p, y: int) -> int:
    return abs(y - p[1])


shadows = ((s[0], dist(s, b) - dist_y(s, Y)) for (s, b) in pairs)
regions = sorted((x - d, x + d) for (x, d) in shadows if d >= 0)
i = 1
while i < len(regions):
    if regions[i-1][1] >= regions[i][0]:
        regions[i-1] = (regions[i-1][0], max(regions[i-1][1], regions[i][1]))
        del regions[i]
        continue
    i += 1
print(f'{regions=}')

actual = [s for (_, s) in pairs if s[1] == Y]
print(f'{actual=}')

print(sum(r - l + 1 - len(set(s for s in actual if l <= s[0] <= r)) for (l, r) in regions))
