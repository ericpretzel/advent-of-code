class Cave:
    def __init__(self, val, visited=False):
        self.connections = []
        self.val = val
        self.visited = visited
    
    def is_big(self):
        return self.val.isupper()

def visit_caves(cave):
    if cave.val == 'end':
        return 1
    total_visits = 0
    if not cave.is_big():
        cave.visited = True
    for connection in cave.connections:
        if connection.is_big() or (not connection.is_big() and not connection.visited):
            total_visits += visit_caves(connection)
    cave.visited = False
    return total_visits


puzzle_input = [s.strip() for s in open('input.in').readlines()]

caves = {}

# instantiate caves first idk how else lol
for line in puzzle_input:
    cave_val, next_cave = line.split("-")
    if caves.get(cave_val) is None:
        caves[cave_val] = Cave(cave_val)
    if caves.get(next_cave) is None:
        caves[next_cave] = Cave(next_cave)

# set up connections
for line in puzzle_input:
    cave_val, next_cave = line.split("-")
    caves[cave_val].connections.append(caves[next_cave])
    caves[next_cave].connections.append(caves[cave_val])

print('paths:', visit_caves(caves['start']))






