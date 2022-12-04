puzzle_input = [line.strip() for line in open('input.in').readlines()]

c = 0
for line in puzzle_input:
    a, b = line.split(',')
    alo, ahi = a.split('-')
    blo, bhi = b.split('-')
    if int(alo) <= int(blo) and int(ahi) >= int(bhi):
        c += 1
        continue
    if int(blo) <= int(alo) and int(bhi) >= int(ahi):
        c += 1

print(c)
