#FILENAME = "aoc03-0.txt"
FILENAME = "aoc03-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]


def prio(x: str):
    if 'a' <= x:
        return 1 + ord(x) - ord('a')
    return 27 + ord(x) - ord('A')


sack = [(l[:(len(l)//2)], l[(len(l)//2):]) for l in lines]
print(sack)

doub = []

for s in sack:
    for i in s[0]:
        if i in s[1]:
            doub.append(i)
            break

pr = [prio(x) for x in doub]

print('========================================')
print(f"{pr}\t{sum(pr)}")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
