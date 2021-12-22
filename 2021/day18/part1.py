from Pair import Pair
puzzle_input = [s.strip() for s in open('input.in').readlines()]
# construct pairs
pairs = []
for line in puzzle_input:
    master_pair = Pair()
    stack = [master_pair]
    for c in line[1:-1]:
        if c == '[':
            pair = Pair()
            pairent = stack[-1]
            if None is pairent.left:
                pairent.left = pair
            else:
                pairent.right = pair
            pair.pairent = pairent
            stack.append(pair)
        elif c == ']':
            stack.pop()
        elif c.isdigit():
            pair = stack[-1]
            if None is pair.left:
                pair.left = int(c)
            else:
                pair.right = int(c)
    pairs.append(master_pair)

for i in range(1, len(pairs)):
    added = Pair()
    added.left = pairs[i-1]
    added.right = pairs[i]
    pairs[i-1].pairent = added
    pairs[i].pairent = added
    while True:
        if not added.explode():
            if not added.split():
                break
    pairs[i] = added
print('magnitude:', added.magnitude())