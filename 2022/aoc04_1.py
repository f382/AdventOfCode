#FILENAME = "aoc04-0.txt"
FILENAME = "aoc04-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

import re


c = 0

for l in lines:
    m = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', l)
    a, b, x, y = (int(d) for d in m.groups())
    if a > y or x > b:
        print(f"{l}\t{a}-{b} ! {x}-{y}")
        continue
    print(f"{l}\t{a}-{b} ~ {x}-{y}")
    c += 1

print('========================================')
print(f"{c}\t{c}")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
