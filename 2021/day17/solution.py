with open('input.in') as f:
    line = f.readline().split(' ')
    x = line[2][2:-1].split('..')
    x_range = range(int(x[0]), int(x[1])+1)
    y = line[3][2:].split('..')
    y_range = range(int(y[0]), int(y[1])+1)

def intersects(pos, vx, vy):
    x, y = pos[0], pos[1]
    if x in x_range and y in y_range:
        return True
    elif x >= x_range.stop or y < y_range.start:
        return False
    # move the probe
    x += vx
    y += vy
    # accelerate/decelerate
    vx += 1 if vx < 0 else -1 if vx > 0 else 0
    vy -= 1
    return intersects((x,y), vx, vy)

# cumulative sum
cum = lambda n: n*(n+1)//2
# inverse of above
inv = lambda n: int((8*n+1)**0.5-1)//2

# figure out bounds for velocities
min_vx = inv(x_range.start)
max_vx = x_range.stop

min_vy = y_range.start-1
max_vy = abs(y_range.start)-1

count = 0
for vx in range(min_vx, max_vx+1):
    for vy in range(min_vy, max_vy+1):
        if intersects((0,0), vx, vy):
            count += 1

print('highest_y:', cum(max_vy))
print('count:', count)
