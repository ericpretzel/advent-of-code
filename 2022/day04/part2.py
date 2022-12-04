puzzle_input = [line.strip() for line in open('input.in').readlines()]

c = 0
for line in puzzle_input:
    a, b = line.split(',')
    alo, ahi = a.split('-')
    blo, bhi = b.split('-')
    if (int(alo) > int(bhi)) or (int(ahi) < int(blo)):
        print(a, b)
        continue

    c += 1

print(c)
