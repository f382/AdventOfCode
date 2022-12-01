"""Advent of Code 2022-12-01"""

with open("aoc01-1.txt", "r", encoding = "utf-8") as file:
    lines = [l.strip() for l in file.readlines()] + [""]

sums = []
s = 0
for line in lines:
    if not line:
        sums.append(s)
        s = 0
        continue
    s += int(line)

maximum = max(sums)
print(f"{maximum}\n")

sums.sort()
top3 = sums[-3:]
total = sum(top3)
print(f"{top3}: {total}\n")
