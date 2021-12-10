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
    
    while x1 != x2 or y1 != y2:
        increment((x1, y1))
        x1 += 1 if x1<x2 else -1 if x1>x2 else 0
        y1 += 1 if y1<y2 else -1 if y1>y2 else 0
    increment((x2, y2))  

points = len(list(filter(lambda v: v > 1, grid.values())))
print("points:", points)