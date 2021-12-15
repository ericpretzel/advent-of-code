puzzle_input = [s.strip() for s in open('input.in').readlines()]
width, height = len(puzzle_input[0]), len(puzzle_input)

risk = {}
for x in range(width):
    for y in range(height):
        risk[(x, y)] = int(puzzle_input[y][x])


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
    unvisited = set()
    for node in risk:
        dist[node] = 99999999999
        unvisited.add(node)
    dist[src] = 0
    current = src
    while dst in unvisited:
        for neighbor in filter(lambda n: n in unvisited, neighbors(current)):
            dist[neighbor] = min(dist[neighbor], dist[current] + risk[neighbor])
        unvisited.remove(current)
        # idk
        min_dist = 99999999999
        for node in unvisited:
            if dist[node] <= min_dist:
                min_dist = dist[node]
                current = node
    return dist[dst]
                
print("lowest risk:", dijkstra_risk((0,0), (width-1, height-1)))