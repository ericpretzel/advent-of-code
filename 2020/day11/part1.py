puzzle_input = [s.strip() for s in open('input.in').readlines()]

seats = {}
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        seats[(x, y)] = puzzle_input[y][x]

def adjacent_seats(coord):
    x, y, = coord[0], coord[1]
    n = (x, y-1)
    ne = (x+1, y-1)
    e = (x+1, y)
    se = (x+1, y+1)
    s = (x, y+1)
    sw = (x-1, y+1)
    w = (x-1, y)
    nw = (x-1, y-1)
    return map(lambda c: seats.get(c, '.'), \
        [n, ne, e, se, s, sw, w, nw])

# why doesnt python have do-while loops
while True:
    num_changes = 0
    new_seats = seats.copy()

    # perform rules
    for seat in seats:
        if seats[seat] == 'L':
            if '#' not in adjacent_seats(seat):
                new_seats[seat] = '#'
                num_changes += 1
        elif seats[seat] == '#':
            if len(list(filter(lambda s: s=='#', adjacent_seats(seat)))) >= 4:
                new_seats[seat] = 'L'
                num_changes += 1
    if num_changes == 0: break
    seats = new_seats

# now get occupied seats
print("occupied:", len(list(filter(lambda s: s == '#', seats.values()))))