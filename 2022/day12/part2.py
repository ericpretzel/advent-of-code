from heapq import heappop, heappush # for min-priority queue

puzzle_input = [s.strip() for s in open('input.in').readlines()]
width, height = len(puzzle_input[0]), len(puzzle_input)

grid = {}

for x in range(width):
    for y in range(height):
        if puzzle_input[y][x] == 'S':
            s_pos = (x, y)
            grid[(x, y)] = ord('a')
        elif puzzle_input[y][x] == 'E':
            e_pos = (x, y)
            grid[(x, y)] = ord('z')
        else: grid[(x, y)] = ord(puzzle_input[y][x])

def neighbors(coord):
    x, y = coord[0], coord[1]
    n = (x, y-1)
    e = (x+1, y)
    s = (x, y+1)
    w = (x-1, y)
    return filter(lambda c: c in grid, [n,e,s,w])

def cleanup_a(c, to_remove):
    if c in to_remove: return
    if all(grid[n] == ord('a') for n in neighbors(c)):
        to_remove.add(c)
        for n in neighbors(c):
            cleanup_a(n, to_remove)

to_remove = set()
for c in grid:
    if grid[c] == ord('a'):
        cleanup_a(c, to_remove)

for a in to_remove:
    del grid[a]

def dijkstra(src, dst):
    dist = {}
    queue = []
    for node in grid:
        dist[node] = 999999
        heappush(queue, (dist[node], node))
    
    dist[src] = 0
    heappush(queue, (0, src))
    while len(queue) > 0:
        current = heappop(queue)[1]
        for neighbor in filter(lambda n: grid[n] - grid[current] <= 1, neighbors(current)):
            cost = dist[current] + 1
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heappush(queue, (cost, neighbor))
    return dist[dst]

print(min(dijkstra(c, e_pos) for c in grid if grid[c] == ord('a') and ord('b') in map(grid.get, neighbors(c))))