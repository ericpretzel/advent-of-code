pi = [line.strip() for line in open('input.in').readlines()]
pos = set()
pos.add( (0, 0))

hx = hy = tx = ty = 0
for line in pi:
    direction = line.split(' ')[0]
    amt = int(line.split(' ')[1])
    print(direction, amt)
    if direction == 'R':
        if abs(hx+amt-tx) > 1:
            ty = hy
        hx += amt
        while tx < hx-1:
            tx += 1
            pos.add( (tx, ty) )
    elif direction == 'L':
        if abs(hx-amt-tx) > 1:
            ty = hy
        hx -= amt
        while tx > hx+1:
            tx -= 1
            pos.add( (tx, ty) )
    elif direction == 'U':
        if abs(hy-amt-ty) > 1:
            tx = hx
        hy -= amt
        while ty > hy+1:
            ty -= 1
            pos.add( (tx, ty) )
    elif direction == 'D':
        if abs(hy+amt-ty) > 1:
            tx = hx
        hy += amt
        while ty < hy-1:
            ty += 1
            pos.add( (tx, ty) )
    print(f'H: {(hx, hy)}')
    print(f'T: {(tx, ty)}')

for y in range(-10, 10):
    for x in range(-10, 10):
        print('#' if (x,y) in pos else '.', end='')
    print()

print(len(pos))
