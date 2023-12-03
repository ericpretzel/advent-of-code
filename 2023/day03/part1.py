l = [line.strip() for line in open('input.in').readlines()]

print(l)
grid = []
for line in l:
    grid.append(['.'] + [c for c in line] + ['.'])


width = len(grid[0])
height = len(grid)

grid.insert(0, ['.' for _ in range(width)])
grid.append(['.' for _ in range(width)])
print(grid)
s = 0

width += 2
height += 2


def has_symbol_adj(y, x):
    adj = [grid[y-1][x], grid[y-1][x+1],grid[y][x+1], grid[y+1][x+1], grid[y+1][x], grid[y+1][x-1], grid[y][x-1], grid[y-1][x-1]]
    return any(not c.isdigit() and c != '.' for c in adj)

y = 1

while y < height - 1:
    x = 1
    while x < width - 2:
        number = ''
        add = False
        while grid[y][x].isdigit():
            print(grid[y][x])
            number += grid[y][x]
            if not add: add |= has_symbol_adj(y, x)
            x += 1
        x += 1
        if add and len(number) > 0: 
            print(number)
            s += int(number)
    y += 1

print(s)