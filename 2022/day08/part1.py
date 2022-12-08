pi = [line.strip() for line in open('input.in').readlines()]

grid = dict()
max_x = len(pi[0])
max_y = len(pi)
for y in range(max_y):
    for x in range(max_x):
        grid[(x, y)] = int(pi[y][x])

def is_visible(x, y, grid):
    if all(grid[(n, y)] < grid[(x, y)] for n in range(x)):
        return 1
    if all(grid[(n, y)] < grid[(x, y)] for n in range(x+1, max_x)):
        return 1
    if all(grid[(x, n)] < grid[(x, y)] for n in range(y)):
        return 1
    if all(grid[(x, n)] < grid[(x, y)] for n in range(y+1, max_y)):
        return 1
    return 0

print(sum(is_visible(x, y, grid) for x, y in grid.keys()))