from heapq import heappop, heappush # for priority queue

puzzle_input = [s.strip() for s in open('input.in').readlines()]
width, height = len(puzzle_input[0]), len(puzzle_input)

risk = {}
for x in range(width):
    for y in range(height):
        for i in range(5):
            for j in range(5):
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
    unvisited = set()
    for node in risk:
        dist[node] = 99999999999
        unvisited.add(node)
    dist[src] = 0
    heappush(queue, (0, src))
    while dst in unvisited:
        current = heappop(queue)[1]
        unvisited.remove(current)
        for neighbor in filter(lambda n: n in unvisited, neighbors(current)):
            if dist[current] + risk[neighbor] < dist[neighbor]:
                if neighbor in queue: queue.remove((dist[neighbor], neighbor))
                dist[neighbor] = dist[current] + risk[neighbor]
                heappush(queue, (dist[current] + risk[neighbor], neighbor))
    return dist[dst]
                
print("lowest risk:", dijkstra_risk((0,0), (width*5-1, height*5-1)))