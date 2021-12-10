import re
puzzle_input = [s.strip() for s in open('input.in').readlines()]

grid = {}

def increment(point):
    val = grid.get(point)
    if val is None:
        grid[point] = 1
    else:
        grid[point] = val+1

for line in puzzle_input:
    line = re.split("\\D+", line)
    x1 = int(line[0])
    y1 = int(line[1])
    x2 = int(line[2])
    y2 = int(line[3])
    
    if y1 == y2:
        startX = min(x1, x2)
        endX = max(x1, x2)
        for x in range(startX, endX+1):
            increment((x, y1))
    elif x1 == x2:
        startY = min(y1, y2)
        endY = max(y1, y2)
        for y in range(startY, endY+1):
            increment((x1, y))
    
points = len(list(filter(lambda v: v > 1, grid.values())))
print("points:", points)