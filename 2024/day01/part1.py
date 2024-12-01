lines = [line.strip() for line in open("input.in").readlines()]

left = sorted(int(x.split()[0]) for x in lines)
right = sorted(int(x.split()[1]) for x in lines)

print('part 1:', sum(abs(x - y) for x, y in zip(left, right)))

left_count = {x: left.count(x) for x in left}
right_count = {x: right.count(x) for x in right}

print('part 2:', sum(x * right_count.get(x, 0) * left_count[x] for x in left_count.keys()))