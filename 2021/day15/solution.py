from heapq import heappop, heappush # for min-priority queue

puzzle_input = [s.strip() for s in open('input.in').readlines()]
width, height = len(puzzle_input[0]), len(puzzle_input)

risk = {}
for x in range(width):
    for y in range(height):
        for i in range(5): # set range to 1 for part 1
            for j in range(5): # set range to 1 for part 1
                c = (x+width*i, y+height*j)
                risk[c] = int(puzzle_input[y][x]) + i + j
                if risk[c] > 9: risk[c] %= 9

def neighbors(coord):
    x, y = coord[0], coord[1]
    n = (x, y-1)
    e = (x+1, y)
    s = (x, y+1)
    w = (x-1, y)
    return filter(lambda c: c in risk,\
        [n,e,s,w])

def dijkstra_risk(src, dst):
    dist = {}
    queue = []
    for node in risk:
        dist[node] = 999999
        heappush(queue, (dist[node], node))
    
    dist[src] = 0
    heappush(queue, (0, src))
    while len(queue) > 0:
        current = heappop(queue)[1]
        for neighbor in neighbors(current):
            cost = dist[current] + risk[neighbor]
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heappush(queue, (cost, neighbor))
    return dist[dst]
                
print("lowest risk:", dijkstra_risk((0,0), (width*5-1, height*5-1))) # change to width-1, height-1 for part 1