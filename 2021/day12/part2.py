class Cave:
    def __init__(self, val):
        self.connections = []
        self.val = val
        self.visits = 0
    
    def is_big(self):
        return self.val.isupper()

def visit_caves(cave, visited_small_cave_twice = False):
    if cave.val == 'end':
        return 1
    elif cave.val == 'start':
        if cave.visits == 0:
            cave.visits += 1 # can't return to start
        else: return 0

    total_visits = 0
    for connection in cave.connections:
        connection.visits += 1
        if not connection.is_big():
            if connection.visits == 2:
                if not visited_small_cave_twice:
                    total_visits += visit_caves(connection, True)
            elif connection.visits < 2: total_visits += visit_caves(connection, visited_small_cave_twice)
        else:
            total_visits += visit_caves(connection, visited_small_cave_twice)
        connection.visits -= 1
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






