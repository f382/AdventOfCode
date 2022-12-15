import re

# FILENAME = "aoc15-0.txt"
FILENAME = "aoc15-1.txt"

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

def check(a, b, c, d):
    sortleft = lambda rh: rh[0][0]
    sorttop = lambda rh: rh[0][1]
    left = sorted((a, b, c, d), key = sortleft)
    (lt, lb, rt, rb) = sorted(left[:2], key = sorttop) + sorted(left[2:], key = sorttop)
    if sorttop(lb) < sorttop(rt):
        return
    summ   = lt[0][0] + lt[0][1] + lt[1] + 1
    summ_r = rb[0][0] + rb[0][1] - rb[1] - 1
    diff   = lb[0][0] - lb[0][1] + lb[1] + 1
    diff_r = rt[0][0] - rt[0][1] - rt[1] - 1
    if (summ == summ_r) and (diff == diff_r):
        x = (summ + diff) // 2
        y = (summ - diff) // 2
        print(lt, lb, rt, rb, '->', (x, y), '->', x * 4000000 + y)


rhombs = [(s, dist(s, b)) for (s, b) in pairs]

for i in range(len(pairs)):
    for j in range(i, len(pairs)):
        for k in range(j, len(pairs)):
            for l in range(k, len(pairs)):
                check(rhombs[i], rhombs[j], rhombs[k], rhombs[l])
