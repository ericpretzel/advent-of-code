puzzle_input = [s.strip() for s in open('input.in').readlines()]

tubes = {}

for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        coord = (x, y)
        tubes[coord] = int(puzzle_input[y][x])
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

# dict of sets, key is the lowest point of the basin
basins = {}

def get_basin(coord, basin):
    tube = tubes[coord]
    if tube == 9: return

    basins[basin].add(coord)
    # reach out to greater tiles only
    for c in filter(lambda co: co != coord and tubes[co] > tube, adjacent_tiles(coord)):
        get_basin(c, basin)

# generate basins
for coord in tubes:
    if not is_border(coord) and is_pit(coord):
        tube = tubes[coord]
        basins[coord] = {coord}
        for adj in adjacent_tiles(coord):
            get_basin(adj, coord)

sorted_basins = sorted(basins.values(), key=len, reverse=True)
print("product:", len(sorted_basins[0])*len(sorted_basins[1])*len(sorted_basins[2]))