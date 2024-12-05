
puzzle = [line.strip() for line in open("input.in").readlines()]


pages = dict()
for i in range(len(puzzle)):
    line = puzzle[i]
    if not line:
        break
    page1, page2 = map(int, line.split("|"))
    pages.setdefault(page1, set()).add(page2)
from functools import cmp_to_key
s = 0

for j in range(i + 1, len(puzzle)):
    line = puzzle[j]
    if not line:
        break
    update = list(map(int, line.split(",")))
    ordered = sorted(update, key=cmp_to_key(lambda x, y: -1 if x in pages and y in pages[x] else 1))
    print(update, ordered)
    for x, y in zip(update, ordered):
        if x != y:
            break
    else:
        s += update[len(update) // 2]

print(s)
