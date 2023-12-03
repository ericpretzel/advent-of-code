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


def gear_adj(y, x):
    adj = [grid[y-1][x], grid[y-1][x+1],grid[y][x+1], grid[y+1][x+1], grid[y+1][x], grid[y+1][x-1], grid[y][x-1], grid[y-1][x-1]]


    gears = set()
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0: continue
            if grid[y+dy][x+dx] == '*': gears.add( (y+dy, x+dx))
    return gears

y = 1

# (y, x) : [numbers]
gears = dict()

while y < height - 1:
    x = 1
    while x < width - 2:
        number = ''
        gears_found = set()
        while grid[y][x].isdigit():
            number += grid[y][x]
            gears_found.update(gear_adj(y, x))
            x += 1
        x += 1
        for gear in gears_found: 
            gears[gear] = gears.get(gear, list()) + [int(number)]
    y += 1


print(gears)
print(sum(numbers[0] * numbers[1] for numbers in gears.values() if len(numbers) == 2))