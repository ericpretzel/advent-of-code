pi = [line.strip() for line in open('input.in').readlines()]
pos = set()
pos.add( (0, 0))

knots = [(0, 0) for _ in range(10)]

def visualize(knots):
    dict = {(x, y) : '.' for x in range(-32, 32) for y in range(-32, 32)}
    
    for i, e in enumerate(knots):
        x, y = e[:2]
        dict[(x, y)] = i
    dict[(0, 0)] = 's'
    for y in range(-32, 32):
        for x in range(-32, 32):
            print(dict[(x, y)], end='')
        print()
    print('-------------------')


for line in pi:
    direction = line.split(' ')[0]
    amount = int(line.split(' ')[1])
    print(direction, amount)
    for s in range(amount):

        
        hx, hy = knots[0][:2]
        if direction == 'R':
            hx += 1
        elif direction == 'L':
            hx -= 1
        elif direction == 'U':
            hy -= 1
        elif direction == 'D':
            hy += 1
        knots[0] = (hx, hy)

        for i in range(1, len(knots)):
            #if line == 'U 8': visualize(knots)
            hx, hy = knots[i-1][:2]
            tx, ty = knots[i][:2]
            # im gonna
            if hy-ty > 1 and hx-tx > 1:
                tx += 1
                ty += 1
            elif hy-ty > 1 and hx-tx < -1:
                tx -= 1
                ty += 1
            elif hy-ty<-1 and hx-tx > 1:
                tx += 1
                ty -= 1
            elif hy-ty<-1 and hx-tx<-1:
                tx -= 1
                ty -= 1
            elif hx-tx > 1:
                ty = hy
                tx += 1
            elif hx-tx < -1:
                ty = hy
                tx -= 1
            elif hy-ty > 1:
                tx = hx
                ty += 1
            elif hy-ty < -1:
                #print('HERE')
                tx = hx
                ty -= 1
            
            if i == 9: pos.add( (tx, ty) )
            knots[i] = (tx, ty)

    print(f'H: {(hx, hy)}')
    print(f'T: {(tx, ty)}')


print(len(pos))