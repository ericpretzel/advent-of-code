pi = [line.strip() for line in open('input.in').readlines()]

grid = dict()
max_x = len(pi[0])
max_y = len(pi)
for y in range(max_y):
    for x in range(max_x):
        grid[(x, y)] = int(pi[y][x])

visible = set()
# from horizontal

for y in range(max_y):
    max_tree = -1
    for x in range(max_x):
        tree = grid[(x, y)]
        if tree > max_tree:
            visible.add( (x, y) )
            max_tree = tree
    max_tree = -1
    for x in reversed(range(max_x)):
        tree = grid[(x, y)]
        if tree > max_tree:
            visible.add( (x, y) )
            max_tree = tree
# from vertical
for x in range(max_x):
    max_tree = -1
    for y in range(max_y):
        tree = grid[(x, y)]
        if tree > max_tree:
            visible.add( (x, y) )
            max_tree = tree
    max_tree = -1
    for y in reversed(range(max_y)):
        tree = grid[(x, y)]
        if tree > max_tree:
            visible.add( (x, y) )
            max_tree = tree    
print(len(visible))