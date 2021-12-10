puzzle_input = [s.strip() for s in open('testinput.in').readlines()]

valid_seats = []
seats = {}
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        valid_seats.append((x, y))
        seats[(x, y)] = puzzle_input[y][x]
        seats[(-1, y)] = '.'
        seats[(len(puzzle_input[y]), y)] = '.'
        seats[(x, -1)] = '.'
        seats[(x, len(puzzle_input))] = '.'

print(seats)

# this will be very painful
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

    n, ne, e, se, s, sw, w, nw = map(lambda c: seats.get(c, '.'), \
        [n, ne, e, se, s, sw, w, nw])

    x, y = coord[0], coord[1]
    while y > 0 and n == '.':
        y -= 1
        n = seats[(x,y)]
    
    x, y = coord[0], coord[1]
    while y > 0 and x < len(puzzle_input[0])-1 and ne == '.':
        x += 1
        y -= 1
        ne = seats[(x,y)]
    
    x, y = coord[0], coord[1]
    while x < len(puzzle_input[0])-1 and e == '.':
        x += 1
        e = seats[(x,y)]
    
    x, y = coord[0], coord[1]
    while x < len(puzzle_input[0])-1 and se == '.':
        x += 1
        y += 1
        se = seats[(x,y)]
    
    x, y = coord[0], coord[1]
    while y < len(puzzle_input)-1 and s == '.':
        y+=1
        s = seats[(x,y)]
    
    x, y = coord[0], coord[1]
    while y < len(puzzle_input)-1 and x > 0 and sw == '.':
        x -= 1
        y += 1
        sw = seats[(x,y)]
    
    x, y = coord[0], coord[1]
    while x > 0 and w == '.':
        x -= 1
        w = seats[(x,y)]

    x, y = coord[0], coord[1]
    while x > 0 and y > 0 and nw == '.':
        x -= 1
        y -= 1
        nw = seats[(x,y)]
    return [n, ne, e, se, s, sw, w, nw]

# why doesnt python have do-while loops
while True:
    num_changes = 0
    new_seats = seats.copy()

    # perform rules
    for seat in valid_seats:
        if seats[seat] == 'L':
            if '#' not in adjacent_seats(seat):
                new_seats[seat] = '#'
                num_changes += 1
        elif seats[seat] == '#':
            if len(list(filter(lambda s: s=='#', adjacent_seats(seat)))) >= 5:
                new_seats[seat] = 'L'
                num_changes += 1
    if num_changes == 0: break
    seats = new_seats

# now get occupied seats
print("occupied:", len(list(filter(lambda s: s == '#', seats.values()))))