puzzle_input = [line.strip() for line in open('input.in').readlines()]

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = {s[i] : i+1 for i in range(len(s))}

total = 0
for line in puzzle_input:
    a = line[:len(line)//2]
    b = line[len(line)//2:]
    total += sum(priority[m] for m in set(c for c in a).intersection(c for c in b))

print(total)
