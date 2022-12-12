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
    return filter(lambda c: c in grid and grid[(x, y)] - grid[c] <= 1, [n,e,s,w])

def dijkstra(src, dst = None):
    dist = {}
    queue = []
    for node in grid:
        dist[node] = 999999
        heappush(queue, (dist[node], node))
    
    dist[src] = 0
    heappush(queue, (0, src))
    while len(queue) > 0:
        current = heappop(queue)[1]
        for neighbor in neighbors(current):
            cost = dist[current] + 1
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heappush(queue, (cost, neighbor))
    return dist if dst is None else dist[dst]

dist = dijkstra(e_pos)
print(min(dist[c] for c in grid if grid[c] == ord('a')))