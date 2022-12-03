puzzle_input = [line.strip() for line in open('input.in').readlines()]

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = {s[i] : i+1 for i in range(len(s))}

total = 0
for i in range(0, len(puzzle_input), 3):
    a, b, c = puzzle_input[i:i+3]
    total += sum(priority[m] for m in set(ch for ch in a).intersection(ch for ch in b).intersection(ch for ch in c))

print(total)