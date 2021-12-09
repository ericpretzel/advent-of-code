puzzle_input = [s.strip() for s in open('input.in').readlines()]

tubes = {}

for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        coord = (x, y)
        tubes[coord] = int(puzzle_input[y][x])
        # pad the input
        tubes[(-1, y)] = 9
        tubes[(len(puzzle_input[0]), y)] = 9
        tubes[(x, -1)] = 9
        tubes[(x, len(puzzle_input))] = 9

# corners
tubes[(-1, -1)] = 9
tubes[(-1, len(puzzle_input))] = 9
tubes[(len(puzzle_input[0]), -1)] = 9
tubes[(len(puzzle_input[0]), len(puzzle_input))] = 9

def is_border(coord):
    return coord[0] == -1 or coord[1] == -1\
        or coord in [(-1, -1), (-1, len(puzzle_input)),\
        (len(puzzle_input[0]), -1), (len(puzzle_input[0]), len(puzzle_input))]

def adjacent_tiles(coord):
    x, y = coord[0], coord[1]
    up = (x, y-1)
    down = (x, y+1)
    left = (x-1, y)
    right = (x+1, y)
    return [up, down, left, right]

def is_pit(coord):
    tube = tubes[coord]
    up, down, left, right = adjacent_tiles(coord)
    return tubes[up] > tube \
        and tubes[down] > tube \
        and tubes[left] > tube \
        and tubes[right] > tube

risk = 0

for coord in tubes:
    if not is_border(coord) and is_pit(coord):
        risk += 1 + tubes[coord]


print("risk:", risk)
