from Pair import Pair
puzzle_input = [s.strip() for s in open('input.in').readlines()]

def construct(s):
    master_pair = Pair()
    stack = [master_pair]
    for c in s[1:-1]:
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
    return stack.pop()

max_mag = -1
for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input)):
        if i == j: continue
        left = construct(puzzle_input[i])
        right = construct(puzzle_input[j])
        added = Pair()
        added.left = left
        added.right = right
        while True:
            if not added.explode():
                if not added.split():
                    break
        max_mag = max(max_mag, added.magnitude())


print('max:', max_mag)