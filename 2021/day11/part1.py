puzzle_input = [s.strip() for s in open('input.in')]

octopi = {}
for y in range(10):
    for x in range(10):
        octopi[(x, y)] = int(puzzle_input[y][x])

def adjacent_octopi(coord): 
    x, y = coord[0], coord[1]
    n = (x, y-1)
    ne = (x+1, y-1)
    e = (x+1, y)
    se = (x+1, y+1)
    s = (x, y+1)
    sw = (x-1, y+1)
    w = (x-1, y)
    nw = (x-1, y-1)
    return list(filter(lambda c: c in octopi,\
        [n,ne,e,se,s,sw,w,nw]))

def flash(coord, flashed):
    if octopi[coord] > 9 and coord not in flashed:
        flashed.append(coord)
        octopi[coord] = 0
        flashes = 1
        for c in adjacent_octopi(coord):
            octopi[c] += 1 if c not in flashed else 0
            flashes += flash(c, flashed)
        return flashes
    else: return 0
        
total_flashes = 0
for i in range(100):
    flashed = []
    for coord in octopi:
        octopi[coord] += 1
    for coord in octopi:
        total_flashes += flash(coord, flashed)

print(total_flashes)