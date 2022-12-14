pi = [line.strip() for line in open('input.in').readlines()]

grid = dict()

for line in pi:
    coords = [tuple(map(int, c.split(','))) for c in line.split(' -> ')]
    px, py = coords[0]
    grid[(px, py)] = '#'
    for x, y in coords[1:]:
        while px != x:
            px += 1 if px < x else -1
            grid[(px, py)] = '#'
        while py != y:
            py += 1 if py < y else -1
            grid[(px, py)] = '#'
        px, py = x, y

floor = max(c[1] for c in grid) + 2
units = 0
while grid.get((500, 0), '.') != '+':
    units += 1
    x, y = 500, 0
    while y < floor-1:
        below = [grid.get((a, y+1), '.') for a in [x-1, x, x+1]]
        if below[1] == '.':
            y += 1
        elif below[0] == '.':
            y += 1
            x -= 1
        elif below[2] == '.':
            y += 1
            x += 1
        else:
            break
    grid[(x, y)] = '+'

print(units)