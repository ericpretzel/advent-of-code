# this solution only works with 
# a '#' as the first character 
# in the algorithm and a '.'
# as the last

grid = {}
with open('input.in') as f:
    algorithm = f.readline().strip()

    f.readline()
    img = [s.strip() for s in f.readlines()]
    width, height = len(img[0]), len(img)
    min_x = -3
    max_x = width+3
    min_y = -3
    max_y = height+3
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if x in range(width) and y in range(height):
                c = '0' if img[y][x]=='.' else '1'
            else:
                c = '0'
            grid[(x,y)]=c

def square(c):
    x, y = c[0],c[1]
    n = (x,y-1)
    ne = (x+1,y-1)
    e = (x+1,y)
    se = (x+1,y+1)
    s = (x,y+1)
    sw = (x-1,y+1)
    w = (x-1,y)
    nw = (x-1,y-1)
    return [nw,n,ne,w,c,e,sw,s,se]

for i in range(50): # change to 2 for part 1
    new_grid = {}
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            a = map(lambda n: grid.get(n, '0' if i%2==0 else '1'),square((x,y)))
            b = '0b' + ''.join(a)
            num = int(b, base=2)
            if algorithm[num] == '#':
                new_grid[(x,y)] = '1'
            else: 
                new_grid[(x,y)] = '0'
    grid = new_grid
    min_x -= 3
    min_y -= 3
    max_x += 3
    max_y += 3

print('lit:', len(list(filter(lambda a: a =='1', grid.values()))))
