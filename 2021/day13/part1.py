puzzle_input = [s.strip() for s in open('input.in').readlines()]

paper = {}
def fold(axis, line):
    for coord in filter(lambda c: paper[c] and c[0] < width and c[1] < height, paper):
        x, y = coord[0], coord[1]
        if axis == 'x':
            new_x = line - (x - line) if x > line else x
            paper[(new_x, y)] = True
        elif axis == 'y':
            new_y = line - (y - line) if y > line else y
            paper[(x, new_y)] = True

# construct paper
width, height = 0, 0
for i in range(len(puzzle_input)):
    if puzzle_input[i] == '': break
    line = puzzle_input[i].split(',')
    x, y = int(line[0]), int(line[1])
    width = max(width, x+1)
    height = max(height, y+1)
    paper[(x, y)] = True

# fill the rest of the paper with False
for x in range(width):
    for y in range(height):
        paper[(x, y)] = paper.get((x, y), False)

# get instructions
instructions = []
for i in range(i+1, len(puzzle_input)):
    line = puzzle_input[i]
    a, l = line[line.rindex(" ")+1:].split("=")
    fold(axis=a, line=int(l))
    if a == 'x':
        width //= 2
    elif a == 'y':
        height //= 2
    break # only get the first instruction for p1

dots_count = 0
for x in range(width):
    for y in range(height):
        if paper.get((x, y), False):
            dots_count += 1

print("dots:", dots_count)


