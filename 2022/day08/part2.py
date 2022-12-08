pi = [line.strip() for line in open('input.in').readlines()]

grid = dict()
max_x = len(pi[0])
max_y = len(pi)
for y in range(max_y):
    for x in range(max_x):
        grid[(x, y)] = int(pi[y][x])

def scenic_score(x, y, grid):
    left = right = up = down = 0
    for n in range(x-1, -1, -1):
        left += 1
        if grid[(n, y)] >= grid[(x, y)]:
            break
    for n in range(x+1, max_x):
        right += 1
        if grid[(n, y)] >= grid[(x, y)]:
            break
    for n in range(y-1, -1, -1):
        up += 1
        if grid[(x, n)] >= grid[(x, y)]:
            break
    for n in range(y+1, max_y):
        down += 1
        if grid[(x, n)] >= grid[(x, y)]:
            break
    return left*right*up*down

print(max(scenic_score(x, y, grid) for x, y in grid.keys()))