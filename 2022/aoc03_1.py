#FILENAME = "aoc03-0.txt"
FILENAME = "aoc03-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]


def prio(x: str):
    if 'a' <= x:
        return 1 + ord(x) - ord('a')
    return 27 + ord(x) - ord('A')


doub = []

group = []
for l in lines:
    group.append(l)
    if len(group) == 3:
        print(group)
        for i in group[0]:
            if i in group[1] and i in group[2]:
                doub.append(i)
                break
        group = []

pr = [prio(x) for x in doub]

print('========================================')
print(f"{pr}\t{sum(pr)}")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
